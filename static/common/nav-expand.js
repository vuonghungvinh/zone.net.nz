/*
Expand and contract site navigation.
*/

/*jslint browser: true, indent: 4, maxlen: 80, plusplus: true, vars: true */
/*global $, console, jQuery,  */

(function () {
    "use strict";

    var navContainer;

    function open(e) {
        $(navContainer).find('ul.nav').slideToggle(function() {
            $('.nav-close').show();
        });
        e.preventDefault();
    }

    function close(e) {
        $('.nav-close').hide();
        $(navContainer).find('ul.nav').slideToggle();
        e.preventDefault();
    }

    function init() {
        var navClose, navExpand;

        navContainer = $('li#product-nav');
        navExpand = $('a.nav-expand');
        navClose = $('a.nav-close');

        $(navExpand).click(open);
        $(navClose).click(close);
    }

    jQuery(init);

}());
