/*********************************************************************************

    Template Name: Fsulting - Financial Consulting Bootstrap 4 Template
	Description: Fsulting is a beautiful and unique financial & consulting html template which comes with bootstrap 4 framework.
	Version: 1

    Note: This is scripts js. All custom scripts here.
    URL: http://www.bootstrapmb.com
**********************************************************************************/

/*===============================================================================
			[ INDEX ]
=================================================================================

    Inline Background Image
    Sticky Header
    Only Content Sticky Blog
    Contact Effect
    Menu Dropdown Last

=================================================================================
			[ END INDEX ]
================================================================================*/

(function($) {
	'use strict';


    /* Sticky Header */
    function stickyHeader(){
        var header = $('.sticky--header');
        $(window).on('scroll', function(){
            var scrollOffset = $(this).scrollTop();
            if(scrollOffset > 300){
                header.addClass('is-sticky');
            }
            else{
                header.removeClass('is-sticky');
            }
        });
    }
    stickyHeader();



    /* Only Content Sticky Blog */
    function onlyContentStickyBlog(){
        $('.blog').each(function(){
            var check = $(this).find('.blog__thumb').length;
            if(!check){
                $(this).addClass('blog--onlycontent');
            }
        });
    }
    onlyContentStickyBlog();


    /* Contact Effect */
    function contactEffect(){
        var container = $('.single-input');
        container.on('focus', 'input, textarea', function () {
            $(this).siblings('label').addClass('state-change');
        });
        container.on('focusout', 'input, textarea', function () {
            $(this).siblings('label').removeClass('state-change');
            var $this = $(this);
            if ($this.val().trim().length !== 0) {
                $(this).siblings('label').addClass('state-change');
            }
        });
    }
    contactEffect();



    /* Menu Dropdown Last */
    function menuDropdownLast(){
        $('.main-navigation > ul > li').slice(-3).addClass('last-elements');
    }
    menuDropdownLast();


    /* Inline Background Image */
    function bgImageSet(){
        $('[data-bgimage]').each(function(){
            var bgImageUrl = $(this).data('bgimage');
            $(this).css({
                'background-image': 'url('+bgImageUrl+')'
            });
        });
    }
    bgImageSet();



})(jQuery);