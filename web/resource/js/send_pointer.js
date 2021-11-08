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
    context.drawImage(img, 0, 0);
  }

  canvas.addEventListener('click', e=>{
    var r = e.target.getBoundingClientRect();
    var click_x = e.clientX - r.left;
    var click_y = e.clientY - r.top;
    console.log("click point: x = %d, y = %d", click_x, click_y);

    var request = new XMLHttpRequest();
    var crop_uri = '/crop';
    request.open('GET', crop_uri, true);
    request.responseType = 'text';
    request.onload = function() {
      var a_font_path = request.response;
      var frame_several = document.getElementById('frame_several');
      var frame_several_doc = frame_several.contentDocument || frame_several.contentWindow.document;
      var fonts = frame_several_doc.getElementById('Fonts');
      var a_font_elem = frame_several_doc.getElementById('a_font_img');
      a_font_elem.src = a_font_path;
    };
    request.send();

  }, false);
}, false);