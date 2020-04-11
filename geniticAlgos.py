from random import seed
from random import randint
import satInstances as data


satVariableLength=75
individual=[]
population=[]


def generatPpopulation(numberOfIndividuals):
    global individual
    global population
    for i in range(numberOfIndividuals):
        seed(randint(0,1000))
        for i in range(satVariableLength):
            individual.append(randint(-75,75))
        population.append(individual)    
        individual=[]
    return population    


def firstPopulation(numberOfIndividuals):
    return generatPpopulation(numberOfIndividuals)

firstPopulation(10)
print(len(population))