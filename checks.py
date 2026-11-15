"""Checking that the graph is a valid scheduling graph.

Owner: Member 3 — issue #4. Checked by: Member 4.
Shared names: README, section 4.
"""


def is_scheduling_graph(matrix):
    """Check the six properties, printing a trace for each one, then the verdict.

    1. a single entry point      2. a single exit point
    3. no cycle (method of eliminating entry points, print each round)
    4. same weight on all edges leaving a vertex
    5. edges leaving the entry point weigh 0      6. no negative edge
    Returns True if all properties hold, False otherwise. Must never crash.
    """
    raise NotImplementedError("is_scheduling_graph — Member 3, issue #4")
