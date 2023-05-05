import matplotlib.pyplot as plt  # Importing the graph library
import random  # importing the "random" library
import math  # importing the "math" library

# Making the "Problem" class


class Problem:

    # Problem class Constructor
    def __init__(self, fileName, vahicules, startingPoint):
        self.length = 0
        self.x = []
        self.y = []
        # Passing the number of vehicules and the starting point as parameters
        self.vehicules = vahicules
        self.startingPoint = startingPoint
        with open(fileName, 'r') as fp:
            # Setting the length to the number of lines in the file
            self.length = sum(1 for _ in fp)
            # Resetting the file pointer to the beginning of the file
            fp.seek(0)
            # Storing the data in the x and y lists
            for each in fp:
                tab = each.strip().split()
                self.x.append(float(tab[1]))
                self.y.append(float(tab[2]))


# Making the "population" class
class Population:

    # Generating a random individual
    def randomIndividual(fileLength, vehicules, startingPoint):
        individual = list(range(1, fileLength + vehicules))
        random.shuffle(individual)
        individual.remove(startingPoint)
        return individual

    # Making an initial population using "n" individuals
    def initialPopulation(n, vehicules, length, startingPoint):
        population = []
        for i in range(n):
            individual = Population.randomIndividual(
                length, vehicules, startingPoint)
            # print(individual)
            population.append(individual)
        return population


