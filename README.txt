Please Run the main.py file, with both GA.py and city.py placed in the same folder as main.py.

	1) solve() in GA.py has the population_size, Crossover_number and mutation_rate defined.
	   These can be changed to make the solution more accurate.
	   Default values are pop_size = 150, crossover = 80/150, mutation_rate = 0.001 and 500 iters.

	2) Increase pop_size and iters for perfect solution. pop_size = 2000, crossover = 900
           and iters = 500, with mutation turned off gave me the best results.

	3) To use Manhattan distance, go to solve() in GA.py file and change 
	   genAlg.generate_distance_table() to genAlg.generate_manhattan_disance_table().

Thank You
