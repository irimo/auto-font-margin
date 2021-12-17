#coding: utf-8

import ufo2svg

# from ttfquery import describe
# from ttfquery import glyphquery
# import ttfquery.glyph as glyph

# char = "a"
# font_url = "/home/dist/ttfs/VL-Gothic-Regular.ttf"
# font = describe.openFont(font_url)
# g = glyph.Glyph(char)
# contours = g.calculateContours(font)
# for contour in contours:
#     for point, flag in contour:
#         print(point, flag)

# class pad :
#     def outputImages() :
#         from font2img import ParseTTFFont
#         # import cv2
#         # import PIL

#         p = ParseTTFont("dist/ttfs/VL-Gothic-Regular.ttf") # 载入当前目录下的 font_file.woff 字体文件
#         glyphnames = p.get_glyphnames() # 获取字体文件中所有有效字形的代号

#         # im 类型为 PIL.Image
#         im = p.one_to_image(glphnames[10]) # 获取第 11 个字形的图像
#         im.show()
#         im.save("./resource/hoge11.jpg")
#         # 将所有字形整合成一张图像, 所有图像类型为 PIL.Image
#         # image: 包含所有字形的图形
#         # name_list: 包含所有字形的代号
#         # image_dict: 各字形图像同其代号的字典
#         image, name_list, image_dict = p.all_to_image() 

# pad.outputImages()

import argparse
import defcon
import extractor
ttf_path = "./dist/ttfs/VL-Gothic-Regular.ttf"
ufo_path = "./dist/ufos/VL.ufo"

def ttf_to_svg():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-i", help = "input filename")
    # parser.add_argument("-o", help = "output filename")
    # args = parser.parse_args()
    # return args

    # args = create_arg_parser()
    ttf_path = "./dist/ttfs/VL-Gothic-Regular.ttf"
    ufo_path = "./dist/ufos/VL.ufo"
    # print('ttf_path: ', ttf_path)
    # print('ufo_path:', ufo_path)
    # # Make UFO
    # print('Generating UFO...', ufo_path)
    ufo = defcon.Font()
    extractor.extractUFO(ttf_path, ufo)
    # ufo.save(ufo_path)
    svg_path = "./dist/svgs/VL.svg"
    ufo2svg.convertUFOToSVGFont(ufo, svg_path)
    print('Done.')

# ttf2ufo()

# def ufo_to_svg():
#     svg_path = "./dist/svgs/"
#     ufo2svg.convertUFOToSVGFont(ufo_path)

ttf_to_svg()