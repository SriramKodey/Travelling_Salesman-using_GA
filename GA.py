#/*
# * @Author: SriramKodey 
# * @Date: 2021-02-14 18:49:03 
# * @Last Modified by:   SriramKodey 
# * @Last Modified time: 2021-02-14 18:49:03 
# */


import numpy as np
import random
from city import city
import city
import math
from matplotlib import pyplot as plt

def euclidean(a, b):
    dist = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return dist

def manhattan(a, b):
    dist = abs(a.x - b.x) + abs(a.y + b.y)
    return dist

class GA:
    def __init__(self, pop_size, cities, crossover_threshold, mutation_rate):
        self.pop_size = pop_size
        self.cities = cities
        self.chromo_size = len(cities)

        self.best_solution = []
        self.best_solution_fitness = 0

        self.distance_table = np.empty([self.chromo_size, self.chromo_size], dtype = np.uint8)
        self.mutation_rate = mutation_rate
        self.curr_pop = np.empty([self.pop_size, (self.chromo_size+1)])
        self.fitness = []
        self.best_parents = []
        self.crossover_threshold = crossover_threshold

    def addtopop(self, arr):
        self.curr_pop = np.concatenate((self.curr_pop, arr))

    def replace_pop(self, arr):
        self.curr_pop = arr

    def generate_distance_table(self):
        for i in range(self.chromo_size):
            for j in range(self.chromo_size):
                if i == j:
                    self.distance_table[i][j] = 0

                else:
                    self.distance_table[i][j] = euclidean(self.cities[i], self.cities[j])

    def generate_manhattan_distance_table(self):
        for i in range(self.chromo_size):
            for j in range(self.chromo_size):
                if i == j:
                    self.distance_table[i][j] = 0

                else:
                    self.distance_table[i][j] = manhattan(self.cities[i], self.cities[j])


    def generate_random(self):
        nums = np.arange(self.chromo_size)

        for i in range(self.pop_size):
            np.random.shuffle(nums)
            self.curr_pop[i][0:self.chromo_size] = nums

    def get_fitness(self, arr):
        dist = 0
        for j in range(self.chromo_size-1):
            dist += self.distance_table[int(arr[j])][int(arr[j+1])]

        dist += self.distance_table[int(arr[0])][int(arr[self.chromo_size-1])]
        
        return dist


    def gen_fitness_pop(self):
        self.fitness = []
        for i in range(self.pop_size):
            fitness = self.get_fitness(self.curr_pop[i])
            self.fitness.append(fitness)
            self.curr_pop[i][self.chromo_size] = fitness

    def selection(self):
        ''' Using the Roulette Wheel system'''
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

    
    def selection_ranking(self):
        ''' Using the ranking system'''
        n = self.crossover_threshold
        arr = []
        i = 0
        temp = [True, False]
        flag = True

        self.curr_pop = self.curr_pop[self.curr_pop[:, self.chromo_size].argsort()]
        
        while flag:
            prob = [1 - (i/self.pop_size), (i/self.pop_size)]
            choice = np.random.choice(temp, p = prob)

            if choice:
                arr.append(self.curr_pop[i])
                if len(arr) == n:
                    flag = False
            
            i = i+1
            if i == self.pop_size:
                i = 0

        return arr

    def normalization(self):
        n = len(self.fitness)
        n_sum = sum(self.fitness)

        for i in range(n):
            self.fitness[i] = self.fitness[i] / n_sum

            
    def pmx_operation(self, parent_a, parent_b, crossover_point_1, crossover_point_2):
        kid_a = parent_a
        kid_b = parent_b

        kid_a[crossover_point_1 : crossover_point_2] = parent_b[crossover_point_1 : crossover_point_2]
        kid_b[crossover_point_1 : crossover_point_2] = parent_a[crossover_point_1 : crossover_point_2]

        string_b = parent_b[crossover_point_1 : crossover_point_2]
        string_a = parent_a[crossover_point_1 : crossover_point_2]
        
        relationsWithDupes = []
        for i in range(len(string_a)):
            relationsWithDupes.append([string_b[i], string_a[i]])

        relations = []
        for pair in relationsWithDupes:

            for i in range(len(relationsWithDupes)):
                if pair[0] in relationsWithDupes[i] or pair[1] in relationsWithDupes[i]:
                    if pair != relationsWithDupes[i]:
                        if pair[0] == relationsWithDupes[i][1]:
                            pair[0] = relationsWithDupes[i][0]

                        else:
                            pair[1] = relationsWithDupes[i][1]

            if pair not in relations and pair[::-1] not in relations:
                relations.append(pair)

        for i in kid_a[:crossover_point_1]:
            for x in relations:
                if i == x[0]:
                    i = x[1]

        for i in kid_a[crossover_point_2:]:
            for x in relations:
                if i == x[0]:
                    i = x[1]

        for i in kid_b[:crossover_point_1]:
            for x in relations:
                if i == x[1]:
                    i = x[0]

        for i in kid_b[crossover_point_2:]:
            for x in relations:
                if i == x[1]:
                    i = x[0]

        return kid_a, kid_b


    def order_operation(self, parent_a, parent_b, crossover_point_1, crossover_point_2):
        nums = range(self.chromo_size)

        kid_a = random.sample(nums, self.chromo_size)
        kid_b = random.sample(nums, self.chromo_size)

        kid_a[crossover_point_1 : crossover_point_2] = parent_b[crossover_point_1 : crossover_point_2]
        kid_b[crossover_point_1 : crossover_point_2] = parent_a[crossover_point_1 : crossover_point_2]

        string_a = parent_b[crossover_point_1 : crossover_point_2]
        string_b = parent_a[crossover_point_1 : crossover_point_2]

        t_1 = crossover_point_2
        t_2 = crossover_point_2

        for i in range(self.chromo_size):
            if (t_1 >= self.chromo_size):
                t_1 = t_1 % self.chromo_size

            if (parent_a[i] in string_a):
                pass
            else:
                kid_a[t_1] = parent_a[i]
                t_1 = t_1 + 1


            if (t_2 >= self.chromo_size):
                t_2 = t_2 % self.chromo_size

            if (parent_b[i] in string_b):
                pass
            else:
                kid_b[t_2] = parent_b[i]
                t_2 = t_2 + 1

        kid_a.append(0)
        kid_b.append(0)

        return kid_a, kid_b
        



    def crossover_new(self):
        arr = self.selection_ranking()
        n = len(arr)

        kids = []
        for i in range(n-1):
            parent_a = arr[i]
            parent_b = arr[i+1]
            #i = i+1
            temp = parent_a

            crossover_point_1 = random.randint(1, self.chromo_size-1)
            crossover_point_2 = crossover_point_1 + random.randint(1, self.chromo_size - crossover_point_1)
            
            kid_a, kid_b = self.order_operation(parent_a, parent_b, crossover_point_1, crossover_point_2)

            kids.append(kid_a)
            kids.append(kid_b)
        
        for i in range(n):
            kids[i][self.chromo_size] = self.get_fitness(kids[i])

        kids = np.array(kids)
        self.addtopop(kids)
        self.curr_pop = self.curr_pop[self.curr_pop[:, self.chromo_size].argsort()]
        self.replace_pop(self.curr_pop[0:self.pop_size])


    def mutate(self):
        for i in range(self.pop_size):
            temp = [True, False]
            prob = [1 - self.mutation_rate, self.mutation_rate]

            for j in range(50):
                choice = np.random.choice(2, 1, p = prob)

                if choice:
                    n1 = random.randint(1, self.chromo_size-1)
                    n2 = random.randint(1, self.chromo_size-1)

                    if n1 != n2:
                        temp = self.curr_pop[i][n1]
                        self.curr_pop[i][n1] = self.curr_pop[i][n2]
                        self.curr_pop[i][n2] = temp

                    else:
                        n1 = j




