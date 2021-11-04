#coding: utf-8
from flask import Flask, render_template
import cv2

app = Flask(__name__, static_folder='./resource')

@app.route('/')
def page_index():
    return render_template("index.html")

@app.route('/all')
def page_all():
    return render_template("all.html")

@app.route('/several')
def page_several():
    return render_template("several.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)