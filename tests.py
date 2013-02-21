import random
import unittest
from mock import Mock, patch
from genetics import Genome, Population


class TestGenome(unittest.TestCase):
    def setUp(self):
        self.genomeA = Genome([1, 2, 3, 4, 5, 6, 7, 8])
        self.genomeB = Genome([8, 7, 6, 5, 4, 3, 2, 1])

    def test_mate(self):
        child = self.genomeA.mate(self.genomeB);
        expected_child = Genome([1, 2, 3, 4, 4, 3, 2, 1])
        self.assertEqual(child, expected_child)

    @patch.object(random, 'randint')
    def test_mutate(self):
        expected_mutant = Genome([2, 2, 3, 4, 5, 6, 7, 8])
        mock_randint.return_value = 0
        self.genomeA.mutate()
        self.assertEqual(self.genomeA, expected_mutant, expected_mutant)


if __name__ == "__main__":
    unittest.main()
