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

def generatePairs(x,y):
    for i in xrange(x):
        for j in xrange(y):
            yield i,j

class Landscape(Cell2D):
    """Simulation of opinion Landscape as 2D grid."""

    def __init__(self, n, m = None, t = 0.4, k = 6.0):
        """
        n = number of rows
        m = number of columns

        """
        self.n = n
        self.m = n if m is None else m
        self.array = np.random.random_sample(size= (self.n, self.m))
        self.t = t
        self.k = k
        # self.kernel = np.array([[-.125,-.125,-.125],
        #                         [-.125,    1,-.125],
        #                         [-.125,-.125,-.125]])
        # self.options = dict(mode='same', boundary='wrap')

    def __str__(self):
        return str(self.array)

    def interact(self,cell1,cell2, k):
        # One interaction per timestep? Random one-hot kernel to select random neighbor
        """Takes the value of two cells and adjusts them accordingly."""
        difference = math.fabs(cell1-cell2)
        if difference<=self.t: #if both cells are close enough: 
            if cell1>cell2:
                # print "Case 1"
                return (cell1-difference/k,cell2+difference/k)
            else:
                # print "Case 2"
                return (cell1+difference/k,cell2-difference/k)
        else: #cells too far apart, they radicalize
            if cell1>cell2:
                # print "Case 3"
                return (cell1+(1-cell1)/k,cell2-cell2/k) #the higher one moves toward 1, the lower one moves toward 0
            else:
                # print "Case 4"
                return (cell1-cell1/k,cell2+(1-cell2)/k)

    # def step(self,a): #a is self.array
    #     """Simulates one timestep."""
    #     a = np.pad(a,(1,1),'wrap')
    #     for x,y in generatePairs(self.n,self.m):
    #         neighbors = a[x:x+3,y:y+3]
    #         neighbors = [k for k in np.nditer(neighbors)]
    #         shuffle(neighbors)
    #         for cell in neighbors:
    #             (a[x+1,y+1],cell) = self.interact(a[x+1,y+1],cell)
    #     return self.measure_segregation(a)
        

    def step(self,a): #a is self.array
        """Simulates one timestep."""
        # for x in range(a.shape[0]):
        #     for y in range(a.shape[1]): #turn two for loops into generator! for x,y in generatePairs(): slice = array[x-1:x+2,y-1:y+2] -> make slice/compute a function
        for x,y in generatePairs(a.shape[0],a.shape[1]):
            neighbors = []
            for i in xrange(-1,2):
                for j in xrange(-1,2): #make loop an array slice!
                    neighbors.append(a[(x+i)%a.shape[0],(y+j)%a.shape[1]])
            shuffle(neighbors)
            # print neighbors
            for cell in neighbors:
                (a[x,y],cell) = self.interact(a[x,y],cell,self.k)
        return self.measure_segregation(a)



    def simulate(self, steps, measure_segregation = True):
        """Simulates a changing Landscape over (steps) timesteps."""
        if measure_segregation:
            store = [self.measure_segregation(self.array)]
            for i in xrange(steps):
                store.append(self.step(self.array))
            return store
        else:
            for i in xrange(steps):
                self.step(self.array)
            return [1 for i in xrange(steps)]

    def measure_segregation(self,a):
        """Measures how different the average cell is from its neighbors."""
        b = 0
        # for x in range(a.shape[0]):
        #     for y in range(a.shape[1]):
        for x,y in generatePairs(a.shape[0],a.shape[1]):
            temp = 0
            for i in xrange(-1,2):
                for j in xrange(-1,2): #loop guarantees O(8n^2), but there's no way around it
                    temp+=math.fabs(a[x,y]-a[(x+i)%a.shape[0],(y+j)%a.shape[1]]) #we sum the absolute difference between the center cell and each of its neighbors
            b+=(temp/8.0) #we divide the sum of differences by 8 
        return b/(self.n*self.m)

   


### Helper functions ###
def array_and_graph(n,m,t,k,steps, slice=None):
    if slice == None:
        slice = steps
    """Runs a n x m simulation with threshold t over (steps) timesteps."""
    m = n if m is None else m
    a = Landscape(n,m,t,k)

    c = Cell2DViewer(a)
    plt.subplot(2,3,1)
    c.draw_array()

    b = a.simulate(slice)
    e = Cell2DViewer(a)
    plt.subplot(2,3,2)
    e.draw_array()

    d = a.simulate(steps-slice)
    f = Cell2DViewer(a)
    plt.subplot(2,3,3)
    f.draw_array()


    plt.subplot(2,3,(4,6))
    plt.plot([k for k in range(len(b+d))],b+d,'r')
    plt.show()

array_and_graph(n=40,m=40,t=0.50,k=32.0,steps=100, slice=15)

def find_critical_t(n,m,steps,iterations,t1,t2,numT):
    result = []
    for t in np.linspace(t1,t2,num=numT):
        store = 0.0
        for i in range(iterations):
            a = Landscape(n,m,t)
            store += sum(a.simulate(steps)[-15:])/15.0
        result.append(store/iterations)
    plt.plot(np.linspace(t1,t2,num=numT),result)
    plt.show()

# find_critical_t(40,40,40,2,0.4,0.6,25)