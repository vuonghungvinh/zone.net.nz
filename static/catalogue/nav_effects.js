/*
Product navigation effects.
*/

/*jslint browser: true, indent: 4, maxlen: 80, plusplus: true, vars: true */
/*global $, console, jQuery,  */

(function () {
    "use strict";

    function showNavigation(event) {
        var container, nav, target;

        // Ensure navigation state & events.
        hideNavigation();
        setupEvents();

        target = event.target;
        if (target.localName !== 'a') {
            target = $(target).parents('a')[0]
        }

        // Enable category nav links
        $(target).off('click');

        // Show selected sub category nav
        container = $(event.target).parents('li');
        if (container.length > 1) {
            container = container[0];
        }
        nav = $(container).find('ul');
        nav.show();

        $(container).mouseleave(hideNavigation);
        return false;
    }

    function hideNavigation() {
        $('.categories .sub-categories').hide();
    }

    function setupEvents() {
        $('.categories a').not('.sub-categories a').click(showNavigation);
    }

    function init() {
        hideNavigation();
        setupEvents();
    }

    jQuery(init);

}());
