window.addEventListener('load', function(){
  var frame_all = document.getElementById('frame_all');
  var frame_all_doc = frame_all.contentDocument || frame_all.contentWindow.document;
  // frame_all.contentDocument.getElementBy では取れない(JSあるある)
  var canvas = frame_all_doc.getElementById('SimpleCanvas');

  if (!canvas || !canvas.getContext) {
    console.log("cannot get the canvas");
    return false;
  }
  var context = canvas.getContext('2d');
  
  var img = new Image();
  img.src = './../resource/law1.jpg'; //相対URLの場合
  
  img.onload = function() {
    console.log("img onload now");
    //   // 画像imageを(dx,dy)の位置に表示する
    //  context.drawImage(image, dx,dy);

    //   // 画像imageを(dx,dy)の位置に幅dw、高さdhに拡大/縮小して表示する
    //  context.drawImage(image, dx,dy,dw,dh);

    //   // 画像imageの指定した矩形領域（左上(sx,sy)、幅sw、高さsh）をCanvasの(dx,dy)の位置に幅dw、高さdhで表示する
    //   context.drawImage(image, sx,sy,sw,sh, dx,dy,dw,dh)
    context.drawImage(img, 0, 0);
  }

  canvas.addEventListener('click', function() {
    alert('shuzo');
  }, false);
}, false);