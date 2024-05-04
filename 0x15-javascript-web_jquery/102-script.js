#!/usr/bin/node

/**
 * script that fetches and prints how to say “Hello” depending on the language
 *
 * - use this API service: https://www.fourtonfish.com/hellosalut/hello/
 * - the language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 * - the translation must be fetched when the user clicks on INPUT#btn_translate
 * - the translation of “Hello” must be displayed in the tag DIV#hello
*/

const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
};
