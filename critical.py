"""Floats and critical paths.

Owner: Member 5 — issue #6. Checked by: Member 1.
Shared names: README, section 4.
"""


def compute_floats(earliest, latest):
    """Return {vertex: total float} with float = latest - earliest. Print them."""
    raise NotImplementedError("compute_floats — Member 5, issue #6")


def critical_paths(matrix, earliest, floats):
    """Return every critical path as a list of vertices from 0 to n + 1. Print them.

    A critical path uses only vertices with float 0 and edges u -> v where E(u) + weight = E(v).
    """
    raise NotImplementedError("critical_paths — Member 5, issue #6")
