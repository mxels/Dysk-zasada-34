
$(function() {
	//resizeTo(800,600);
  var b = $('#body');
	//要素の高さを取得する
	var iHeight = b.outerHeight(true);
	//$(window).width=500;
	window.resizeTo(450,iHeight+100);
//  window.alert(
//    'height/width:' + b.height() + '/' + b.width() + '\n' +
//    'innerHeight/innerWidth:'
//          + b.innerHeight() + '/' + b.innerWidth() + '\n' +
//    'outerHeight/outerWidth:'
//          + b.outerHeight() + '/' + b.outerWidth() + '\n' +
//    'outerHeight/outerWidth(true):'
//          + b.outerHeight(true) + '/' + b.outerWidth(true)
//  );
});
