window.addEventListener('load', function(){
    // alert('aaaaaa');
        var frame_all = document.getElementById('frame_all');

        var canvas = frame_all.getElementById('SimpleCanvas');
  
        if (!canvas || !canvas.getContext) {
          return false;
        }
        var context = canvas.getContext('2d');
        
        var img = new Image();
        
        img.onload = function onImageLoad() {
          context.drawImage(img, 640, 480);
        }
       
        img.src = './resource/law1.jpg'; //相対URLの場合
        //img.src = 'http://www.ipentec.com/images/img01.png'; //絶対URLの場合
}, false);

document.addEventListener('DOMContentLoaded',function(){
    var frame_all = document.getElementById('frame_all');
    var law1 = frame_all.getElementsByClassName('law1');
    // law1.addEventListener('click', function(){
    //     alert('赤ピクミンは火に強い');
    // });
    // for(var i = 0; i < btns.length; i++){
    //     btns[i].addEventListener('click',function(){
    //         alert('クリックされたよ！');
    //         this.style.color = 'blue';
    //     },false);
}, false);