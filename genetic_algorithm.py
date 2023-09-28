import util
import random


class GA(object):
    def __init__(self, list_of_cities, mutation_probability, tournament_size, elitism):
        self.list_of_cities = list_of_cities
        self.mutation_prob = mutation_probability
        self.tournament_size = tournament_size
        self.elitism = elitism

    def crossover(self, parent1, parent2):
        # create child
        child_route = util.Route(self.list_of_cities)

        # set all of child's route to null
        for x in range(0, len(child_route.route)):
            child_route.route[x] = None

        # Two random integer indices of the parent1:
        start_pos = random.randint(0, len(parent1.route))
        end_pos = random.randint(0, len(parent1.route))

        # if the start position is before the end:
        if start_pos < end_pos:
            # do it in the start-->end order
            for x in range(start_pos, end_pos):
                child_route.route[x] = parent1.route[x]  # set the values to each other
        # if the start position is after the end:
        elif start_pos > end_pos:
            # do it in the end-->start order
            for i in range(end_pos, start_pos):
                child_route.route[i] = parent1.route[i]  # set the values to each other

        # Cycles through the parent2. And fills in the child_route
        # cycles through length of parent2:
        for i in range(len(parent2.route)):
            # if parent2 has a city that the child doesn't have yet:
            if not parent2.route[i] in child_route.route:
                # it puts it in the first 'None' spot and breaks out of the loop.
                for x in range(len(child_route.route)):
                    if child_route.route[x] is None:
                        child_route.route[x] = parent2.route[i]
                        break
        # repeated until all the cities are in the child route

        # returns the child route (of type Route())
        child_route.calculate_length()
        return child_route

    def mutate(self, route_to_mut):
        # Swaps two random indexes in route_to_mut.route.
        if random.random() < self.mutation_prob:

            # two random indices:
            mut_pos1 = random.randint(0, len(route_to_mut.route) - 1)
            mut_pos2 = random.randint(0, len(route_to_mut.route) - 1)

            # if they're the same, skip to the chase
            if mut_pos1 == mut_pos2:
                return route_to_mut

            # Otherwise swap them:
            city1 = route_to_mut.route[mut_pos1]
            city2 = route_to_mut.route[mut_pos2]

            route_to_mut.route[mut_pos2] = city1
            route_to_mut.route[mut_pos1] = city2

        # Recalculate the length of the route (updates it's .length)
        route_to_mut.calculate_length()

        return route_to_mut

    def tournament_select(self, population):
        # New smaller population (not initialised)
        tournament_pop = util.Routes(size=self.tournament_size, initialise=False, list_of_cities=self.list_of_cities)

        # fills it with random individuals (can choose same twice)
        for i in range(self.tournament_size - 1):
            tournament_pop.route_population.append(random.choice(population.route_population))

        # returns the fittest:
        return tournament_pop.get_fittest()

    def evolve_population(self, init_pop):
        # makes a new population:
        descendant_pop = util.Routes(size=init_pop.size, initialise=True, list_of_cities=self.list_of_cities)

        # Elitism offset (amount of Routes() carried over to new population)
        elitism_offset = 0

        # if we have elitism, set the first of the new population to the fittest of the old
        if self.elitism:
            descendant_pop.route_population[0] = init_pop.fittest
            elitism_offset = 1

        # Goes through the new population and fills it with the child of two tournament winners from the previous population
        for x in range(elitism_offset, descendant_pop.size):
            # two parents:
            tournament_parent1 = self.tournament_select(init_pop)
            tournament_parent2 = self.tournament_select(init_pop)

            # A child:
            tournament_child = self.crossover(tournament_parent1, tournament_parent2)

            # Fill the population up with children
            descendant_pop.route_population[x] = tournament_child

        # Mutates all the routes (mutation with happen with a prob p = k_mut_prob)
        for route in descendant_pop.route_population:
            if random.random() < self.mutation_prob:
                self.mutate(route)

        # Update the fittest route:
        descendant_pop.get_fittest()

        return descendant_pop