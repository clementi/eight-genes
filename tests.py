import random
import unittest
from mock import Mock, patch
from genetics import Genome, Population, fitness_function


def fake_randint(a, b):
    return 0


class TestGenome(unittest.TestCase):
    def setUp(self):
        self.genomeA = Genome([1, 2, 3, 4, 5, 6, 7, 8])
        self.genomeB = Genome([8, 7, 6, 5, 4, 3, 2, 1])

    def test_mate(self):
        child = self.genomeA.mate(self.genomeB)
        expected_child = Genome([1, 2, 3, 4, 4, 3, 2, 1])
        self.assertEqual(child, expected_child)

    @patch('random.randint', fake_randint)
    def test_mutate(self):
        expected_mutant = Genome([2, 2, 3, 4, 5, 6, 7, 8])
        self.genomeA.mutate()
        self.assertEqual(self.genomeA, expected_mutant, str(self.genomeA))


class TestPopulation(unittest.TestCase):
    def test_init_with_no_parameters(self):
        random_population = Population()
        self.assertEqual(random_population.size(), 50)

    def test_get_fittest_pair(self):
        population = Population(
            members=[Genome([1, 2, 3, 4, 5, 6, 7, 8]),
                     Genome([8, 7, 6, 5, 4, 3, 2, 1]),
                     Genome([4, 3, 2, 1, 8, 7, 6, 5])])
        fittest_pair = population.get_fittest_pair(self._fitness_function)
        expected_fittest_pair = (
            Genome([8, 7, 6, 5, 4, 3, 2, 1]),
            Genome([4, 3, 2, 1, 8, 7, 6, 5]))
        self.assertEqual(fittest_pair, expected_fittest_pair)

    def _fitness_function(self, genome):
        return genome.solution[0]


class TestFitnessFunction(unittest.TestCase):
    def test_all_same(self):
        genome = Genome([1, 1, 1, 1, 1, 1, 1, 1])
        expected_fitness = -28
        fitness = fitness_function(genome)
        self.assertEqual(fitness, expected_fitness)

    def test_one_pair(self):
        genome = Genome([1, 1, 3, 5, 7, 2, 4, 6])
        expected_fitness = -1
        fitness = fitness_function(genome)
        self.assertEqual(fitness, expected_fitness)


if __name__ == "__main__":
    unittest.main()
