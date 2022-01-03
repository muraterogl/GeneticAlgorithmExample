import time
import numpy as np

POPULATION_SIZE = 100
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"
TARGET = "My name is Murat"
GENES = np.array(list(GENES))
TARGET = np.array(list(TARGET))
GENES_LEN = len(GENES)
TARGET_LEN = len(TARGET)
def randomGene(): return np.random.choice(GENES, replace=False)
def randomGenes(): return np.random.choice(GENES, size=TARGET_LEN, replace=False)
def indexToGenes(n): return [GENES[i] for i in n]
def fitness(n): return np.sum(n!=TARGET, axis=1)

start = time.perf_counter()
generation = 0
population = population = indexToGenes(np.random.randint(0, GENES_LEN, size=[POPULATION_SIZE, TARGET_LEN]))
found = False

while not found:
    population = np.array(population)[np.argsort(fitness(population))]
    bf = fitness([population[0]])[0]
    if bf <= 0:
        found = True
        break
    elites = population[:10,:]
    offspring = np.empty_like(population)[:90,:]
    for s in range(0,90,2):
        i1 = np.random.randint(0,10)
        i2 = np.random.randint(0,10)
        for x in range(TARGET_LEN):
            ğ = np.random.randint(0,100)
            if ğ < 45:
                offspring[s, x] = elites[i1, x]
                offspring[s+1, x] = elites[i2, x]
            elif ğ < 90:
                offspring[s, x] = elites[i2, x]
                offspring[s+1, x] = elites[i1, x]
            else:
                offspring[s, x] = randomGene()
                offspring[s+1, x] = randomGene()
    population[:10]=elites
    population[10:]=offspring
    #population = np.concatenate((elites, offspring), axis=0)
    #print(f"Generation: {generation}\tString: {population[0].chromosome}\tFitness: {population[0].fitness}")
    generation += 1

end = time.perf_counter()
print(f"Time elapsed: {(end - start)*1000:.2f}ms, generation count: {generation}")
