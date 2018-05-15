#!/usr/bin/python

import pysvg.structure
import pysvg.builders

shape_builder = pysvg.builders.ShapeBuilder()

class Layout:
    def __init__(self, height, width):
        self.shape_builder = pysvg.builders.ShapeBuilder()
        self.doc = pysvg.structure.Svg()
        self.doc.addElement(self.shape_builder.createRect(0, 0, "%dpx" % height, "%dpx" % width,
                                                          strokewidth = 3))

    def add(self, x, y, h, w):
        self.doc.addElement(self.shape_builder.createRect(x, y, "%dpx" % h, "%dpx" % w))

    def save(self, filename):
        self.doc.save(filename)

# A4@75dpi
layout = Layout(620, 877)

layout.add(0, 0, 200, 100)
layout.add(0, 105, 200, 50)
layout.add(205, 0, 300, 450)

layout.save("layout.svg")