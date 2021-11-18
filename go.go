package main

import (
	"bytes"
	"fmt"
	"math/rand"
	"sort"
	"time"
)

const POPULATION_SIZE int = 100

const GENES string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"
const TARGET string = "My name is Murat"

func random_num(min int, max int) int {
	return rand.Intn(max - min + 1) + min
}

func mutated_genes() byte {
	len := len(GENES)
	r := random_num(0, len-1)
	return GENES[r]
}

func create_gnome() string {
	len := len(TARGET)
	gnome := bytes.NewBufferString("")
	for i:=0; i<len; i++ {
		gnome.WriteByte(mutated_genes())
	}
	return gnome.String()
}

type Individual struct {
	chromosome string
	fitness int
}

func makeIndividual(chromosome string) Individual {
	i := Individual{}
	i.chromosome = chromosome
	i.fitness = i.cal_fitness();
	return i
}

func (par1 Individual) mate(par2 Individual) Individual {
	child_chromosome := bytes.NewBufferString("")
	len := len(par1.chromosome)
	for i:=0; i<len; i++ {
		p := random_num(0,100)
		if p < 45 {
			child_chromosome.WriteByte(par1.chromosome[i])
		} else if p < 90 {
			child_chromosome.WriteByte(par2.chromosome[i])
		} else {
			child_chromosome.WriteByte(mutated_genes())
		}
	}
	return makeIndividual(child_chromosome.String())
}

func (p Individual) cal_fitness() int {
	len := len(TARGET)
	fitness := 0
	for i:=0; i<len; i++ {
		if p.chromosome[i] != TARGET[i] {
			fitness++
		}
	}
	return fitness
}

func main() {
	start := time.Now()
	rand.Seed(time.Now().UnixNano())
	generation := 0
	population := make([]Individual, 100)
	found := false
	for i:=0; i<POPULATION_SIZE; i++ {
		population[i] = makeIndividual(create_gnome())
	}

	for !found {
		sort.Slice(population, func(i int, j int) bool{
			return population[i].fitness < population[j].fitness
		})
		if population[0].fitness <=0 {
			found = true
			break
		}
		newGeneration := make([]Individual, 100)

		s:= 10*POPULATION_SIZE/100
		for i:=0; i<s; i++ {
			newGeneration[i] = population[i]
		}

		for i:=s; i<POPULATION_SIZE; i++ {
			p1 := random_num(0, POPULATION_SIZE/2)
			p2 := random_num(0, POPULATION_SIZE/2)
			newGeneration[i] = population[p1].mate(population[p2])
		}
		population = newGeneration
		fmt.Printf("Generation: %d\tString: %s\tFitness: %d\n", generation, population[0].chromosome, population[0].fitness)
		generation++
	}

	fmt.Printf("Generation: %d\tString: %s\tFitness: %d\n", generation, population[0].chromosome, population[0].fitness)
	elapsed := time.Since(start)
	fmt.Printf("Time elapsed: %s\n", elapsed)
}