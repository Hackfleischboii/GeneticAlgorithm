import City
from Display import Display
import Nodehandler

MAX_ITERATIONS_NO_IMPROVE = 50
MAX_ITERATIONS = 5000
NUM_CITIES = 10
NUM_PER_POP = 100

def main():
    cities = initialise_cities(NUM_CITIES)
    initial_pop = initialise_population(NUM_PER_POP)
    initial_pop.generate_tours(cities)

    initial_pop.evaluate_nodes()
    initial_pop.create_mating_pool()

    display = Display(initial_pop.best_fitness, 0)
    print("Initial Pop's best fitness:", initial_pop.best_fitness)
    display.plot()

    last_pop = initial_pop

    no_change_counter = 0
    iteration = 0

    while (no_change_counter < MAX_ITERATIONS_NO_IMPROVE
           and iteration < MAX_ITERATIONS):
        cur_pop = Nodehandler.gen_new_population(last_pop)
        cur_pop.mutate_pop()

        cur_pop.evaluate_nodes()
        cur_pop.create_mating_pool()
        print(cur_pop.best_fitness, "in generation ", iteration)
        if cur_pop.best_fitness.fitness <= last_pop.best_fitness.fitness:
            no_change_counter += 1
        else:
            print("counter reset")
            no_change_counter = 0
        last_pop = cur_pop
        iteration += 1

    display = Display(last_pop.best_fitness, iteration)
    print("Last Pop's best fitness:", last_pop.best_fitness)
    print("No change counter ", no_change_counter)
    display.plot()

def initialise_cities(num_cities):
    cities = []
    for i in range(num_cities):
        cities.append(City.City(i))
    return cities

def initialise_population(start_pop):
    nodes = []
    for i in range(start_pop):
        nodes.append(Nodehandler.Node(i, []))
    return Nodehandler.Population(nodes)

main()