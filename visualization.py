import typing as t
from datetime import datetime
from pathlib import Path

import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.text import Annotation
from matplotlib.text import Annotation

from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D

from metrics import Metrics

import PySide6.QtCore

matplotlib.use('QtAgg')


class Annotation3D(Annotation):

    def __init__(self, text, xyz, *args, **kwargs):
        super().__init__(text, xy=(0, 0), *args, **kwargs)
        self._xyz = xyz

    def draw(self, renderer):
        x2, y2, z2 = proj_transform(*self._xyz, self.axes.M)
        self.xy = (x2, y2)
        super().draw(renderer)


def _annotate3D(ax, text, xyz, *args, **kwargs):
    '''Add anotation `text` to an `Axes3d` instance.'''

    annotation = Annotation3D(text, xyz, *args, **kwargs)
    ax.add_artist(annotation)

setattr(Axes3D, 'annotate3D', _annotate3D)


class Visualize():
    def __init__(self, function: t.Callable, mutation: t.Callable):
        self.test_func = function
        self.test_function_name = function.__name__
        self.mutation_strategy_name = mutation.__name__
        self.fig_path = Path('runs')

    def _construct_test_plot(self):
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})

        # Make data.
        X_arr = np.arange(-40, 40, 1)
        Y_arr = np.arange(-40, 40, 1)
        X, Y = np.meshgrid(X_arr, Y_arr)
        Z = np.ndarray(shape=(len(X_arr), len(Y_arr)))
        for ix, x in enumerate(X_arr):
            for iy, y in enumerate(Y_arr):
                Z[ix][iy] = self.test_func([x,y])
        # Plot the surface.
        surf = self.ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                            linewidth=0, antialiased=False)
        # Customize the z axis.
        self.ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        self.ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        self.fig.colorbar(surf, shrink=0.5, aspect=5)

    def plot_history(self, values):
        X = np.arange(0, len(values), 1)
        plt.plot(X, values)
        plt.title('Values per iteration')
        plt.xlabel('Iteration')
        plt.ylabel('Best value')

        save_to = self.fig_path.joinpath(self.test_function_name)
        
        if not save_to.exists():
            save_to.mkdir(parents=True)
        timestamp = datetime.now().strftime(r'%y%m%d%H%M%S')

        plt.savefig(save_to.joinpath(timestamp+'_'+self.mutation_strategy_name+'.jpg'))
        

    def show_best(self, coords):
        self._construct_test_plot()
        self.ax.annotate3D('Calc. Min', coords,
              xytext=(-30, -30),
              textcoords='offset points',
              arrowprops=dict(ec='black', fc='white', shrink=1.5))
        plt.show()
