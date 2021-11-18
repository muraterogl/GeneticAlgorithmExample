import java.util.Comparator;
import java.util.Arrays;

class GaExample {
    public static final int POPULATION_SIZE = 100;
    public static final String GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}";
    public static final String TARGET = "My name is Murat";
    
    public static void main(String[] args) {
        GaExample ga = new GaExample();
        ga.start();
    }
    public int random_num(int min, int max) {
        return (int) (Math.random() * (max - min)) + min;
    }
    public char mutated_genes() {
        return GENES.charAt(random_num(0, GENES.length()-1));
    }
    public String create_genome() {
        String genome = "";
        for (int i=0; i<TARGET.length(); i++) {
            genome += mutated_genes();
        }
        return genome;
    }
    class Individual implements Comparable<Individual>{
        String chromosome;
        int fitness;
        public Individual() {
            this.chromosome = create_genome();
            this.fitness = cal_fitness();
        }
        public Individual(String chromosome) {
            this.chromosome = chromosome;
            this.fitness = cal_fitness();
        }
        public Individual mate(Individual par2) {
            String child_chromosome = "";
            for (int i=0; i<this.chromosome.length(); i++) {
                int p = random_num(0, 100);
                if (p < 45) {
                    child_chromosome += this.chromosome.charAt(i);
                }
                else if (p < 90) {
                    child_chromosome += par2.chromosome.charAt(i);
                }
                else {
                    child_chromosome += mutated_genes();
                }
            }
            return new Individual(child_chromosome);
        }
        public int cal_fitness() {
            int fitness = 0;
            for (int i=0; i<TARGET.length(); i++) {
                if (this.chromosome.charAt(i) != TARGET.charAt(i)) {
                    fitness++;
                }
            }
            return fitness;
        }

        @Override
        public int compareTo(Individual i2) {
            return this.fitness - i2.fitness;
        }
        @Override
        public String toString() {
            return String.format("String: %s\tFitness: %d", this.chromosome, this.fitness);
        }
    }
    public void start() {
        long startTime = System.currentTimeMillis();
        int generation = 0;
        Individual[] population = new Individual[POPULATION_SIZE];
        boolean found = false;
        for (int i=0; i < POPULATION_SIZE; i++) {
            population[i] = new Individual();
        }
        while (!found) {
            Arrays.sort(population);
            if (population[0].fitness <= 0) {
                found = true;
                break;
            }
            Individual[] newGeneration = new Individual[POPULATION_SIZE];
            int s = 10*POPULATION_SIZE/100;
            for (int i=0; i<s; i++) {
                newGeneration[i] = population[i];
            }
            for (int i=s; i<POPULATION_SIZE; i++) {
                int p1 = random_num(0, POPULATION_SIZE/2);
                int p2 = random_num(0, POPULATION_SIZE/2);
                newGeneration[i] = population[p1].mate(population[p2]);
            }
            population = newGeneration;
            System.out.format("Generation: %d\t%s\n",generation, population[0]);
            generation++;
        }
        
        System.out.format("Generation: %d\t%s\n",generation, population[0]);
        long stopTime = System.currentTimeMillis();
        System.out.format("Elapsed time: %dms\n",stopTime-startTime);
    }
}