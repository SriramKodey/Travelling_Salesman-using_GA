#/*
# * @Author: SriramKodey 
# * @Date: 2021-02-14 18:45:10 
# * @Last Modified by:   SriramKodey 
# * @Last Modified time: 2021-02-14 18:45:10 
# */


import numpy as np
import random
from city import city
from city import plot
from matplotlib import pyplot as plt
from GA import solve

def make_cities(n):
    '''Creates 10201 umbers from which 50 are randomly picked out'''
    nums = range(10201)
    points = random.sample(nums, n)

    cities = []

    for i in points:
        cities.append(city(i))

    return cities


def geneticAlgo(cities):  
    solve(cities)

if __name__ == "__main__":
    flag = True
    i = 0
    while flag:
        n = input("Enter the Number of Cities: ")
        n = int(n)
        if n<10:
            print("Why do you need code for that? Enter something greater than 10!")

        elif n>100 and n<500:
            ans = input("It will take a long time. Do you wish to continue y/n? : ")
            if ans == 'y':
                flag = False

        elif n>=500:
            print("Enter less than 500 cities, PLEASE!")
            i += 1
            if i>10:
                flag = False

        else:
            flag = False


    cities = make_cities(n)
    plot(cities)
    geneticAlgo(cities)
