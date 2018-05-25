#!/usr/bin/python

from pysvg.structure import *
from pysvg.builders import *
import json


DOTS_PER_CM = 2.8 # 2.8 dots per mm for screen @ 72dpi

class Layout:
    def __init__(self, height, width):
        self.shape_builder = ShapeBuilder()
        self.doc = Svg()
        height = height #* DOTS_PER_CM
        width = width  #*DOTS_PER_CM
        self.doc.addElement(self.shape_builder.createRect(0, 0, "%dpx" % height, "%dpx" % width,
                                                          strokewidth = 3))

    def add(self, x, y, h, w):
        x = x * DOTS_PER_CM/10
        y = y * DOTS_PER_CM/10
        h = h * DOTS_PER_CM/10
        w = w * DOTS_PER_CM/10
        self.doc.addElement(self.shape_builder.createRect(str(x), str(y), "%dpx" % h, "%dpx" % w))

    def save(self, filename):
        self.doc.save(filename)

def printviz():
    FFDH_result = open('FFDH_result.json', 'r')
    papers_list = json.load(FFDH_result)

    layout_counter = 0

    for paper in papers_list:
        layout = Layout(1189 * DOTS_PER_CM / 10, 841 * DOTS_PER_CM / 10)
        x = 0
        y = 0
        for level in paper['items']:
            item_list = level[1]['items']
            for element in item_list:
                height = element[0]
                width = element[1]
                layout.add(x, y, width, height)
                x+=width
            y += max(i[0] for i in item_list)
            x = 0

        layout_counter += 1
        layout.save("layout_" + str(layout_counter) + ".svg")


printviz()

