#coding: utf-8
from flask import Flask, request, render_template
import cv2
import random

app = Flask(__name__, static_folder='./resource')

@app.route('/')
def page_index():
    return render_template("index.html")

@app.route('/all.html')
def page_all():
    return render_template("all.html")

@app.route('/several.html')
def page_several():
    return render_template("several.html")

@app.route('/crop')
def page_crop():
    click_x: int = int(request.args.get('x', ''))
    click_y: int = int(request.args.get('y', ''))
    law_path = "./resource/law1.jpg"
    # crop 処理をした後、処理後画像を返す
    randstr = str(random.randint(1000000000, 10000000000))
    filename:str = "/resource/work/" + randstr + ".jpg"
    im = cv2.imread(law_path)
    # img[top : bottom, left : right]
    # サンプル1の切り出し、保存
    img1 = im[click_y : click_y + 200, click_x: click_x + 200]
    # random.randrange(3, 8)
    cv2.imwrite("." + filename, img1)
    # return cv2.imshow('test', im)
    # return im.shape
    return filename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)