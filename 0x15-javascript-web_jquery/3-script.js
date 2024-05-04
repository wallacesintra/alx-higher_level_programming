#!/usr/bin/node

/**
 * adds the class red to the <header> element
 * when the user clicks on the tag DIV#red_header
 *
 * can’t use document.querySelector to select the HTML tag
*/

$('DIV#red_header').click(function () {
  $('header').addClass('red');
}
);
