import random


class Population(object):
    def __init__(self, members=None, size=50):
        if members != None:
            self._members = members
        else:
            self._generate_initial_members(size)

    def _generate_initial_members(self, size):
        for i in xrange(size):
            self._members.append(Genome.create())

    def get_fittest_pair(self, fitness_function):
        self._members.sort(self._members, fitness_function)
        return self._members[0], self._members[1]


class Genome(object):
    def __init__(self, solution):
        self.solution = solution

    def mate(self, other):
        half_index = len(self.solution) / 2
        child_solution = self.solution[0:half_index] + other.solution[half_index:]
        return Genome(child_solution)

    def mutate(self):
        index = random.randint(0, len(self.solution))
        self.solution[index] = (self.solution[index] + 1) % len(self.solution) + 1

    def __eq__(self, other):
        return self.solution == other.solution

    def __str__(self):
        return self.solution

    @classmethod
    def create(cls, size=8):
        base_solution = xrange(0, size)
        return Genome(random.sample(base_solution, len(base_solution)))


def fitness_function(genome):
    proposed_solution = genome.solution
    pass # TODO


def main():
    population = Population()