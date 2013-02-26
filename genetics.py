import random


class Population(object):
    def __init__(self, members=None, size=50):
        if members is not None:
            self._members = members
        else:
            self._generate_initial_members(size)

    def _generate_initial_members(self, size):
        self._members = []
        for i in xrange(size):
            self._members.append(Genome.create())

    def get_fittest_pair(self, fitness_function):
        self._members.sort(
            lambda x, y: fitness_function(y) - fitness_function(x))
        return self._members[0], self._members[1]

    def size(self):
        return len(self._members)


class Genome(object):
    def __init__(self, solution):
        self.solution = solution

    def mate(self, other):
        half = len(self.solution) / 2
        child_solution = self.solution[0:half] + other.solution[half:]
        return Genome(child_solution)

    def mutate(self):
        index = random.randint(0, len(self.solution))
        self.solution[index] = self.solution[index] + 1
        if self.solution[index] > 8:
            self.solution[index] = 1

    def __eq__(self, other):
        return self.solution == other.solution

    def __str__(self):
        return str(self.solution)

    @classmethod
    def create(cls, size=8):
        base_solution = xrange(0, size)
        return Genome(random.sample(base_solution, len(base_solution)))


def fitness_function(genome):
    pair_count = count_pairs(genome)
    diagonal_count = count_diagonals(genome)
    return -(pair_count + diagonal_count)


def count_pairs(genome):
    pair_count = 0
    for i in xrange(len(genome.solution)):
        for j in xrange(i + 1, len(genome.solution)):
            if genome.solution[i] == genome.solution[j]:
                pair_count += 1
    return pair_count


def count_diagonals(genome):
    return 0