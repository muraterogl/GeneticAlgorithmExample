using System;
using System.Diagnostics;

public class Program
{
	public const string GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}";
	public const string TARGET = "My name is Murat";
	public const int POPULATION_SIZE = 100;
	public static int random_num(int start, int end)
	{
		Random r = new Random();
		return r.Next(start, end);
	}

	public static char mutated_genes()
	{
		return GENES[random_num(0, GENES.Length - 1)];
	}

	public static string create_genome()
	{
		string genome = "";
		for (int i = 0; i < TARGET.Length; i++)
		{
			genome += mutated_genes();
		}

		return genome;
	}

	public class Individual : IComparable
	{
		public string chromosome;
		public int fitness;
		public Individual()
		{
			this.chromosome = create_genome();
			this.fitness = cal_fitness();
		}

		public Individual(string chromosome)
		{
			this.chromosome = chromosome;
			this.fitness = cal_fitness();
		}

		public Individual mate(Individual par2)
		{
			string child_chromosome = "";
			for (int i = 0; i < this.chromosome.Length; i++)
			{
				int p = random_num(0, 100);
				if (p < 45)
				{
					child_chromosome += this.chromosome[i];
				}
				else if (p < 90)
				{
					child_chromosome += par2.chromosome[i];
				}
				else
				{
					child_chromosome += mutated_genes();
				}
			}

			return new Individual(child_chromosome);
		}

		public int cal_fitness()
		{
			int fitness = 0;
			for (int i = 0; i < TARGET.Length; i++)
			{
				if (this.chromosome[i] != TARGET[i])
					fitness++;
			}

			return fitness;
		}

		public int CompareTo(object obj)
		{
			if (obj is Individual)
			{
				return this.fitness.CompareTo((obj as Individual).fitness);
			}

			throw new ArgumentException("Object is not a User");
		}
	}

	public static void Main()
	{
		var sw = Stopwatch.StartNew();
		int generation = 0;
		Individual[] population = new Individual[POPULATION_SIZE];
		for (int i = 0; i < POPULATION_SIZE; i++)
		{
			population[i] = new Individual();
		}

		bool found = false;
		while (!found)
		{
			Array.Sort(population);
			if (population[0].fitness <= 0)
			{
				found = true;
				break;
			}

			Individual[] newGeneration = new Individual[POPULATION_SIZE];
			int s = (10 * POPULATION_SIZE) / 100;
			for (int i = 0; i < s; i++)
			{
				newGeneration[i] = population[i];
			}

			for (int i = s; i < POPULATION_SIZE; i++)
			{
				newGeneration[i] = population[random_num(0, POPULATION_SIZE / 2)].mate(population[random_num(0, POPULATION_SIZE / 2)]);
			}

			population = newGeneration;
			Console.WriteLine($"Generation: {generation}\tString: {population[0].chromosome}\tFitness: {population[0].fitness}");
			generation++;
		}

		Console.WriteLine($"Generation: {generation}\tString: {population[0].chromosome}\tFitness: {population[0].fitness}");
		Console.WriteLine($"Elapsed time: {sw.ElapsedMilliseconds}ms");
	}
}