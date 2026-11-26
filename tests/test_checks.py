import io
import unittest
from contextlib import redirect_stdout

from reader import read_table
from graph import build_edges, build_matrix
from checks import eliminate_entry_points, is_scheduling_graph

N = None
# Value matrix of the subject's example (Google Doc, step C), typed by hand.
EXAMPLE = [
    [N, 0, 0, N, N, N, N],
    [N, N, N, 1, 1, N, N],
    [N, N, N, N, 2, 2, N],
    [N, N, N, N, N, N, 3],
    [N, N, N, N, N, 4, N],
    [N, N, N, N, N, N, 5],
    [N, N, N, N, N, N, N],
]


def matrix_of(path):
    """Read a table and build its value matrix with the merged reader and graph."""
    tasks, n = read_table(path)
    return build_matrix(build_edges(tasks, n), n)


def quiet(function, *args):
    """Call a function without printing its trace."""
    with redirect_stdout(io.StringIO()):
        return function(*args)


class TestEliminateEntryPoints(unittest.TestCase):

    def test_example_rounds(self):
        """Step E of the doc: rounds of the example, nothing left."""
        rounds, remaining = eliminate_entry_points(EXAMPLE, False)
        self.assertEqual(rounds, [[0], [1, 2], [3, 4], [5], [6]])
        self.assertEqual(remaining, [])

    def test_no_print_when_show_trace_false(self):
        """Lea reuses it for the ranks: nothing must be printed."""
        out = io.StringIO()
        with redirect_stdout(out):
            eliminate_entry_points(EXAMPLE, False)
        self.assertEqual(out.getvalue(), "")

    def test_cycle_in_the_middle(self):
        """Tasks 2 and 3 wait for each other: stuck after round 1."""
        rounds, remaining = eliminate_entry_points(matrix_of("tables/table_03_cycle_middle.txt"), False)
        self.assertEqual(rounds, [[0], [1]])
        self.assertEqual(remaining, [2, 3, 4, 5])

    def test_teacher_cycle_T01(self):
        """T01 has the cycle 4 -> 5 -> 6 -> 13 -> 4."""
        _, remaining = eliminate_entry_points(matrix_of("tables/table_T01_teacher.txt"), False)
        for v in (4, 5, 6, 13):
            self.assertIn(v, remaining)


class TestIsSchedulingGraph(unittest.TestCase):

    def test_example_is_valid(self):
        self.assertTrue(quiet(is_scheduling_graph, EXAMPLE))

    def test_two_chains_is_valid(self):
        self.assertTrue(quiet(is_scheduling_graph, matrix_of("tables/table_04_two_chains.txt")))

    def test_cycles_are_refused(self):
        for name in ("table_02_cycle", "table_03_cycle_middle", "table_T01_teacher", "table_T12_teacher"):
            self.assertFalse(quiet(is_scheduling_graph, matrix_of(f"tables/{name}.txt")), name)

    def test_all_cycle_table_fails_entry_and_exit(self):
        """In table_02 every task is in the cycle: 0 and N+1 are both entry and exit points."""
        out = io.StringIO()
        with redirect_stdout(out):
            is_scheduling_graph(matrix_of("tables/table_02_cycle.txt"))
        self.assertIn("single entry point", out.getvalue())
        self.assertIn("single exit point", out.getvalue())

    def test_negative_duration_is_refused(self):
        self.assertFalse(quiet(is_scheduling_graph, matrix_of("tables/kirolos_negative.txt")))

    def test_other_teacher_tables_are_valid(self):
        for i in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14):
            self.assertTrue(quiet(is_scheduling_graph, matrix_of(f"tables/table_T{i:02d}_teacher.txt")), f"T{i:02d}")


if __name__ == "__main__":
    unittest.main()
