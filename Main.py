from City import City
from Display import Display
from Nodehandler import *

QUIT_VALUE = 0.00000000000001
MAX_ITERATIONS = 1000

def main():
    cities = initialise_cities(10)
    initial_pop = initialise_population(20)
    initial_pop.generate_tours(cities)

    initial_pop.evaluate_nodes()
    initial_pop.select_best()

    display = Display(initial_pop.mating_pool[0], 0)
    display.plot()

    last_pop = initial_pop
    index = 0
    best_fitness_diff = float('inf')

    while best_fitness_diff > QUIT_VALUE and index < MAX_ITERATIONS:
        
        current_pop = gen_new_population(last_pop)
        current_pop.mutate_pop()

        current_pop.evaluate_nodes()
        current_pop.select_best()
        index += 1
        print("Akutelle beste fitness:", current_pop.best_fitness)

        display = Display(current_pop.mating_pool[0], index)

        #best_fitness_diff = current_pop.best_fitness.fitness - last_pop.best_fitness.fitness
        last_pop = current_pop



    print("Die Anzahl der Generationen: ", str(index))
    display.plot()

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