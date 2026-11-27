# checks.py — Audrey (issue #4) · checked by Kirolos
# One entry point, one exit point, no cycle, then the final verdict.
#
# Functions to write — shared names, do not rename them (README, section 4):
#   eliminate_entry_points(matrix, show_trace) -> rounds, remaining
#       (prints each round when show_trace is True; also used by compute_ranks)
#   is_scheduling_graph(matrix)  -> True / False
#       (uses check_weights from graph.py; must never crash, even with a cycle)

from graph import predecessors, successors, check_weights

def format_vertices(vertices):
    """Return the vertices as '1 2 3', or 'None' when the list is empty."""
    return " ".join(str(v) for v in vertices) if vertices else "None"

def entry_points(matrix):
    """Return the vertices with no incoming edge (empty column)."""
    result=[]
    for v in range(len(matrix)):
        if not(predecessors(matrix, v)):
            result.append(v)
    return result

def exit_points(matrix):
    """Return the vertices with no outgoing edge (empty row)."""
    result=[]
    for v in range(len(matrix)):
        if not(successors(matrix,v)):
            result.append(v)
    return result

def eliminate_entry_points(matrix, show_trace):
    """Remove the entry points round by round; return rounds and the vertices left."""
    remaining = list(range(len(matrix)))
    rounds = []
    if show_trace:
        print("* Method of eliminating entry points")
    while remaining:
        # Entry point of this round = a remaining vertex whose predecessors are all removed.
        entries = []
        for v in remaining:
            if not any(u in remaining for u in predecessors(matrix, v)):
                entries.append(v)
        if not entries:
            break  # vertices are left but none can be removed: they wait on a cycle
        rounds.append(entries)
        remaining = [v for v in remaining if v not in entries]
        if show_trace:
            print(f"Entry points: {format_vertices(entries)}")
            print("Eliminating entry points")
            print(f"Remaining vertices: {format_vertices(remaining)}")
    if show_trace:
        if remaining:
            print(f"-> No entry point left among {format_vertices(remaining)}: there is a cycle")
        else:
            print("-> There is no cycle")
    return rounds, remaining


def is_scheduling_graph(matrix):
    """Check the six properties of a scheduling graph; print each one and the verdict."""
    print("\n* Checking the scheduling-graph properties")
    last = len(matrix) - 1  # vertex N+1 (omega)

    entries = entry_points(matrix)
    one_entry = entries == [0]
    if one_entry:
        print("There is one entry point, 0")
    else:
        print(f"Entry points: {format_vertices(entries)} -> there must be exactly one, 0")

    exits = exit_points(matrix)
    one_exit = exits == [last]
    if one_exit:
        print(f"There is one exit point, {last}")
    else:
        print(f"Exit points: {format_vertices(exits)} -> there must be exactly one, {last}")

    print("* Detecting a cycle")
    _, remaining = eliminate_entry_points(matrix, True)
    no_cycle = not remaining

    weights_ok = check_weights(matrix)

    valid = one_entry and one_exit and no_cycle and weights_ok
    if valid:
        print("-> This is a scheduling graph")
    else:
        failed = [name for name, ok in [("single entry point", one_entry),
                                        ("single exit point", one_exit),
                                        ("no cycle", no_cycle),
                                        ("weights", weights_ok)] if not ok]
        print(f"-> This is NOT a scheduling graph (failed: {', '.join(failed)})")
    return valid