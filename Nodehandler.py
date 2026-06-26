import random as rnd
import math

MUTATION_PROBABILITY = 0.1
MATING_POOL_SIZE = 10

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
            total += euclidean_distance(current.location, next_stop.location)

        self.fitness = 1 / total if total > 0 else float('inf')

    def mutate(self):
        if rnd.random() < MUTATION_PROBABILITY:
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

    #Fitness-Funktion auf Individuen anwenden
    def evaluate_nodes(self):
        for node in self.nodes:
            node.calc_fitness()

    #Selektion
    def create_mating_pool(self):
        node_weights = calc_list_weights(self.nodes)
        self.mating_pool = rnd.choices(self.nodes, weights=node_weights, k=MATING_POOL_SIZE)
        self.mating_pool.sort(key=lambda x: x.fitness, reverse=True)
        self.best_fitness = self.mating_pool[0]

    #Mutation
    def mutate_pop(self):
        for node in self.nodes:
            node.mutate()

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calc_list_weights(list):
    total_fitness = sum([node.fitness for node in list])
    return [node.fitness / total_fitness for node in list]

#Crossover
def gen_new_population(population):
    new_nodes = []
    for i in range(len(population.nodes)):
        #2 verschiedene Touren auswählen
        mating_pool_weights = calc_list_weights(population.mating_pool)
        node1 = rnd.choices(population.mating_pool, weights=mating_pool_weights, k=1)[0]
        node2 = rnd.choices(population.mating_pool, weights=mating_pool_weights, k=1)[0]
        while node1.id == node2.id:
            node2 = rnd.choices(population.mating_pool, weights=mating_pool_weights, k=1)[0]
        tour1 = node1.tour
        tour2 = node2.tour
        new_tour = gen_mixed_tour(tour1, tour2)
        new_nodes.append(Node(i, new_tour))
    return Population(new_nodes)

def gen_mixed_tour(tour1, tour2):
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
    return output