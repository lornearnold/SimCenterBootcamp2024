import numpy as np

class Point():

    def __init__(self, X=0., Y=0.):
        self.x = X
        self.y = Y

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)

    def dirTo(self, other):
        return np.array([other.x - self.x, other.y - self.y])

    def distanceTo(self, other):
        return np.linalg.norm( self.dirTo(other) )

    def pointAt(self, dir, dist):
        # dir is an angle in degrees
        x = self.x + np.cos( np.radians(dir) ) * dist
        y = self.y + np.sin( np.radians(dir) ) * dist
        return Point(x,y)


if __name__ == '__main__':
    v1 = Point(3,2)
    v2 = Point(4,-1)
    print("v1 : ",v1)
    print("v2 : ",v2)
    print("v1->v2: ", v1.dirTo(v2))
    print("v2->v1: ", v2.dirTo(v1))
    print("|v1->v2|: ", v1.distanceTo(v2))
    print("|v2->v1|: ", v2.distanceTo(v1))
    print("square:")
    print("   ", v1)
    p2 = v1.pointAt(0, 10)
    print("   ", p2)
    p3 = p2.pointAt(90, 10)
    print("   ", p3)
    p4 = p3.pointAt(180, 10)
    print("   ", p4)
    p5 = p4.pointAt(270, 10)
    print("   ", p5)