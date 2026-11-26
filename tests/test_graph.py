import unittest
from contextlib import redirect_stdout
from io import StringIO
from graph import (build_edges, build_matrix, display_edges, display_matrix,
                   predecessors, successors, check_weights)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.tasks = {1: {'duration': 1, 'preds': []},
                      2: {'duration': 2, 'preds': []},
                      3: {'duration': 3, 'preds': [1]},
                      4: {'duration': 4, 'preds': [1, 2]},
                      5: {'duration': 5, 'preds': [2, 4]}}
        self.edges = [(0, 1, 0), (0, 2, 0), (1, 3, 1), (1, 4, 1),
                      (2, 4, 2), (2, 5, 2), (3, 6, 3), (4, 5, 4), (5, 6, 5)]
        self.matrix = build_matrix(self.edges, 5)

    def test_edges(self):
        self.assertEqual(build_edges(self.tasks, 5), self.edges)

    def test_matrix(self):
        self.assertEqual(self.matrix, [
            [None, 0, 0, None, None, None, None],
            [None, None, None, 1, 1, None, None],
            [None, None, None, None, 2, 2, None],
            [None, None, None, None, None, None, 3],
            [None, None, None, None, None, 4, None],
            [None, None, None, None, None, None, 5],
            [None] * 7])

    def test_neighbors(self):
        self.assertEqual(predecessors(self.matrix, 4), [1, 2])
        self.assertEqual(successors(self.matrix, 4), [5])
        self.assertEqual(predecessors(self.matrix, 5), [2, 4])
        self.assertEqual(successors(self.matrix, 5), [6])
        self.assertEqual(predecessors(self.matrix, 1), [0])
        self.assertEqual(successors(self.matrix, 0), [1, 2])

    def test_display_edges(self):
        with redirect_stdout(StringIO()) as output:
            display_edges(self.edges, 5)
        self.assertEqual(output.getvalue().splitlines(),
                         ['Number of vertices: 7', 'Number of edges: 9'] +
                         [f'{a} -> {b} = {w}' for a, b, w in self.edges])

    def test_display_large_matrix(self):
        matrix = build_matrix([(0, 10, 0), (10, 13, 123)], 12)
        with redirect_stdout(StringIO()) as output:
            display_matrix(matrix)
        lines = output.getvalue().splitlines()[1:]
        self.assertEqual(len(lines), 15)
        self.assertEqual(len(set(map(len, lines))), 1)
        self.assertEqual(lines[11].split()[-1], '123')

    def test_weight_checks(self):
        for matrix, expected in [(self.matrix, True),
                                 (build_matrix([(0, 1, 0), (1, 2, -2)], 1), False),
                                 (build_matrix([(0, 1, 2)], 1), False),
                                 (build_matrix([(1, 2, 2), (1, 3, 3)], 2), False)]:
            with redirect_stdout(StringIO()) as output:
                self.assertEqual(check_weights(matrix), expected)
            self.assertEqual(len(output.getvalue().splitlines()), 3)

    def test_cycle_is_preserved(self):
        tasks = {1: {'duration': 2, 'preds': [2]},
                 2: {'duration': 3, 'preds': [1]}}
        self.assertEqual(build_edges(tasks, 2), [(1, 2, 2), (2, 1, 3)])

    def test_zero_duration(self):
        tasks = {1: {'duration': 0, 'preds': []}}
        self.assertEqual(build_edges(tasks, 1), [(0, 1, 0), (1, 2, 0)])


if __name__ == '__main__':
    unittest.main()
