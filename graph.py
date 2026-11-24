# Kirolos - Issue #3: edges, value matrix and weight checks.


def build_edges(tasks, n):
    """Build the weighted edges including the fictitious start and end."""
    edges = set()
    used_as_pred = set()
    for task, info in tasks.items():
        if not info['preds']:
            edges.add((0, task, 0))
        for pred in info['preds']:
            edges.add((pred, task, tasks[pred]['duration']))
            used_as_pred.add(pred)
    for task, info in tasks.items():
        if task not in used_as_pred:
            edges.add((task, n + 1, info['duration']))
    return sorted(edges)


def display_edges(edges, n):
    """Print the vertex count, edge count and weighted edges."""
    print(f'Number of vertices: {n + 2}')
    print(f'Number of edges: {len(edges)}')
    for start, end, weight in edges:
        print(f'{start} -> {end} = {weight}')


def build_matrix(edges, n):
    """Build the value matrix with None for absent edges."""
    matrix = [[None for _ in range(n + 2)] for _ in range(n + 2)]
    for start, end, weight in edges:
        matrix[start][end] = weight
    return matrix


def display_matrix(matrix):
    """Print the value matrix with aligned row and column headers."""
    size = len(matrix)
    width = max([1, len(str(size - 1))] + [len(str(w)) for row in matrix for w in row if w is not None])
    print('Value matrix:')
    print(' ' * width + ' ' + ' '.join(f'{v:>{width}}' for v in range(size)))
    for v, row in enumerate(matrix):
        cells = ['*' if w is None else str(w) for w in row]
        print(f'{v:>{width}} ' + ' '.join(f'{cell:>{width}}' for cell in cells))


def predecessors(matrix, v):
    """Return vertices with an edge entering v."""
    return [u for u in range(len(matrix)) if matrix[u][v] is not None]


def successors(matrix, v):
    """Return vertices with an edge leaving v."""
    return [u for u, weight in enumerate(matrix[v]) if weight is not None]


def check_weights(matrix):
    """Print and return the result of the three weight checks."""
    same = all(len({w for w in row if w is not None}) <= 1 for row in matrix)
    start_zero = all(w == 0 for w in matrix[0] if w is not None)
    nonnegative = all(w >= 0 for row in matrix for w in row if w is not None)
    print(f'Same weight on outgoing edges: {"OK" if same else "FAIL"}')
    print(f'Edges leaving 0 weigh 0: {"OK" if start_zero else "FAIL"}')
    print(f'No negative edge: {"OK" if nonnegative else "FAIL"}')
    return same and start_zero and nonnegative
