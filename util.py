import random


class City(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = float(x)
        self.y = float(y)

    def calculate_distance(self, destination):
        return ((self.x - destination.x) ** 2 + (self.y - destination.y) ** 2) ** 0.5


class Route:
    def __init__(self, list_of_cities):
        self.route = sorted(list_of_cities, key=lambda args: random.random())
        self.length = 0.0
        self.calculate_length()

    def calculate_length(self):
        self.length = 0.0
        # for every city in its route attribute:
        for city in self.route:
            # points to next city
            next_city = self.route[self.route.index(city) - len(self.route) + 1]
            # gets distance between the current city and the next
            dist_to_next = city.calculate_distance(next_city)
            # adds this length to its length attr.
            self.length += dist_to_next


class Routes:
    def __init__(self, size, initialise, list_of_cities):
        self.route_population = []
        self.size = size
        # If True initialize population:
        if initialise:
            for x in range(0, size):
                new_route = Route(list_of_cities)
                self.route_population.append(new_route)
            self.get_fittest()

    def get_fittest(self):
        # sorts the list
        sorted_list = sorted(self.route_population, key=lambda x: x.length, reverse=False)
        try:
            self.fittest = sorted_list[0]
        except:
            return 0
        return self.fittest


class Graph(object):
    def __init__(self, cost_matrix: list, rank: int):
        self.matrix = cost_matrix
        self.rank = rank
        self.pheromone = [[1 / (rank * rank) for j in range(rank)] for i in range(rank)]
