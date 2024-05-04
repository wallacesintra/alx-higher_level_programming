#!/usr/bin/node

/**
 *  updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
 *
 * can’t use document.querySelector to select the HTML tag
 *
*/

$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
}
);
