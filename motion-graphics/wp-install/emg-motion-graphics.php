<?php
/**
 * Plugin Name: EMG Motion Graphics
 * Description: Swaps the static section graphics on the Web Design, Digital Marketing, and Public Relations pages for the looping SVG/CSS motion graphics. No theme edits; delete this file (and the emg-motion folder) to undo.
 * Version: 1.0.0
 *
 * Install: copy this file and the emg-motion/ folder into wp-content/mu-plugins/.
 * Must-use plugins load automatically; there is nothing to activate.
 */

if (!defined('ABSPATH')) {
	exit;
}

/**
 * Page slug => how to find the old graphic in the rendered page, and which partial replaces it.
 */
function emg_motion_targets() {
	return [
		'web-design' => [
			// Everything inside .media-content__loop (the old "elloop" animation).
			'pattern' => '#(<div class="media-content__loop">).*?(?=</div>\s*</div>\s*<div class="col col--right)#s',
			'keep_prefix' => true,
			'partial' => 'web-design.html',
		],
		'digital-marketing-solutions' => [
			'pattern' => '#<img[^>]*marketing-circle@2x-1\.webp[^>]*>#',
			'keep_prefix' => false,
			'partial' => 'digital-marketing.html',
		],
		'public-relations' => [
			'pattern' => '#<img[^>]*public-relations-graphic\.webp[^>]*>#',
			'keep_prefix' => false,
			'partial' => 'public-relations.html',
		],
	];
}

function emg_motion_current_target() {
	if (is_admin() || wp_doing_ajax() || is_feed() || !is_page()) {
		return null;
	}
	$slug = get_post_field('post_name', get_queried_object_id());
	$targets = emg_motion_targets();
	return isset($targets[$slug]) ? $targets[$slug] : null;
}

add_action('wp_enqueue_scripts', function () {
	if (!emg_motion_current_target()) {
		return;
	}
	$dir = WPMU_PLUGIN_DIR . '/emg-motion/';
	$url = WPMU_PLUGIN_URL . '/emg-motion/';
	wp_enqueue_style('emg-motion', $url . 'emg-motion.css', [], filemtime($dir . 'emg-motion.css'));
	wp_enqueue_script('emg-motion', $url . 'emg-motion.js', [], filemtime($dir . 'emg-motion.js'), true);
	// The old Web Design animation's stylesheet is no longer needed once its markup is gone.
	wp_dequeue_style('elysium-loop');
}, 20);

add_action('template_redirect', function () {
	$target = emg_motion_current_target();
	if (!$target) {
		return;
	}
	ob_start(function ($html) use ($target) {
		$file = WPMU_PLUGIN_DIR . '/emg-motion/partials/' . $target['partial'];
		if (!is_readable($file)) {
			return $html;
		}
		$partial = file_get_contents($file);
		$replaced = preg_replace_callback($target['pattern'], function ($m) use ($partial, $target) {
			return ($target['keep_prefix'] ? $m[1] : '') . $partial;
		}, $html, 1, $count);
		// If the page markup changed and nothing matched, leave the page exactly as it was.
		return ($replaced !== null && $count === 1) ? $replaced : $html;
	});
});
