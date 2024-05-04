#!/usr/bin/node

/**
 *  fetches and prints how to say “Hello” depending on the language
 * - The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 * - The translation must be fetched when the user clicks on INPUT#btn_translate
 * - The translation of “Hello” must be displayed in the tag DIV#hello
*/

const $ = window.$;

window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    showHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
};

function showHello () {
  const lan = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}
