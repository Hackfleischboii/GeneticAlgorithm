import random as rnd
import City

MUTATION_PROBABILITY = 0.1

population_size = 0

class Node:
    def __init__(self, id, tour):
        self.id = id
        self.tour = tour
        self.fitness = None

    def __repr__(self):
        return "Node " + str(self.id) + ": with fitness: " + str(self.fitness)

    def gen_rand_tour(self, cities):
        cities = cities.copy()
        output = []
        while cities:
            rand_index = rnd.randint(0, len(cities) - 1)
            city = cities[rand_index]
            output.append(city)
            cities.remove(city)

        self.tour = output

    def calc_fitness(self):
        total = 0
        for i in range(len(self.tour)):
            current = self.tour[i]
            next_stop = self.tour[(i + 1) % len(self.tour)]  # Wieder zum Start
            total += euclidean_distance_squared(current.location, next_stop.location)

        self.fitness = 1 / total if total > 0 else float('inf')

    def mutate(self):
        if rnd.randint(0, int((1 / MUTATION_PROBABILITY) + 1)) == 0:
            output = self.tour.copy()
            i = rnd.randint(0, len(output) - 1)
            j = rnd.randint(0, len(output) - 1)
            output[i], output[j] = output[j], output[i]
            self.tour = output


class Population:
    def __init__(self, nodes):
        self.nodes = nodes
        self.mating_pool = None
        self.best_fitness = -float('inf')

    def __repr__(self):
        output = ""
        for node in self.nodes:
            output += str(node)
            output += "\n"
        return output

    def generate_tours(self, cities):
        for node in self.nodes:
            node.gen_rand_tour(cities)

    def evaluate_nodes(self):
        for node in self.nodes:
            node.calc_fitness()

    def select_best(self):
        num_best = 2

        sorted_nodes = sorted(self.nodes, key=lambda x: x.fitness, reverse=True)

        self.best_fitness = sorted_nodes[0]
        self.mating_pool = sorted_nodes[:num_best]

    def mutate_pop(self):
        for node in self.nodes:
            node.mutate()

def euclidean_distance_squared(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def gen_new_population(population):
    tour1 = population.mating_pool[0].tour
    tour2 = population.mating_pool[1].tour

    start_index = 0
    cur_index = start_index
    output = []
    visited = []

    while cur_index not in visited:
        visited.append(cur_index)
        tour1_city = tour1[cur_index]
        cur_index = tour2.index(tour1_city)

    for i in range(len(tour1)):
        if i in visited:
            output.append(tour1[i])
        else:
            output.append(tour2[i])

    return Population([Node(i, output) for i in range(len(population.nodes))])