def solve(cities):
    np.set_printoptions(suppress = True)
    num_iters = 500
    pop_size = 150
    crossover_threshold = int(0.6 * pop_size)
    mutation_rate = 0.001 # = 1/50
    
    genAlg = GA(pop_size, cities, crossover_threshold, mutation_rate)
    genAlg.generate_distance_table()
    genAlg.generate_random()
    min_fitness_table = []
    fitness_table = []
    genAlg.gen_fitness_pop()
    print(sum(genAlg.fitness))
    genAlg.best_solution_fitness = min(genAlg.fitness)

    k = 0
    
    for i in range(num_iters):
        genAlg.gen_fitness_pop()

        if k>50:
            if genAlg.chromo_size <= 20:
                break

            else:
                genAlg.mutation_rate = 0.005

        k += 1

        fitness_table.append(sum(genAlg.fitness)/genAlg.pop_size)
        min_fitness_table.append(min(genAlg.fitness))
        if min(genAlg.fitness) < genAlg.best_solution_fitness:
            k = 0
            genAlg.best_solution_fitness = min(genAlg.fitness)
            t = genAlg.fitness.index(min(genAlg.fitness))
            genAlg.best_solution = genAlg.curr_pop[t]

        #genAlg.normalization()
        genAlg.crossover_new()
        if i != num_iters:
            genAlg.mutate()

        print("Iteration ", i, " Completed", " Current best fitness: = ", min_fitness_table[i])

    genAlg.gen_fitness_pop()

    genAlg.gen_fitness_pop()
    print(sum(genAlg.fitness))

    plt.plot(fitness_table)
    plt.show()

    plt.clf()
    plt.plot(min_fitness_table, 'r')
    plt.show()

    final_cities = []
    for i in range(genAlg.chromo_size):
        final_cities.append(genAlg.cities[int(genAlg.best_solution[i])])

    print("The best solution is: ", np.array(genAlg.best_solution))
    print("Population size = ", pop_size, " Crossover rate = ", crossover_threshold, "/", pop_size, " and Mutation rate = ", mutation_rate) 
    city.plot_path(final_cities)

if __name__ == "__main__":
    arr = [1, 10, 3 , 4, 5 ,6]
    plt.plot(arr)
    plt.show()
    pass