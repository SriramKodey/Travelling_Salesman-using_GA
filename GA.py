import numpy as np
import random
from city import city
import math
from matplotlib import pyplot as plt

def euclidean(a, b):
    dist = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return dist



class GA:
    def __init__(self, pop_size, cities, mutation_rate):
        self.pop_size = pop_size
        self.cities = cities

        self.distance_table = np.empty([50, 50])
        self.mutation_rate = mutation_rate
        self.curr_pop = np.empty([self.pop_size, 50])
        self.fitness = []
        self.best_parents = []
        self.crossover_threshold = 32

    def generate_distance_table(self):
        for i in range(50):
            for j in range(50):
                if i == j:
                    self.distance_table[i][j] = 0

                else:
                    self.distance_table[i][j] = euclidean(self.cities[i], self.cities[j])


    def generate_random(self):
        nums = np.arange(50)

        for i in range(self.pop_size):
            np.random.shuffle(nums)
            self.curr_pop[i] = nums

    def get_fitness(self, arr):
        dist = 0
        for j in range(49):
            dist += self.distance_table[int(arr[j])][int(arr[j+1])]

        dist += self.distance_table[int(arr[0])][int(arr[49])]

        return dist


    def gen_fitness_pop(self):
        self.fitness = []
        for i in range(self.pop_size):
            fitness = self.get_fitness(self.curr_pop[i])
            self.fitness.append(fitness)

    def selection(self):
        n = self.crossover_threshold
        arr = []
        i = 0
        temp = [True, False]

        while i < n:
            tmp = random.randint(0, n-1)
            prob = [1 - self.fitness[tmp], self.fitness[tmp]]
            choice = np.random.choice(temp, p = prob)

            if choice:
                arr.append(self.curr_pop[tmp])
                np.delete(self.curr_pop, tmp, 0)
                i += 1

        return arr

    def normalization(self):
        n = len(self.fitness)
        n_sum = sum(self.fitness)

        for i in range(n):
            self.fitness[i] = self.fitness[i] / n_sum

    def crossover(self):
        arr = self.selection()
        n = len(arr)
        
        kids = []
        for i in range(n-1):
            parent_a = arr[i]
            parent_b = arr[i+1]
            i = i+1
            temp = parent_a

            crossover_point = random.randint(1, 49)

            parent_a[crossover_point:] = parent_b[crossover_point:]
            parent_b[crossover_point:] = temp[crossover_point:]

            kids.append(parent_a)
            kids.append(parent_b)
        
        sum_parents_fitness = 0
        sum_kids_fitness = 0
        for i in range(n):
            sum_parents_fitness += self.get_fitness(arr[i])
            sum_kids_fitness += self.get_fitness(kids[i])

        if sum_kids_fitness>sum_parents_fitness:
            np.concatenate((self.curr_pop, np.array(kids)))

        else:
            np.concatenate((self.curr_pop, np.array(arr)))

    def mutate(self):
        for i in range(self.pop_size):
            temp = [True, False]
            prob = [self.mutation_rate, 1 - self.mutation_rate]

            for j in range(50):
                choice = np.random.choice(2, 1, p = prob)

                if choice:
                    n1 = random.randint(1, 49)
                    n2 = random.randint(1, 49)

                    if n1 != n2:
                        temp = self.curr_pop[i][n1]
                        self.curr_pop[i][n1] = self.curr_pop[i][n2]
                        self.curr_pop[i][n2] = temp

                    else:
                        n1 = j




def solve(cities):
    num_iters = 1000
    
    genAlg = GA(500, cities, 0.08)
    genAlg.generate_distance_table()
    genAlg.generate_random()
    min_fitness_table = []
    fitness_table = []

    for i in range(num_iters):
        genAlg.gen_fitness_pop()
        fitness_table.append(sum(genAlg.fitness)/500)
        min_fitness_table.append(min(genAlg.fitness))
        if i == 0:
            print(sum(genAlg.fitness))

        genAlg.normalization()
        genAlg.crossover()
        genAlg.mutate()
    
    genAlg.gen_fitness_pop()
    print(sum(genAlg.fitness))

    plt.plot(fitness_table)
    plt.show()

    plt.clf()

    plt.plot(min_fitness_table)
    plt.show()

if __name__ == "__main__":
    arr = [1, 10, 3 ,4, 5 ,6]
    plt.plot(arr)
    plt.show()
    pass