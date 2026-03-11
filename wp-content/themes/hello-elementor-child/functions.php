<?php
/**
 * Hello Elementor Child Theme Functions
 *
 * @package HelloElementorChild
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue child theme styles
 */
function hello_elementor_child_enqueue_styles() {
    wp_enqueue_style(
        'hello-elementor-child-style',
        get_stylesheet_uri(),
        [ 'hello-elementor-style' ],
        wp_get_theme()->get( 'Version' )
    );
}
add_action( 'wp_enqueue_scripts', 'hello_elementor_child_enqueue_styles' );

/**
 * Enqueue Google Fonts — DM Sans and Inter
 */
function hello_elementor_child_google_fonts() {
    wp_enqueue_style(
        'hello-elementor-child-fonts',
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600&display=swap',
        [],
        null
    );
}
add_action( 'wp_enqueue_scripts', 'hello_elementor_child_google_fonts' );
