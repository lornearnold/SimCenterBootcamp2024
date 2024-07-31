from Shape import *

class Triangle(Shape):

    def __init__(self, ref, side, color='red', fill=False):
        super().__init__(ref, side, color=color, fill=fill)
        self.n = 3
