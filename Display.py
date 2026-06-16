import matplotlib.pyplot as plt

class Display:
    def __init__(self, best_node, index):
        self.best_node = best_node
        self.index = index

    def plot(self):
        plt.clf()
        plt.xlabel('X-Koordinate')
        plt.ylabel('Y-Koordinate')
        plt.title(str( "Aktuelle Generation: " + str(self.index) + "\n" +
                    "Höchste Fitness der aktuellen Generation: " + str(self.best_node.fitness) + "\n" +
                    "Aktuelle kürzeste Strecke: " + str(1 / self.best_node.fitness)))
        x_coords = [city.location[0] for city in self.best_node.tour]
        y_coords = [city.location[1] for city in self.best_node.tour]

        x_coords.append(self.best_node.tour[0].location[0])
        y_coords.append(self.best_node.tour[0].location[1])

        plt.plot(x_coords, y_coords, color='black')
        plt.scatter(x_coords, y_coords, s=50, c='black')

        plt.savefig("images/" + str(self.index) + ".png")
        plt.show()

