import random

#Creating a random population
def randomIndividual():
    individual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    random.shuffle(individual)
    return individual

def population():
    population = []
    for i in range (500):
        individual = randomIndividual()
        population.append(individual)
    return population

print(population())