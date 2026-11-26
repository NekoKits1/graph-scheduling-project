# main.py — Nancy (issue #2) · checked by Audrey
# The loop from the subject's pseudo-code: choose a table in tables/, run every step,
# then ask for another table, without restarting the program.
#
# Must also support:  python main.py --all   (runs every table, used by the CI)
# Wrap each run in recording(path) from trace.py so traces/ gets one file per table.
# Uses only the shared functions listed in the README, section 4.

import contextlib
import importlib
import os
import sys
import traceback

from reader import read_table, display_constraint_table

TABLES_DIR = "tables"


def list_tables():
    """Return sorted list of .txt files in the tables directory."""
    if not os.path.isdir(TABLES_DIR):
        return []
    return sorted(f for f in os.listdir(TABLES_DIR) if f.endswith(".txt"))


def choose_table():
    """Display a menu and return the chosen table path, or None to quit."""
    tables = list_tables()
    if not tables:
        print("No tables found in tables/.")
        return None
    print("\nAvailable tables:")
    for i, name in enumerate(tables, 1):
        print(f"  {i}. {name}")
    print("  0. Quit")
    while True:
        try:
            choice = input("\nYour choice: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(tables):
            return os.path.join(TABLES_DIR, tables[int(choice) - 1])
        print("Invalid choice, try again.")


def load(module_name, *names):
    """Return the named functions of a module, or None if one is not written yet."""
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None
    functions = [getattr(module, name, None) for name in names]
    if any(f is None for f in functions):
        return None
    return functions


def not_ready(step):
    """Say which step is not written yet; the table stops there."""
    print(f"\n[{step} is not written yet: stopping here for this table.]")


def run_one_table(path):
    """Run every step of the scheduling analysis on one table, in order."""
    print(f"\n{'=' * 50}")
    print(f"Table: {path}")
    print(f"{'=' * 50}")

    # Step 1 — Read and display the constraint table
    try:
        tasks, n = read_table(path)
    except (OSError, ValueError, IndexError) as error:
        print(f"Cannot read this table: {error}")
        return
    display_constraint_table(tasks)

    # Step 2 — Graph with 0 and n+1, edge list, value matrix
    graph = load("graph", "build_edges", "display_edges", "build_matrix", "display_matrix")
    if graph is None:
        return not_ready("Step 2 (graph.py)")
    build_edges, display_edges, build_matrix, display_matrix = graph
    edges = build_edges(tasks, n)
    display_edges(edges, n)
    matrix = build_matrix(edges, n)
    display_matrix(matrix)

    # Step 3 — Scheduling-graph properties
    checks = load("checks", "is_scheduling_graph")
    if checks is None:
        return not_ready("Step 3 (checks.py)")
    (is_scheduling_graph,) = checks
    if not is_scheduling_graph(matrix):
        print("\nThis is not a valid scheduling graph: no ranks or calendars for this table.")
        return

    # Steps 4 and 5 — Ranks, earliest and latest dates, floats
    calendar = load("calendar_calc", "compute_ranks", "earliest_dates", "latest_dates", "compute_floats")
    if calendar is None:
        return not_ready("Steps 4-5 (calendar_calc.py)")
    compute_ranks, earliest_dates, latest_dates, compute_floats = calendar
    ranks = compute_ranks(matrix)
    if ranks is None:
        print("\nCycle detected: ranks cannot be computed.")
        return
    earliest = earliest_dates(matrix, ranks)
    latest = latest_dates(matrix, ranks, earliest)
    floats = compute_floats(earliest, latest)

    # Step 6 — Results table and critical path(s)
    critical = load("critical", "critical_paths", "display_results")
    if critical is None:
        return not_ready("Step 6 (critical.py)")
    critical_paths, display_results = critical
    display_results(tasks, ranks, earliest, latest, floats)
    critical_paths(matrix, earliest, floats)


def run_and_record(path):
    """Run one table inside recording(path) once trace.py provides it."""
    trace = load("trace", "recording")
    context = trace[0](path) if trace else contextlib.nullcontext()
    with context:
        run_one_table(path)


def main():
    """Main loop: choose a table, run it, ask for another."""
    if "--all" in sys.argv:
        # Used by the CI: no menu, and any real error stops the program so the CI turns red.
        tables = list_tables()
        if not tables:
            print("No tables found in tables/.")
            return
        for name in tables:
            run_and_record(os.path.join(TABLES_DIR, name))
        return

    while True:
        path = choose_table()
        if path is None:
            print("Goodbye!")
            break
        try:
            run_and_record(path)
        except Exception:
            print("\nUnexpected error on this table (details below). Back to the menu.")
            traceback.print_exc()


if __name__ == "__main__":
    main()
