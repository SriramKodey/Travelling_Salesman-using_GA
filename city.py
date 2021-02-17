#/*
# * @Author: SriramKodey 
# * @Date: 2021-02-14 18:49:22 
# * @Last Modified by:   SriramKodey 
# * @Last Modified time: 2021-02-14 18:49:22 
# */


import numpy as np
from matplotlib import pyplot as plt
import random

class city:
    ''' City class, with x and y points'''
    def __init__(self, num):
        y = int(num/101)
        x = int(num%101)

        self.x = x
        self.y = y

def plot(cities):
    n = len(cities)
    x = []
    y = []
    for i in range(n):
        x.append(cities[i].x)
        y.append(cities[i].y)

    a = n%7
    b = int(n/7)
    
    clrs = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    colors = random.sample(clrs, a)
    for i in range(b):
        colors = colors + random.sample(clrs, 7)

    plt.scatter(x, y, c = colors)
    plt.show()

def plot_path(cities):
    n = len(cities)
    x = []
    y = []
    for i in range(n):
        x.append(cities[i].x)
        y.append(cities[i].y)

    x.append(x[0])
    y.append(y[0])

    plt.plot(x, y, 'r+')
    plt.plot(x, y)
    plt.show()



if __name__ == "__main__":
    hyd = city(10200)
    print(hyd.x, hyd.y)