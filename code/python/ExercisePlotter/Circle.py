from Shape import *
from numpy import pi

class Circle(Shape):

    def __init__(self, centerPt, radius, color='red', fill=False):
        N = 36
        ref = centerPt.pointAt(270., radius)
        side = 2 * pi * radius / N
        super().__init__(ref, side, color=color, fill=fill)
        self.n = N
