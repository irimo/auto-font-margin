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
svg_path = "./dist/svgs/"
png_path = "./dist/pngs/"

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

def save_all_glyph_as_svg(font):
    from textwrap import dedent
    from fontTools.pens.svgPathPen import SVGPathPen

    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()

    for c in cmap:
        glyph_name = cmap[c]
        glyph = glyph_set[glyph_name]
        svg_path_pen = SVGPathPen(glyph_set)
        glyph.draw(svg_path_pen)

        ascender = font['OS/2'].sTypoAscender
        descender = font['OS/2'].sTypoDescender
        width = glyph.width
        height = ascender - descender

        content = dedent(f'''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-ascender} {width} {height}">
                <g transform="scale(1, -1)">
                    <path d="{svg_path_pen.getCommands()}"/>
                </g>
            </svg>
        ''')
        with open(svg_path + glyph_name + ".svg", 'w') as f:
            f.write(content) 

def convert_all_svg_to_png():
    from cairosvg import svg2png
    import os
    files = os.listdir(svg_path)
    files_file = [f for f in files if os.path.isfile(os.path.join(svg_path, f))]
    for fname in files_file:
        bname, ext =  os.path.splitext(fname)

        try:
            svg2png(url=svg_path + bname + '.svg', write_to=png_path + bname + '.png')
        except:
            print(fname)
    return 

def ttf_to_png():
    from fontTools.ttLib import TTFont
    font = TTFont(ttf_path)
    save_all_glyph_as_svg(font)
    convert_all_svg_to_png()

ttf_to_png()