"""Building the scheduling graph: edges and value matrix.

Owner: Member 2 — issue #3. Checked by: Member 3.
Shared names: README, section 4.
Vertices go from 0 (fictitious start, alpha) to n + 1 (fictitious end, omega).
"""


def build_edges(tasks, n):
    """Return the list of edges (start, end, weight), including vertices 0 and n + 1.

    - Task with no predecessor: edge 0 -> task, weight 0.
    - Task B needs task A: edge A -> B, weight = duration of A.
    - Task that is nobody's predecessor: edge task -> n + 1, weight = its duration.
    """
    raise NotImplementedError("build_edges — Member 2, issue #3")


def display_edges(edges, n):
    """Print the number of vertices, the number of edges, then one line per edge: 'A -> B = w'."""
    raise NotImplementedError("display_edges — Member 2, issue #3")


def build_matrix(edges, n):
    """Return the value matrix: a list of (n + 2) lists of (n + 2) cells.

    matrix[i][j] = weight of edge i -> j, or None if there is no edge.
    """
    raise NotImplementedError("build_matrix — Member 2, issue #3")


def display_matrix(matrix):
    """Print the value matrix from memory: '*' for None, aligned columns, row and column headers."""
    raise NotImplementedError("display_matrix — Member 2, issue #3")


def predecessors(matrix, v):
    """Return the list of vertices u with an edge u -> v."""
    raise NotImplementedError("predecessors — Member 2, issue #3")


def successors(matrix, v):
    """Return the list of vertices w with an edge v -> w."""
    raise NotImplementedError("successors — Member 2, issue #3")
