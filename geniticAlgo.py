from random import seed
from random import randint
from random import choice
import satInstances as satdata


satVariableLength=75
satisfactionGaol=325
individual=[]
population=[]
data=[]
fitnessValues=[]
fitness=0

def generatPpopulation(numberOfIndividuals):
    global individual
    global population
    for i in range(numberOfIndividuals):
        seed(randint(0,i+1))
        for i in range(satVariableLength):
            individual.append(randint(-75,75))
        population.append(individual)    
        individual=[]
    return population    

def sortFitness(element):
    return element[1]

def generatAndFitnessFirstPopulation(numberOfIndividuals):
    global data
    global fitnessValues
    global population
    global fitness
    generatPpopulation(numberOfIndividuals)
    data=satdata.returnInstances()
    for i in range(len(population)):
        

        for y in range(len(data[0])):
            
            for x in range(3):
               
                if data[0][y][x] in population[i]:
                    fitness+=1
                    break
        fitnessValues.append([i,fitness])
        fitness=0            
    fitnessValues.sort(key=sortFitness,reverse=True) #this will sort the individuals from best to worst

    
def crossOver(rateOfCrossOver):
    global population
    firstChild=[]
    secondChild=[]
    for i in range(len(population)//rateOfCrossOver):
        parentOne=population[fitnessValues[i][0]]
        parentTow=population[fitnessValues[i+1][0]]
        firstChild=parentOne[0:38]+parentTow[38:]
        secondChild=parentOne[38:]+parentTow[0:38]
        del population[((-1)*i)-1]
        del population[((-1)*i)-1]
        population.append(firstChild)
        population.append(secondChild)    


def mutation(rateOfMutation):
    global population
    for i in range((len(population)*rateOfMutation)//100):
        seed(randint(0,i+1))
        for j in range(len(population[i])):
            population[i][j]=choice(population[i])
            

def fitnessVerification():
    global population
    global data
    global fitness
    global fitnessValues
    fitnessValues=[]
    for i in range(len(population)):
        

        for y in range(len(data[0])):
            
            for x in range(3):
               
                if data[0][y][x] in population[i]:
                    fitness+=1
                    break
        fitnessValues.append([i,fitness])
        fitness=0            
    fitnessValues.sort(key=sortFitness,reverse=True)
       
def fitnessDeclaration(numberOfIteration):
    if fitnessValues[0][1] == 325:
        print("we found a solution for the sat problem in iteration number "+str(numberOfIteration+1)+" :")
        print(fitnessValues[0][1])
    else :
        print(" we could not find soloution in the "+str(numberOfIteration+1)+" iteration and the best one is")
        print(fitnessValues[0][1]) 

def geniticAlgo(numberOfIteration,numberOfIndividuals,rateOfCrossOver,rateOfMutation):
    generatAndFitnessFirstPopulation(numberOfIndividuals)
    for i in range(numberOfIteration):
        crossOver(rateOfCrossOver)
        fitnessVerification()
        fitnessDeclaration(i)
        mutation(rateOfMutation)


