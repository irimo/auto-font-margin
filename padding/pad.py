#coding: utf-8

from ttfquery import describe
from ttfquery import glyphquery
import ttfquery.glyph as glyph

char = "a"
font_url = ./dist/ttfs/VL-Gothic-Regular.ttf"
font = describe.openFont(font_url)
g = glyph.Glyph(char)
contours = g.calculateContours(font)
for contour in contours:
    for point, flag in contour:
        print point, flag