// $('a#lang_pt').click(function(){ 
//  $( "form#select_lang" ).submit();
// })
$("#lang_pt").on('click', function() {
	$('#language').val("pt-br");
	$( "form#select_lang" ).submit();
});
$("#lang_en").on('click', function() {
	$('#language').val("en");
	$( "form#select_lang" ).submit();
});
$("#lang_pl").on('click', function() {
	$('#language').val("pl");
	$( "form#select_lang" ).submit();
});