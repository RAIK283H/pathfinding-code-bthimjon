import math
import unittest
import graph_data
import pathing
import permutation
from itertools import permutations


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
        
    def test_startToTarget(self):
        end = len(graph_data.graph_data[0])-1
        path = pathing.startToTarget(0,0,end)
        result = path[len(path)-1]
        self.assertEqual(end,result)

    def test_DFSToTarget(self):
        end = len(graph_data.graph_data[0])-1
        path = pathing.dfsToTarget(0,0,end)
        result = path[len(path)-1]
        self.assertEqual(end,result)

    def test_BFSToTarget(self):
        end = len(graph_data.graph_data[0])-1
        path = pathing.bfsToTarget(0,0,end)
        result = path[len(path)-1]
        self.assertEqual(end,result)

    def test_isValidHami_true(self):
        test = [1,2,3]
        result = permutation.is_valid_hami_cycle(test,4,9)
        self.assertTrue(result)

    def test_isValidHami_false(self):
        test = [0,1,2,3]
        result = permutation.is_valid_hami_cycle(test,4,9)
        self.assertFalse(result)

    def test_isValidHami_trueGraph0(self):
        test = [1]
        result = permutation.is_valid_hami_cycle(test,2,0)
        self.assertTrue(result)

    def test_isValidHami_noConnections(self):
        test = [1,2]
        result = permutation.is_valid_hami_cycle(test,3,11)
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()
