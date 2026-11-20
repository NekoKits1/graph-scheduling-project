# graph.py — Kirolos (issue #3) · checked by Lea
# Builds the scheduling graph (with vertices 0 and n+1), its value matrix,
# and checks the edge weights.
#
# Functions to write — shared names, do not rename them (README, section 4):
#   build_edges(tasks, n)      -> edges
#   display_edges(edges, n)    -> prints vertices, edges, one line "A -> B = w"
#   build_matrix(edges, n)     -> matrix
#   display_matrix(matrix)     -> prints the aligned matrix (also for n >= 10)
#   predecessors(matrix, v) / successors(matrix, v) -> list of vertices
#   check_weights(matrix)      -> True / False (same weight leaving a vertex,
#                                 edges from 0 weigh 0, no negative edge)
# Merge build_matrix, predecessors and successors first: Audrey, Lea and Mayer use them.
