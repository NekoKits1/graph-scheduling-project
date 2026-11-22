# main.py — Nancy (issue #2) · checked by Audrey
# The loop from the subject's pseudo-code: choose a table in tables/, run every step,
# then ask for another table, without restarting the program.
#
# Must also support:  python main.py --all   (runs every table, used by the CI)
# Wrap each run in recording(path) from trace.py so traces/ gets one file per table.
# Uses only the shared functions listed in the README, section 4.

import os
import sys

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
    print(f"  0. Quit")
    while True:
        choice = input("\nYour choice: ").strip()
        if choice == "0":
            return None
        try:
            index = int(choice)
            if 1 <= index <= len(tables):
                return os.path.join(TABLES_DIR, tables[index - 1])
        except ValueError:
            pass
        print("Invalid choice, try again.")


def run_one_table(path):
    """Run every step of the scheduling analysis on one table."""
    from reader import read_table, display_constraint_table

    print(f"\n{'=' * 50}")
    print(f"Table: {path}")
    print(f"{'=' * 50}")

    # Step 1 — Read and display the constraint table
    try:
        tasks, n = read_table(path)
    except Exception as e:
        print(f"Error reading table: {e}")
        return
    display_constraint_table(tasks)

    # Steps 2–6 — Graph, checks, ranks, calendars, critical paths
    try:
        from graph import build_edges, display_edges, build_matrix, display_matrix
        from checks import is_scheduling_graph
        from calendar_calc import compute_ranks, earliest_dates, latest_dates, compute_floats
        from critical import critical_paths, display_results

        edges = build_edges(tasks, n)
        display_edges(edges, n)
        matrix = build_matrix(edges, n)
        display_matrix(matrix)

        if not is_scheduling_graph(matrix):
            print("This is not a valid scheduling graph.")
            return

        ranks = compute_ranks(matrix)
        if ranks is None:
            print("Cycle detected, cannot compute ranks.")
            return

        earliest = earliest_dates(matrix, ranks)
        latest = latest_dates(matrix, ranks, earliest)
        floats = compute_floats(earliest, latest)
        paths = critical_paths(matrix, earliest, floats)
        display_results(tasks, ranks, earliest, latest, floats)

    except ImportError:
        print("Some modules are not ready yet.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main loop: choose a table, run it, ask for another."""
    all_mode = "--all" in sys.argv

    if all_mode:
        tables = list_tables()
        if not tables:
            print("No tables found in tables/.")
            return
        for name in tables:
            path = os.path.join(TABLES_DIR, name)
            run_one_table(path)
    else:
        while True:
            path = choose_table()
            if path is None:
                print("Goodbye!")
                break
            run_one_table(path)
            print()


if __name__ == "__main__":
    main()