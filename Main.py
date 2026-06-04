from City import City
from Nodehandler import *

QUIT_VALUE = 0.01

def main():
    cities = initialise_cities(10)
    initial_pop = initialise_population(20)
    initial_pop.generate_tours(cities)

    initial_pop.evaluate_nodes()
    initial_pop.select_best()

    last_pop_best = initial_pop.best_fitness
    cur_pop = None
    index = 0

    while cur_pop is None or (cur_pop.best_fitness - last_pop_best) > QUIT_VALUE or index >= 10:
        if cur_pop is not None:
            last_pop_best = cur_pop.best_fitness
        
        cur_pop = gen_new_population(cur_pop)
        cur_pop.mutate_pop()

        cur_pop.evaluate_nodes()
        cur_pop.select_best()
        index += 1
        print("Aktuelle Generation: ")
        print(cur_pop)
        print(cur_pop.best_fitness)

    print("Die Anzahl der Generationen: ", str(index))

def initialise_cities(num_cities):
    cities = []
    for i in range(num_cities):
        cities.append(City(i))
    return cities

def initialise_population(start_pop):
    nodes = []
    for i in range(start_pop):
        nodes.append(Node(i, []))
    return Population(nodes)

main()