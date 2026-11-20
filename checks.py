# checks.py — Audrey (issue #4) · checked by Kirolos
# One entry point, one exit point, no cycle, then the final verdict.
#
# Functions to write — shared names, do not rename them (README, section 4):
#   eliminate_entry_points(matrix, show_trace) -> rounds, remaining
#       (prints each round when show_trace is True; also used by compute_ranks)
#   is_scheduling_graph(matrix)  -> True / False
#       (uses check_weights from graph.py; must never crash, even with a cycle)
