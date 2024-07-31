import matplotlib.pyplot as plt

class Plotter():

    def __init__(self):
        self.clear()

    def _draw(self, ax):
        ax.set_title('Shapes')
        for obj in self.objects:
            obj.plot(ax)
        ax.set_aspect('equal')

    def plot(self):
        ax = plt.gca()
        self._draw(ax)
        plt.show()

    def addObject(self, obj):
        self.objects.append(obj)

    def clear(self):
        self.objects = []

    def export(self, filename):
        self._draw(plt.gca())
        plt.savefig(filename)
        # the next line should not be necessary but jupyter-notebook is doing weird stuff otherwise
        plt.clf()
