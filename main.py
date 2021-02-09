import numpy as np
import random
from city import city
from matplotlib import pyplot as plt
from GA import solve

def make_cities():
    '''Creates 10201 umbers from which 50 are randomly picked out'''
    nums = range(10201)
    points = random.sample(nums, 50)

    cities = []

    for i in points:
        cities.append(city(i))

    return cities

def plot(cities):
    x = []
    y = []
    for i in range(50):
        x.append(cities[i].x)
        y.append(cities[i].y)

    plt.plot(x, y, 'bo')
    plt.show()

def geneticAlgo(cities):    
    solve(cities)

if __name__ == "__main__":
    cities = make_cities()
    plot(cities)

    geneticAlgo(cities)
