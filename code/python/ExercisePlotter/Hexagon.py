from Shape import *

class Hexagon(Shape):

    def __init__(self, ref, side, color='red', fill=False, center=False):
        super().__init__(ref, side, color=color, fill=fill)
        self.n = 6
