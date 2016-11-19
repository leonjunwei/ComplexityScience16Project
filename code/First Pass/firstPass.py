import math

import warnings
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('animation', html='html5')

from Cell2D import Cell2D, Cell2DViewer

class landScape(Cell2D):
    """Simulation of opinion landscape as 2D grid."""
    def __init__(self, n, m = None, t = 0.4):
        """
        n = number of rows
        m = number of columns

        """
        self.n = n
        self.m = n if m is None else m
        self.array = np.random.random_sample(size= (self.n, self.m))
        self.t = t
    def __str__(self):
        return str(self.array)
    def interact(self,cell1,cell2):
        difference = math.fabs(cell1-cell2)
        if 0.0<=difference<=0.1: #if both cells are close enough: 
            if cell1>cell2:
                # print "Case 1"
                return (cell1-difference/2.0,cell2+difference/2.0)
            else:
                # print "Case 2"
                return (cell1+difference/2.0,cell2-difference/2.0)
        else: #cells too far apart, they radicalize
            if cell1>cell2:
                # print "Case 3"
                return (cell1+(1-cell1)/3.0,cell2/3.0) #the higher one moves toward 1, the lower one moves toward 0
            else:
                # print "Case 4"
                return (cell1/3.0,cell2+(1-cell2)/3.0)

    def step(self):
        a = self.array
        for x in range(a.shape[0]):
            for y in range(a.shape[1]):
                for i in range(-1,2):
                    for j in range(-1,2): #loop guarantees O(8n^2), but there's no way around it
                        (a[x,y],a[(x+i)%a.shape[0],(y+j)%a.shape[1]]) = self.interact(a[x,y],a[(x+i)%a.shape[0],(y+j)%a.shape[1]])
    def simulate(self, steps):
        for i in range(steps):
            self.step()




a = landScape(75)
a.simulate(200)
print a
b = Cell2DViewer(a)
b.draw_array()
plt.show()
