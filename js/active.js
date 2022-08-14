/*********************************************************************************

    Template Name: Fsulting - Financial Consulting Bootstrap 4 Template
	Description: Fsulting is a beautiful and unique financial & consulting html template which comes with bootstrap 4 framework.
	Version: 1

	Note: This is active js. Plugins activation code here.

**********************************************************************************/


/*===============================================================================
			[ INDEX ]
=================================================================================

	Scroll Up Activation
	Slider Activation
	Banner Slider
	Testimonial Content
	Testimonial Author
	Blog Slider
	Wowjs active
	CounterUp Active
	Mobile menu
	Selct2 active
	Instafeed active
	Fake Loader
	Portfolio Filter & Zoom Active
	Portfolio Zoom Active
	Video Popup
	
=================================================================================
			[ END INDEX ]
================================================================================*/

(function ($) {
	'use strict';


	/* Scroll Up Activation */
	$.scrollUp({
		scrollText: '<i class="fa fa-angle-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'slide'
	});




	/* Slider Activation */
	// Banner Slider
	$('.banner-slider-active').slick({
		arrows: true,
		infinite: true,
		pauseOnHover: true,
		slidesToShow: 1,
		slideToScroll: 1,
		fade: true,
		cssEase: 'ease-out',
		easing: 'ease-out',
		speed: 600,
		adaptiveHeight: true,
		prevArrow: '<button class="cr-slick-arrow cr-slick-prev"><i class="fa fa-angle-left"></i></button>',
		nextArrow: '<button class="cr-slick-arrow cr-slick-next"><i class="fa fa-angle-right"></i></button>'
	});




	// Testimonial Content
	$('.testimonial-content-slider-active').slick({
		adaptiveHeight: true,
		autoplay: true,
		autoplaySpeed: 8000,
		arrows: false,
		infinite: true,
		pauseOnHover: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		asNavFor: '.testimonial-author-slider-active'
	});



	// Testimonial Author
	$('.testimonial-author-slider-active').slick({
		centerMode: true,
		autoplay: true,
		autoplaySpeed: 8000,
		arrows: false,
		focusOnSelect: true,
		infinite: true,
		pauseOnHover: true,
		slidesToShow: 3,
		slideToScroll: 1,
		asNavFor: '.testimonial-content-slider-active',
		responsive: [{
			breakpoint: 577,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
		}]
	});



	// Blog Slider
	$('.blog--slider-active .blog__thumb').slick({
		arrows: true,
		infinite: true,
		pauseOnHover: true,
		slidesToShow: 1,
		slideToScroll: 1,
		prevArrow: '<button class="cr-slick-arrow cr-slick-prev"><i class="fa fa-angle-left"></i></button>',
		nextArrow: '<button class="cr-slick-arrow cr-slick-next"><i class="fa fa-angle-right"></i></button>'
	});



	/* Wowjs active */
	new WOW().init();





	/* CounterUp Active */
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});



	/* Mobile menu */
	$('nav.main-navigation').meanmenu({
		meanMenuClose: '<i class="flaticon-close"></i>',
		meanMenuCloseSize: '18px',
		meanScreenWidth: '991',
		meanExpandableChildren: true,
		meanMenuContainer: '.mobile-menu',
		onePage: true
	});




	/* Selct2 active */
	$('select').select2();




	/* Instafeed active */
	if ($('#sidebar-instagram-feed').length) {

		var userFeed = new Instafeed({
			get: 'user',
			userId: 6665768655,
			accessToken: '6665768655.1677ed0.313e6c96807c45d8900b4f680650dee5',
			target: 'sidebar-instagram-feed',
			resolution: 'thumbnail',
			limit: 6,
			template: '<li><a href="{{link}}" target="_new"> <img src="{{image}}" /><ul class="likes-comments"><li><i class="fa fa-heart-o"></i><span>{{likes}}</span></li><li><i class="fa fa-comments-o"></i><span>{{comments}}</span></li></ul></a></li>',
		});
		userFeed.run();

	}



	/* Fake Loader */
	$('.fakeloader').fakeLoader({
		timeToHide: 1200,
		bgColor: 'rgba(225,225,225,0.95)',
		spinner: 'spinner2'
	});



	/* Portfolio Filter & Zoom Active */
	function portfolioActivation() {

		var $gallery = $('.portfolio-wrap');
		var $boxes = $('.portfolio-item');
		$boxes.hide();
		$gallery.imagesLoaded({
			background: true
		}, function () {
			$boxes.fadeIn();
			$gallery.isotope({
				itemSelector: '.portfolio-item',
			});
		});

		var filterValueNew = '.portfolio-zoomicon';
		$('.portfolio-filters').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$('.portfolio-wrap').isotope({
				filter: filterValue
			});

			filterValueNew = '' + filterValue + ' .portfolio-zoomicon';
			if (filterValueNew == '* .portfolio-zoomicon') {
				filterValueNew = '.portfolio-zoomicon';
			}
			$gallery.data('lightGallery').destroy(true);
			$gallery.lightGallery({
				selector: filterValueNew,
				thumbnail: false,
			});
		});

		$gallery.lightGallery({
			selector: filterValueNew,
			thumbnail: false,
		});

		$('.portfolio-filters').on('click', 'button', function () {
			$('.portfolio-filters button').removeClass('is-active');
			$(this).addClass('is-active');
		});

	}
	portfolioActivation();



	/* Portfolio Zoom Active */
	$('.portfolio-gallery-active').lightGallery({
		selector: '.portfolio-zoomicon',
		thumbnail: false
	});


	/* Video Popup */
	$('.videopopup-box').lightGallery({
		selector: '.video-btn'
	});





})(jQuery);