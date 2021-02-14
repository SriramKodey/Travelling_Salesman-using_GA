import numpy as np
import random
from city import city
from city import plot
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


def geneticAlgo(cities):    
    solve(cities)

if __name__ == "__main__":
    cities = make_cities()
    plot(cities)

    geneticAlgo(cities)
