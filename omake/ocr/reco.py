from pytesseract import pytesseract
from PIL import Image
import os

if __name__ == '__main__':

    # for imgid in range(1, 5):
    img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/miyazawa.jpg", "r");

    # インストールしたtesseractコマンドのパス
    pytesseract.tesseract_cmd = "/usr/bin/tesseract";

    # -psm 8は1文字判定のフラグ
    result = pytesseract.image_to_string(img, config="--psm 10", lang="eng");
    # result = pytesseract.image_to_string(crop, config="--psm 10", lang="eng+jpn");

    print(result);