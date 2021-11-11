var scale = 0.5;
window.addEventListener('load', function () {
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
    img.onload = function () {
        var w = img.naturalWidth;
        var h = img.naturalHeight;
        canvas.width = w;
        canvas.height = h;
        var scale = 0.5;
        context.drawImage(img, 0, 0);
        context.drawImage(img, 0 // 画像上の描画開始位置X
        , 0 // 画像上の描画開始位置Y
        , w // 描画する画像の幅
        , h // 描画する画像の高さ
        , 0 // 描画位置X
        , 0 // 描画位置Y
        , w * scale // 描画幅
        , h * scale // 描画高さ
        );
    };
    canvas.addEventListener('click', function (e) {
        var r = e.target.getBoundingClientRect();
        var click_x = e.clientX / scale - r.left;
        var click_y = e.clientY / scale - r.top;
        var request = new XMLHttpRequest();
        var crop_uri = '/crop?x=' + click_x + '&y=' + click_y;
        console.log(crop_uri);
        request.open('GET', crop_uri, true);
        request.responseType = 'text';
        request.onload = function () {
            var a_font_path = request.response;
            console.log(a_font_path);
            var frame_several = document.getElementById('frame_several');
            var frame_several_doc = frame_several.contentDocument || frame_several.contentWindow.document;
            var fonts = frame_several_doc.getElementById('Fonts');
            var a_font_elem = frame_several_doc.getElementById('a_font_img');
            var a_font_elem2 = a_font_elem.cloneNode(true);
            a_font_elem2.src = a_font_path;
            fonts.appendChild(a_font_elem2);
        };
        request.send();
    }, false);
}, false);
