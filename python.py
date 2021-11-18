import random
import time

POPULATION_SIZE = 100
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"
TARGET = "My name is Murat"

def random_num(min, max):
    return random.randint(min, max)

def mutated_genes():
    return GENES[random_num(0, len(GENES)-1)]

def create_genome():
    return "".join([mutated_genes() for i in range(len(TARGET))])

class Individual:
    def __init__(self, *args):
        self.chromosome = args[0] if len(args)>0 else create_genome()
        self.fitness = sum(1 if self.chromosome[i]!=TARGET[i] else 0 for i in range(len(TARGET)))
    def mate(self, par2):
        return Individual("".join([self.chromosome[i] if (p:=random_num(0,POPULATION_SIZE))<45 else par2.chromosome[i] if p<90 else mutated_genes() for i in range(len(par2.chromosome))]))
    
start = time.perf_counter()
generation = 0
population = [Individual() for i in range(POPULATION_SIZE)]
found = False

while not found:
    population.sort(key=lambda x:x.fitness)
    if population[0].fitness <= 0:
        found = True
        break
    newGeneration = [population[i] if i<10*POPULATION_SIZE/100 else population[random_num(0, POPULATION_SIZE/2)].mate(population[random_num(0, POPULATION_SIZE/2)]) for i in range(POPULATION_SIZE)]
    population = newGeneration
    print(f"Generation: {generation}\tString: {population[0].chromosome}\tFitness: {population[0].fitness}")
    generation += 1

print(f"Generation: {generation}\tString: {population[0].chromosome}\tFitness: {population[0].fitness}")
end = time.perf_counter()
print(f"Time elapsed: {(end - start)*1000:.2f}ms")