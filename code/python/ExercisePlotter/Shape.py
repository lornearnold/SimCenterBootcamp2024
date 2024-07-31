import numpy as np
from matplotlib import colors
from Point import *

class Shape():

    def __init__(self, ref = Point(), side=1, color='red', fill=False):
        self.refPt = ref       # reference point
        self.side = side       # side length
        self.n = 1             # number of sides
        self.dir = 0.0         # starting angle for plotting
        self.color = color     # shape outline color
        self.filled = fill

    def plot(self, axis):
        dtheta = 360./self.n
        pt = self.startPoint()

        theta = self.dir
        x = [pt.x]
        y = [pt.y]
        for i in range(self.n):
            pt = pt.pointAt(theta, self.side)
            x.append(pt.x)
            y.append(pt.y)
            theta += dtheta

        if self.filled:
            axis.fill(x,y, color=self.color)
        else:
            axis.plot(x,y, color=self.color)

    def translate(self, dir, dist=1):
        pass

    def rotate(self, angle):
        pass

    def startPoint(self):
        return self.refPt
