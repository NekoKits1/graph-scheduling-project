"""Automatic test: the subject's example, solved by hand (Google Doc, section 2).

Each test is skipped while its function is not written yet, and must pass once it is.
Run:  python -m unittest discover -s tests -v
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reader import read_table
from graph import build_edges, build_matrix
from checks import is_scheduling_graph
from calendar_calc import compute_ranks, earliest_dates, latest_dates
from critical import compute_floats, critical_paths

TABLE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tables", "table_01_subject_example.txt")
CYCLE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tables", "table_02_cycle.txt")

N = 5
TASKS = {1: {"duration": 1, "preds": []}, 2: {"duration": 2, "preds": []}, 3: {"duration": 3, "preds": [1]},
         4: {"duration": 4, "preds": [1, 2]}, 5: {"duration": 5, "preds": [2, 4]}}
EDGES = {(0, 1, 0), (0, 2, 0), (1, 3, 1), (1, 4, 1), (2, 4, 2), (2, 5, 2), (3, 6, 3), (4, 5, 4), (5, 6, 5)}
X = None
MATRIX = [[X, 0, 0, X, X, X, X],
          [X, X, X, 1, 1, X, X],
          [X, X, X, X, 2, 2, X],
          [X, X, X, X, X, X, 3],
          [X, X, X, X, X, 4, X],
          [X, X, X, X, X, X, 5],
          [X, X, X, X, X, X, X]]
RANKS = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4}
EARLIEST = {0: 0, 1: 0, 2: 0, 3: 1, 4: 2, 5: 6, 6: 11}
LATEST = {0: 0, 1: 1, 2: 0, 3: 8, 4: 2, 5: 6, 6: 11}
FLOATS = {0: 0, 1: 1, 2: 0, 3: 7, 4: 0, 5: 0, 6: 0}


def quiet(function, *args):
    """Call a function without printing its trace; skip the test if it is not written yet."""
    try:
        with redirect_stdout(io.StringIO()):
            return function(*args)
    except NotImplementedError as missing:
        raise unittest.SkipTest(f"not written yet: {missing}")


class SubjectExample(unittest.TestCase):
    def test_read_table(self):
        tasks, n = quiet(read_table, TABLE)
        self.assertEqual(n, N)
        self.assertEqual({t: tasks[t]["duration"] for t in tasks}, {t: TASKS[t]["duration"] for t in TASKS})
        self.assertEqual({t: sorted(tasks[t]["preds"]) for t in tasks}, {t: TASKS[t]["preds"] for t in TASKS})

    def test_build_edges(self):
        self.assertEqual(set(quiet(build_edges, TASKS, N)), EDGES)

    def test_build_matrix(self):
        self.assertEqual(quiet(build_matrix, sorted(EDGES), N), MATRIX)

    def test_is_scheduling_graph(self):
        self.assertTrue(quiet(is_scheduling_graph, MATRIX))

    def test_compute_ranks(self):
        self.assertEqual(quiet(compute_ranks, MATRIX), RANKS)

    def test_earliest_dates(self):
        self.assertEqual(quiet(earliest_dates, MATRIX, RANKS), EARLIEST)

    def test_latest_dates(self):
        self.assertEqual(quiet(latest_dates, MATRIX, RANKS, EARLIEST), LATEST)

    def test_compute_floats(self):
        self.assertEqual(quiet(compute_floats, EARLIEST, LATEST), FLOATS)

    def test_critical_paths(self):
        self.assertEqual(quiet(critical_paths, MATRIX, EARLIEST, FLOATS), [[0, 2, 4, 5, 6]])


class CycleTable(unittest.TestCase):
    def test_cycle_is_rejected(self):
        tasks, n = quiet(read_table, CYCLE)
        matrix = quiet(build_matrix, quiet(build_edges, tasks, n), n)
        self.assertFalse(quiet(is_scheduling_graph, matrix))


if __name__ == "__main__":
    unittest.main()
