import math
from scipy.signal import correlate2d
import warnings
import numpy as np
import matplotlib.pyplot as plt

from random import shuffle

from matplotlib import rc
rc('animation', html='html5')

from Cell2D import Cell2D, Cell2DViewer

"""
Using Allen's Cell2D and Cell2DViewer classes to simulate an opinion Landscape
"""

class Landscape(Cell2D):
    """Simulation of opinion Landscape as 2D grid."""

    def __init__(self, n, m = None, t = 0.4):
        """
        n = number of rows
        m = number of columns

        """
        self.n = n
        self.m = n if m is None else m
        self.array = np.random.random_sample(size= (self.n, self.m))
        self.t = t
        # self.kernel = np.array([[-.125,-.125,-.125],
        #                         [-.125,    1,-.125],
        #                         [-.125,-.125,-.125]])
        # self.options = dict(mode='same', boundary='wrap')

    def __str__(self):
        return str(self.array)

    def interact(self,cell1,cell2):
        """Takes the value of two cells and adjusts them accordingly."""
        difference = math.fabs(cell1-cell2)
        if difference<=self.t: #if both cells are close enough: 
            if cell1>cell2:
                # print "Case 1"
                return (cell1-difference/2.0,cell2+difference/2.0)
            else:
                # print "Case 2"
                return (cell1+difference/2.0,cell2-difference/2.0)
        else: #cells too far apart, they radicalize
            if cell1>cell2:
                # print "Case 3"
                return (cell1+(1-cell1)/2.0,cell2/2.0) #the higher one moves toward 1, the lower one moves toward 0
            else:
                # print "Case 4"
                return (cell1/2.0,cell2+(1-cell2)/2.0)

    def step(self,a): #a is self.array
        """Simulates one timestep."""
        for x in range(a.shape[0]):
            for y in range(a.shape[1]):
                neighbors = []
                for i in range(-1,2):
                    for j in range(-1,2): #loop guarantees O(8n^2), but there's no way around it
                        neighbors.append(a[(x+i)%a.shape[0],(y+j)%a.shape[1]])
                shuffle(neighbors)
                # print neighbors
                for cell in neighbors:
                    (a[x,y],cell) = self.interact(a[x,y],cell)

        

    def simulate(self, steps, measure_segregation = True):
        """Simulates a changing Landscape over (steps) timesteps."""
        if measure_segregation:
            store = [self.measure_segregation(self.array)]
            for i in range(steps):
                store.append(self.step(self.array))
            return store
        else:
            for i in range(steps):
                self.step(self.array)
            return [1 for i in range(steps)]