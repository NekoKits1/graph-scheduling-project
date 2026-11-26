import unittest
from reader import read_table, display_constraint_table


class TestReadTable(unittest.TestCase):
    """Tests for reader.py using the subject's example."""

    def test_subject_example_tasks(self):
        """read_table returns the correct tasks dict."""
        tasks, n = read_table("tables/table_01_subject_example.txt")
        self.assertEqual(n, 5)
        self.assertEqual(tasks[1], {"duration": 1, "preds": []})
        self.assertEqual(tasks[3], {"duration": 3, "preds": [1]})
        self.assertEqual(tasks[4], {"duration": 4, "preds": [1, 2]})
        self.assertEqual(tasks[5], {"duration": 5, "preds": [2, 4]})

    def test_subject_example_n(self):
        """read_table returns the correct number of tasks."""
        tasks, n = read_table("tables/table_01_subject_example.txt")
        self.assertEqual(n, 5)

    def test_cycle_table(self):
        """read_table reads a table with a cycle without crashing."""
        tasks, n = read_table("tables/table_02_cycle.txt")
        self.assertEqual(n, 3)
        self.assertEqual(tasks[1]["preds"], [3])

    def test_missing_file(self):
        """read_table raises an error on a missing file."""
        with self.assertRaises(FileNotFoundError):
            read_table("tables/does_not_exist.txt")

    def test_display_does_not_crash(self):
        """display_constraint_table prints without crashing."""
        tasks, n = read_table("tables/table_01_subject_example.txt")
        display_constraint_table(tasks)

    def test_teacher_table_odd_format(self):
        """T13 has Windows line endings, an empty first line and no final newline."""
        tasks, n = read_table("tables/table_T13_teacher.txt")
        self.assertEqual(n, 4)
        self.assertEqual(tasks[2], {"duration": 2, "preds": [1, 3]})
        self.assertEqual(tasks[4], {"duration": 7, "preds": [3]})

    def test_all_teacher_tables(self):
        """Every teacher table reads with tasks numbered 1 to n."""
        for i in range(1, 15):
            tasks, n = read_table(f"tables/table_T{i:02d}_teacher.txt")
            self.assertEqual(sorted(tasks), list(range(1, n + 1)), f"table T{i:02d}")


if __name__ == "__main__":
    unittest.main()