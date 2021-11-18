const POPULATION_SIZE = 100;
const GENES =
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}';
const TARGET = "My name is Murat";

const random_num = (min, max) =>
    Math.floor(Math.random() * (max - min + 1) + min);

const mutated_genes = () => GENES[random_num(0, GENES.length - 1)];

const create_gnome = () =>
    [...Array(TARGET.length)].map((_) => mutated_genes()).join("");

class Individual {
    constructor(chromosome) {
        this.chromosome =
            chromosome === undefined ? create_gnome() : chromosome;
        this.fitness = [...Array(TARGET.length)]
            .map((_, i) => (this.chromosome[i] != TARGET[i] ? 1 : 0))
            .reduce((a, b) => a + b);
    }
    mate = (par2) =>
        new Individual(
            [...Array(par2.chromosome.length)]
                .map((_, i) => {
                    const p = random_num(0, POPULATION_SIZE);
                    if (p < 45) return this.chromosome[i];
                    else if (p < 90) return par2.chromosome[i];
                    return mutated_genes();
                })
                .join("")
        );
}
console.time("Time elapsed");
generation = 0;
population = [...Array(POPULATION_SIZE)].map((_) => new Individual());
found = false;

while (!found) {
    population = population.sort((a, b) => a.fitness - b.fitness);
    if (population[0].fitness <= 0) {
        found = true;
        break;
    }
    newGeneration = [...Array(POPULATION_SIZE)].map((_, i) => {
        if (i < (10 * POPULATION_SIZE) / 100) {
            return population[i];
        } else {
            p1 = random_num(0, Math.floor(POPULATION_SIZE / 2));
            p2 = random_num(0, Math.floor(POPULATION_SIZE / 2));
            return population[p1].mate(population[p2]);
        }
    });
    population = newGeneration;
    console.log(
        `Generation: ${generation}\tString: ${population[0].chromosome}\tFitness: ${population[0].fitness}`
    );
    generation++;
}

console.log(
    `Generation: ${generation}\tString: ${population[0].chromosome}\tFitness: ${population[0].fitness}`
);
console.timeEnd("Time elapsed");
