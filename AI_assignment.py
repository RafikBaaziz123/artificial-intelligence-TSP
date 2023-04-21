import matplotlib.pyplot as plt # Importing the graph library
import random # importing the "random" library

# Making the "Problem" class
class Problem:
 
    # Initialize the length of the file (prof said so)
    def __init__(self, fileName):
        length = 0
        x = []
        y = []
        with open(fileName, 'r') as fp:
            self.length = len(fp.readlines())
            for each in fp:
                tab = each.strip().split()
                self.x.append(float(tab[1]))
                self.y.append(float(tab[2]))


#x, y = Problem.read_point("cidades29.tsp.txt")
p = Problem("cidades29.tsp.txt")
print(p.x)

# Plot the data as a scatter plot
plt.scatter(x, y)

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter plot')

# Show the plot
#plt.show()

# Making the "population" class
class Population:
    
    # Generating a random individual
    def randomIndividual(fileLength, vehicules):
        individual=list(range(1, fileLength + vehicules))
        random.shuffle(individual)
        individual.remove(13)
        return individual
    
    # Making an initial population using "n" individuals
    def initialPopulation(n, vehicules):
        population = []
        p = Problem("cidades29.tsp.txt")
        for i in range (n):
            individual = Population.randomIndividual(p.length, vehicules)
            population.append(individual)
        return population
    
#print(Population.initialPopulation(500, 3))
#print(len(Population.initialPopulation(500, 3)))

class Algorithm:
    
    # Generating routes
    def split_list(lst):
        l = []
        p = Problem("cidades29.tsp.txt")
        sublists = []
        sublist = []
        print(p.length)
        for item in lst:
            for i in item:
                if i > p.length:
                    sublists.append(sublist)
                    sublist = []
                else:
                    sublist.append(item)
            sublists.append(sublist)
            l.append(sublists)
        return l
    
    # Calculating the distance of a route
    def distance(list, x, y):
        i = list[0]
        j = list[1]
        
print(Algorithm.split_list(Population.initialPopulation(500, 3)))