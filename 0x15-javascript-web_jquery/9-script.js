#!/usr/bin/node

/**
 * fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
 * The translation of “hello” must be displayed in the HTML tag DIV#hello
 *
 */

$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
}
);
