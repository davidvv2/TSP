import glob
import re
import time
import copy
import math
import util
import genetic_algorithm as ga


MAX_GENERATIONS = 100
mutation_prob = 0.5
elitism = True
list_of_cities = []


path = "./TSP"
tsp_files = glob.glob(path + "/*.tsp")
pattern = re.compile("[0-9]+\.?[0-9]*")
counter = 1

for file in tsp_files:
    for line in open(file, 'rt', encoding='utf-8'):
        data = re.split(" ", line.strip())
        data = list(filter(pattern.match, data))

        if len(data) != 3:
            continue

        city = util.City(data[0], data[1], data[2])
        list_of_cities.append(city)
        pop_size = len(list_of_cities)

    # tournament size is set to 10% of the number of cities in route
    tournament_size = math.floor(pop_size / 10)
    # takes the start time of the run:
    start_time = time.time()

    the_population = util.Routes(pop_size, True, list_of_cities)
    initial_length = the_population.fittest.length
    best_route = util.Route(list_of_cities)
    generation = 0

    while generation <= MAX_GENERATIONS:
        # Evolves the population:
        the_population = ga.GA(list_of_cities, mutation_prob, tournament_size, elitism).evolve_population(the_population, )
        if the_population.fittest.length < best_route.length:
            # set the route
            best_route = copy.deepcopy(the_population.fittest)

        generation += 1

    end_time = time.time()

    f = open("Results/saved" + str(counter) + ".txt", 'w', encoding='utf-8')
    f.write("Elapsed time was {0:.1f} seconds.".format(time.time() - start_time) + '\n')
    f.write('Initial best distance: {0:.2f}'.format(initial_length) + '\n')
    f.write('Final best distance:   {0:.2f}'.format(best_route.length) + '\n')
    f.write('The best route went via:   {}' .format([x.name for x in best_route.route]) + '\n\n')

    counter += 1

