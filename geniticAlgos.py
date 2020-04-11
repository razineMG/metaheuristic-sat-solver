from random import seed
from random import randint
import satInstances as satdata


satVariableLength=75
individual=[]
population=[]
data=[]
fitnessValues=[]
fitness=0

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


def fitnessFirstPopulation(numberOfIndividuals):
    global data
    global fitnessValues
    global population
    global fitness
    generatPpopulation(numberOfIndividuals)
    data=satdata.returnInstances()
    print(len(data[0]))
    for i in population:

        for y in data[0]:
            for x in range(3):
                if data[0][y][x] in population[i]:
                    fitnessValues.append([i,fitness+1])
    

    
fitnessFirstPopulation(5)
print(fitnessValues)
