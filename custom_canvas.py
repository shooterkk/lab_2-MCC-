from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure, Axes
from PyQt5 import QtWidgets

class StaticCanvas(FigureCanvas):

    def __init__(self, parent=None, title=None, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        if title:
            self.axes.set_title(title)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def set_xlim(self, *limits):
        self.axes.set_xlim(left=limits[0], right=limits[1])

    def set_ylim(self, *limits):
        self.axes.set_ylim(left=limits[0], right=limits[1])

    def clear(self):
        self.axes.clear()

    def plot(self, *args, **kwargs):
        self.axes.plot(*args,**kwargs)
        self.axes.grid(True)
        self.draw()

    def set_xlabel(self, s):
        self.axes.set_xlabel(s)

    def set_ylabel(self, s):
        self.axes.set_ylabel(s)
