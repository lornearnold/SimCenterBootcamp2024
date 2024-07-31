
from Plotter import *
from Point import *
from Square import *
from Triangle import *
from Circle import *

def problem1():
    x = Plotter()
    shapes = []
    shapes.append( Square( Point(), 4 ) )
    shapes.append( Square( Point(2,1), 4, color='green') )
    for shape in shapes:
        x.addObject(shape)
    x.plot()
    x.export('problem1.png')

def problem2():
    x = Plotter()
    x.addObject( Square( Point(), 4, fill=True ) )
    x.addObject( Triangle( Point(2,1), 4, color='green' ) )
    x.addObject( Circle( Point(1,2), 1, color='blue', fill=True) )
    x.plot()
    x.export('problem1.png')


if __name__ == '__main__':
    problem1()
