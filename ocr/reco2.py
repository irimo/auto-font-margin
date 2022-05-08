# -*- coding: utf-8 -*-
###############################################################################
# ライブラリインポート
###############################################################################
import os                       # os の情報を扱うライブラリ
# from PIL import Image           # 画像処理ライブラリ
import cv2
import matplotlib.pyplot as plt # データプロット用ライブラリ
import numpy as np              # データ分析用ライブラリ
import pyocr                    # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import pyocr.builders           # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import sys                      # 実行環境関連ライブラリ
 
# カレントディレクトリを変更する
# os.chdir("C:\\作業\ocr-Preprocessing")
 
Image000 = 'sample1.png'
 
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
 
tool = tools[0]
pyocr.tesseract.TESSERACT_CMD = "/usr/bin/tesseract"
    
#################### 画像の読み込み ####################
# img = Image.open(Image000)
img = cv2.imread(Image000)
txt = tool.image_to_string(
        img,
        lang="eng",
        # config="--psm 10",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
 
# 画像を配列に変換
im_list = np.array(img)
 
# データプロットライブラリに貼り付け
plt.imshow(im_list)
 
# 表示
plt.show()
 
# 抽出したテキストの出力
print()
print("text ↓")
print(txt)
print()