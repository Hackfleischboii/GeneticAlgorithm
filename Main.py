from City import City
from Display import Display
from Nodehandler import *

QUIT_VALUE = 0.00000000000001
MAX_ITERATIONS = 1000
NUM_CITIES = 10
NUM_PER_POP = 20

def main():
    cities = initialise_cities(NUM_CITIES)
    initial_pop = initialise_population(NUM_PER_POP)
    initial_pop.generate_tours(cities)

    initial_pop.evaluate_nodes()
    initial_pop.select_best()

    display = Display(initial_pop.mating_pool[0], 0)
    display.plot()
    

    for node in initial_pop.nodes:
        print(node)
    print("==================================")
    for node in initial_pop.mating_pool:
        print(node)

def initialise_cities(num_cities):
    cities = []
    for i in range(num_cities):
        cities.append(City.City(i))
    return cities

def initialise_population(start_pop):
    nodes = []
    for i in range(start_pop):
        nodes.append(Node(i, []))
    return Population(nodes)

main()