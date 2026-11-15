"""Reading a constraint table from a .txt file.

Owner: Member 1 — issue #2. Checked by: Member 2.
Shared names: README, section 4.
"""


def read_table(path):
    """Read a constraint table and store it in memory.

    Each line: task number, duration, then its predecessors (zero or more).
    Returns (tasks, n):
        tasks = {task: {"duration": int, "preds": [int, ...]}}
        n     = number of real tasks (tasks are numbered 1..n)
    Example: the line "4 4 1 2" gives tasks[4] = {"duration": 4, "preds": [1, 2]}
    """
    raise NotImplementedError("read_table — Member 1, issue #2")


def display_constraint_table(tasks):
    """Print the constraint table read from the file (task, duration, predecessors)."""
    raise NotImplementedError("display_constraint_table — Member 1, issue #2")
