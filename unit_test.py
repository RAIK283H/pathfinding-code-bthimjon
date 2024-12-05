import math
import unittest
import graph_data
import pathing
import permutation
from itertools import permutations
import global_game_data
import f_w


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

    def test_DijkstrasToTarget(self):
        end = len(graph_data.graph_data[0])-1
        path = pathing.dijkstrasToTarget(0,0,end)
        result = path[len(path)-1]
        self.assertEqual(end,result)

    def test_FloydWarshallPathSmallGraph(self):
        parent = [[0, 0, 1], [1, 1, 1], [1, 2, 2]]
        resultPath = f_w.FloydWarshallPath(parent,0,2)
        expectedPath = [0,1,2]
        self.assertEqual(resultPath,expectedPath," Did not result in the correct path for a small graph")

    def test_FloydWarshallPathBigGraph(self):
        parent = [[0, 0, 1, 2], [1, 1, 1, 2], [1, 2, 2, 2], [1, 2, 3, 3]]
        resultPath = f_w.FloydWarshallPath(parent,0,3)
        expectedPath = [0,1,2,3]
        self.assertEqual(resultPath,expectedPath," Did not result in the correct path for a big graph")
    def test_FloydWarshallPathEmpty(self):
        parent = [[None,None,None], [None,None,None], [None, None, None]]
        resultPath = f_w.FloydWarshallPath(parent,0,2)
        expectedPath = None
        self.assertEqual(resultPath, expectedPath, "Did not result in the correct path for an empty graph")
    def test_FloydWarshallPathOneNode(self):
        parent = [[0]]
        resultPath = f_w.FloydWarshallPath(parent,0,0)
        expectedPath = [0]
        self.assertEqual(resultPath, expectedPath, "Did not result in the correct path for a graph with one node")

 


if __name__ == '__main__':
    unittest.main()
