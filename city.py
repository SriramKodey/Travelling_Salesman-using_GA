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
    x = []
    y = []
    for i in range(50):
        x.append(cities[i].x)
        y.append(cities[i].y)

    colors = ['b']
    clrs = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(7):
        colors = colors + random.sample(clrs, 7)

    plt.scatter(x, y, c = colors)
    plt.show()

def plot_path(cities):
    x = []
    y = []
    for i in range(50):
        x.append(cities[i].x)
        y.append(cities[i].y)

    x.append(x[0])
    y.append(y[0])

    plt.plot(x, y, 'r+')
    plt.plot(x, y)
    plt.show()


def plot_path_manhattanI(cities):
    x = []
    y = []
    for i in range(50):
        x.append(cities[i].x)
        y.append(cities[i].y)

    plt.plot(x, y, 'r+')



if __name__ == "__main__":
    hyd = city(10200)
    print(hyd.x, hyd.y)