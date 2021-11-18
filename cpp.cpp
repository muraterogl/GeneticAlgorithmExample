#include <bits/stdc++.h>
using namespace std;


#define POPULATION_SIZE 100
 
const string GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}";
const string TARGET = "My name is Murat";

int random_num(int start, int end) {
    int range = (end-start)+1;
    int random_int = start+(rand()%range);
    return random_int;
}
 
char mutated_genes() {
    int len = GENES.size();
    int r = random_num(0, len-1);
    return GENES[r];
}

string create_genome() {
    int len = TARGET.size();
    string genome = "";
    for(int i = 0;i<len;i++)
        genome += mutated_genes();
    return genome;
}

class Individual {
public:
    string chromosome;
    int fitness;
    Individual();
    Individual(string chromosome);
    Individual mate(Individual parent2);
    int cal_fitness();
};

Individual::Individual() {
    this->chromosome = create_genome();
    fitness = cal_fitness();
};

Individual::Individual(string chromosome) {
    this->chromosome = chromosome;
    fitness = cal_fitness();
};

Individual Individual::mate(Individual par2) {
    string child_chromosome = "";
 
    int len = chromosome.size();
    for(int i=0; i<len; i++) {
        
        int p = random_num(0, 100);
 
        if(p < 45)
            child_chromosome += chromosome[i];
        else if(p < 90)
            child_chromosome += par2.chromosome[i];
        else
            child_chromosome += mutated_genes();
    }
    return Individual(child_chromosome);
};
 
int Individual::cal_fitness() {
    int len = TARGET.size();
    int fitness = 0;
    for(int i=0; i<len; i++)
    {
        if(chromosome[i] != TARGET[i])
            fitness++;
    }
    return fitness;   
};

bool compareIndividual(const Individual &ind1, const Individual &ind2) {
    return ind1.fitness < ind2.fitness;
}

int main()
{
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
    auto start = high_resolution_clock::now();
    srand((unsigned)(time(0)));

    int generation = 0;
 
    Individual population[POPULATION_SIZE];
    bool found = false;
 
    while(!found) {
        sort(begin(population), end(population), compareIndividual);
        if(population[0].fitness <= 0) {
            found = true;
            break;
        }
        Individual new_generation[POPULATION_SIZE];
 
        int s = (10*POPULATION_SIZE)/100;
        for(int i=0; i<s; i++)
            new_generation[i]=population[i];
        
        for(int i=s; i<POPULATION_SIZE; i++){
            new_generation[i] = population[random_num(0, 50)].mate(population[random_num(0, 50)]);
        }
        for(int i = 0;i<POPULATION_SIZE;i++) {   
            population[i]=new_generation[i];
        }
        cout<< "Generation: " << generation << "\t";
        cout<< "String: "<< population[0].chromosome <<"\t";
        cout<< "Fitness: "<< population[0].fitness << "\n";
        generation++;
     }
    cout<< "Generation: " << generation << "\t";
    cout<< "String: "<< population[0].chromosome <<"\t";
    cout<< "Fitness: "<< population[0].fitness << "\n";
    auto end = high_resolution_clock::now();
    duration<double, std::milli> ms_double = end - start;
    cout << ms_double.count() << "ms" << endl;
}