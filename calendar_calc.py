"""Ranks, earliest dates and latest dates.

Owner: Member 4 — issue #5. Checked by: Member 5.
Shared names: README, section 4.
"""


def compute_ranks(matrix):
    """Return {vertex: rank} using the method of eliminating entry points, or None if there is a cycle.

    Print each round (entry points removed, remaining vertices), then the ranks.
    """
    raise NotImplementedError("compute_ranks — Member 4, issue #5")


def earliest_dates(matrix, ranks):
    """Return {vertex: earliest date}. Go up the ranks: E(0) = 0, E(v) = max(E(u) + weight(u -> v)). Print them."""
    raise NotImplementedError("earliest_dates — Member 4, issue #5")


def latest_dates(matrix, ranks, earliest):
    """Return {vertex: latest date}. Go down the ranks: L(n+1) = E(n+1), L(u) = min(L(v) - weight(u -> v)). Print them."""
    raise NotImplementedError("latest_dates — Member 4, issue #5")
