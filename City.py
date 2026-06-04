import numpy as np
import random as rnd

CITY_LOCATION_BOUND_UPPER = 10.0
CITY_LOCATION_BOUND_LOWER = 0.0

def gen_rand_coordinates():
    x_val = rnd.uniform(CITY_LOCATION_BOUND_LOWER, CITY_LOCATION_BOUND_UPPER)
    y_val = rnd.uniform(CITY_LOCATION_BOUND_LOWER, CITY_LOCATION_BOUND_UPPER)
    return np.array((x_val, y_val))

class City:
    def __init__(self, id):
        self.id = id
        self.location = gen_rand_coordinates()

    def __repr__(self):
        return "City " + str(self.id) + ": at: " + str(self.location)