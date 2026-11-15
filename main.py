"""Main loop: choose a constraint table, run every step, ask to continue.

Owner: Member 5 — issue #6. Checked by: Member 1.
Run:  python main.py         (interactive menu)
      python main.py --all   (runs every table in tables/, used by the CI)
"""

import os
import sys

from reader import read_table, display_constraint_table
from graph import build_edges, display_edges, build_matrix, display_matrix
from checks import is_scheduling_graph
from calendar_calc import compute_ranks, earliest_dates, latest_dates
from critical import compute_floats, critical_paths

TABLES_DIR = "tables"


def list_tables(folder=TABLES_DIR):
    """Return the sorted list of .txt tables in the folder."""
    return sorted(f for f in os.listdir(folder) if f.endswith(".txt"))


def run_table(path):
    """Run every step of the subject's pseudo-code on one table."""
    print(f"\n========== {path} ==========")
    try:
        tasks, n = read_table(path)
        display_constraint_table(tasks)

        edges = build_edges(tasks, n)
        display_edges(edges, n)
        matrix = build_matrix(edges, n)
        display_matrix(matrix)

        if not is_scheduling_graph(matrix):
            print("-> Not a scheduling graph: no ranks or calendars for this table.")
            return

        ranks = compute_ranks(matrix)
        if ranks is None:
            print("-> Cycle detected: ranks are not displayed.")
            return
        earliest = earliest_dates(matrix, ranks)
        latest = latest_dates(matrix, ranks, earliest)
        floats = compute_floats(earliest, latest)
        critical_paths(matrix, earliest, floats)
    except NotImplementedError as missing:
        print(f"[not written yet] {missing}")


def main():
    tables = list_tables()
    if "--all" in sys.argv:
        for name in tables:
            run_table(os.path.join(TABLES_DIR, name))
        return

    # TODO Member 5 (issue #6): save each run to traces/, nicer menu.
    while True:
        print("\nAvailable tables:")
        for i, name in enumerate(tables, start=1):
            print(f"  {i}. {name}")
        choice = input("Table number (or q to quit): ").strip()
        if choice.lower() == "q":
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(tables):
            print("Please type a number from the list.")
            continue
        run_table(os.path.join(TABLES_DIR, tables[int(choice) - 1]))


if __name__ == "__main__":
    main()
