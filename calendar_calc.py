# calendar_calc.py — Lea (issue #5) · checked by Mayer
# Ranks, earliest dates, latest dates and floats, each with its trace.
#
# Functions to write — shared names, do not rename them (README, section 4):
#   compute_ranks(matrix)                    -> ranks, or None if there is a cycle
#       (uses eliminate_entry_points from checks.py, without printing the rounds again)
#   earliest_dates(matrix, ranks)            -> earliest
#   latest_dates(matrix, ranks, earliest)    -> latest   (L(n+1) = E(n+1))
#   compute_floats(earliest, latest)         -> floats   (L - E)