class Algorithm:

    # Generating routes
    def route(lst, length):
        route = []
        routesList = []
        for item in lst:
            if (item <= length):
                route.append(item)
            else:
                routesList.append(route)
                route = []
        routesList.append(route)
        return routesList

    #
    def getRoutes(initialPopulation, length):
        list = []
        for i in initialPopulation:
            list.append(Algorithm.route(i, length))
        return list

    # Calculating the distance of a route
    def distance(x1, y1, x2, y2):
        # Making the two points p1 and p2
        point1 = x1 - x2
        point2 = y1 - y2
        # Returns the distance between two points
        return math.sqrt(point1 ** 2 + point2 ** 2)

    # Retreiving the Best fitness value
    def fitnessValue(individual, x, y, startingPoint):
        values = []
        for item in individual:
            distance = 0
            # Adding the starting point at the beginning and the end of the list
            item.insert(0, startingPoint)
            item.append(startingPoint)

            for i in range(len(item)-1):
                j = i + 1
                distance += Algorithm.distance(x[item[i]-1],
                                               y[item[i]-1], x[item[j]-1], y[item[j]-1])
            values.append(distance)
        return max(values)

    # the Selection function
    def selection(initialPopulation, n, x, y, startingPoint, length):
        finalList = []
        index = 0
        routes = Algorithm.getRoutes(initialPopulation, length)
        while (index < n):
            # Incrementing the index variable
            index += 1
            # Generate the first random number and retrieving the fitness value
            num1 = random.randint(1, n)
            fitnessValue1 = Algorithm.fitnessValue(
                routes[num1 - 1], x, y, startingPoint)
            # Generate the second random number and retrieving the fitness value
            num2 = random.randint(1, n)
            fitnessValue2 = Algorithm.fitnessValue(
                routes[num2 - 1], x, y, startingPoint)

            # Checking who has the smallest fitness Value
            if (fitnessValue2 >= fitnessValue1):
                finalList.append(initialPopulation[num1 - 1])
            else:
                finalList.append(initialPopulation[num2 - 1])
        return finalList

    # The Crossover function
    def crossover(strs, strs1):
        copy_strs = strs.copy()
        copy_strs1 = strs1.copy()
        pos = int(random.random()*len(strs))  # starting position random

        # how many value it will take and dont go over list +1 so it will never be a 0
        ln = int(random.random()*(len(strs)-pos)+1)
        # THIS CODE TO SWITCH TWO BLOCK OF ARRAYS  1ST STEP

        def switch(strs, strs1):
            li = []
            for i in range(pos):
                li.append(strs[i])
            for i in range(pos, pos+ln):
                li.append(strs1[i])

            for i in range(pos+ln, len(strs)):
                li.append(strs[i])
            return li

        new = []
        new1 = []
        new = switch(strs, strs1)  # first list
        new1 = switch(strs1, strs)  # second  list

        strs = new.copy()
        strs1 = new1.copy()

        # DO THIS SO WE WONT HAVE THE SAME NUMBER TWICE (it will cause error)
        for i in range(len(strs)):
            if not (pos <= i <= pos+ln-1):
                strs[i] = ''
                strs1[i] = ''

        def place_the_value(liste, z):
            if z+1 > len(liste):

                global test
                test = False
                return 0
            else:
                y = z
                z = 0
                return y
        z = pos+ln
        test = True

        for i in range(len(copy_strs)):
            if not (copy_strs[i] in strs):
                if test == True:
                    z = place_the_value(strs, z)

                strs[z] = copy_strs[i]
                z += 1

        z = pos+ln
        test = True

        for i in range(len(copy_strs1)):

            if not (copy_strs1[i] in strs1):
                if test == True:
                    z = place_the_value(strs1, z)

                strs1[z] = copy_strs1[i]

                z += 1

        for i in range(len(strs)):  # trying to do 2nd step
            if not (pos <= i <= pos+ln-1):
                strs[i] = ''
                strs1[i] = ''

        def place_the_value(liste, z):
            if z+1 > len(liste):

                global test
                test = False
                return 0
            else:
                y = z
                z = 0
                return y
        z = pos+ln
        test = True

        for i in range(len(copy_strs)):
            if not (copy_strs[i] in strs):  # and not(pos <= i<= pos+ln-1)
                if test == True:
                    z = place_the_value(strs, z)
                strs[z] = copy_strs[i]
                z += 1
                
        z = pos+ln
        test = True
        for i in range(len(copy_strs1)):
            if not (copy_strs1[i] in strs1):  # and not(pos <= i<= pos+ln-1)
                if test == True:
                    z = place_the_value(strs1, z)
                strs1[z] = copy_strs1[i]
                z += 1
        return strs, strs1

    # Generating the recombination population
    def populationAfterCrossover(initialPopulation, n):
        finalList = []
        index = 0
        while (index < (n/2)):
            # Incrementing the index variable
            index += 1
            # Generate the first random number and retrieving the fitness value
            num1 = random.randint(1, n)
            randomIndividual1 = initialPopulation[num1 - 1]
            # Generate the second random number and retrieving the fitness value
            num2 = random.randint(1, n)
            randomIndividual2 = initialPopulation[num2 - 1]

            # Checking who has the smallest fitness Value
            list1, list2 = Algorithm.crossover(randomIndividual1, randomIndividual2)
            finalList.append(list1)
            finalList.append(list2)
        return finalList
    
    # The mutation function
    # mutation is to choose a bit and change it with a value of a random index (with probability)
    def individualMutation(individual, rate):
        for cityindex in range(len(individual)):  # choose first value
            if (random.random() < rate):  # the probability
                # all these is to switch the two values
                city_index_to_switch = int(random.random()*len(individual))
                city1 = individual[cityindex]
                city2 = individual[city_index_to_switch]

                individual[cityindex] = city2
                individual[city_index_to_switch] = city1
        return individual  # return list after mutation

    #
    def populationAfterMutation(initialPopulation, rate):
        listAfterMutation = []
        for individual in initialPopulation:
            listAfterMutation.append(
                Algorithm.individualMutation(individual, rate))
        return listAfterMutation


# print(Algorithm.split_list(Population.initialPopulation(500, 3)))
if __name__ == '__main__':

    p = Problem("cidades29.tsp.txt", 3, 13)

    # Printing the initial population
    # print(Population.initialPopulation(500, p.vehicules, p.length, p.startingPoint))

    # Plot the data as a scatter plot
    plt.scatter(p.x, p.y)

    # Add labels and a title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter plot')

    # Show the plot
    # plt.show()

    # print(p.startingPoint)
    # Population.initialPopulation(500, p.vehicules, p.length, p.startingPoint)
    list = Population.initialPopulation(500, p.vehicules, p.length, p.startingPoint)
    print("1st List:")
    print(list)
    routesList = Algorithm.getRoutes(list, p.length)
    listAfterSelection = Algorithm.selection(list, 500, p.x, p.y, p.startingPoint, p.length)
    print("List after selection:")
    print(listAfterSelection)
    listAfterRecombination = Algorithm.populationAfterCrossover(listAfterSelection, 500)
    print("List after recombination:")
    print(listAfterRecombination)
    listAfterMutation = Algorithm.populationAfterMutation(listAfterRecombination, 0.05)
    print("List after mutation:")
    print(listAfterMutation)
