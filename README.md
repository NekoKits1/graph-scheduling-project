# Graph Theory Project — Scheduling

EFREI I2 NEW 2026/2027 · Team of 5 · Python (standard library only)
**Defense: Fri 4 Dec 2026** — 10 min demo + 20 min questions. Program files on Moodle before the defense.

The program reads a constraint table (.txt), builds the scheduling graph and its value matrix, checks that it is a valid scheduling graph, then computes the ranks, earliest and latest dates, floats and critical path(s). It loops so we can test several tables without restarting.

> This README is for the team: how the repo works and the names we all use.
> The full explanation of the project, with a worked example, is in our Google Doc (team plan).

> ⚠️ **Shared names — read section 4 before writing any code.**
> Our files call each other's functions and pass the same data around. Use **exactly** the names and data formats of section 4: don't rename, don't change a format, don't add your own version. Need a new shared name? Ask the group first, then add it to section 4.

---

## 1. Run it

```bash
python main.py                          # menu: pick a table, then another one…
python main.py --all                    # run every table in tables/ (used by the CI)
python -m unittest discover -s tests -v # automatic tests
```

No installation needed: Python 3.10+ only.

---

## 2. Team

| Member | Codes | Files | Checks | Issue |
|---|---|---|---|---|
| Member 1 | Reading a table and displaying it; the menu loop and `--all` | `reader.py`, `main.py` | Member 2 | #2 |
| Member 2 | Edges with 0 and N+1, value matrix, their display, predecessors / successors | `graph.py` | Member 3 | #3 |
| Member 3 | The six properties, elimination of entry points (cycle detection) | `checks.py` | Member 4 | #4 |
| Member 4 | Ranks, earliest and latest dates, floats; saving each run in `traces/` | `calendar_calc.py`, `trace.py` | Member 5 | #5 |
| Member 5 | All critical paths, the final results table | `critical.py` | Member 1 | #6 |

Everyone also adds **two tables** of their own to `tables/` (with results solved by hand) and writes the **tests of their own file** in `tests/`. The checker uses the checklist of that part in the Google Doc (section 6) before approving.

Replace "Member N" with our names.

---

## 3. How the repo is organised

```
graph-scheduling-project/
├── main.py            → the menu loop (Member 1)
├── reader.py          → read a .txt table, display it (Member 1)
├── graph.py           → edges, value matrix, predecessors / successors (Member 2)
├── checks.py          → the six properties, elimination of entry points (Member 3)
├── calendar_calc.py   → ranks, earliest and latest dates, floats (Member 4)
├── trace.py           → recording(path): saves each run in traces/ (Member 4)
├── critical.py        → critical paths, final results table (Member 5)
├── tables/            → our .txt tables, then the teacher's
├── traces/            → saved outputs for Moodle
├── tests/             → automatic tests (the hand-solved example)
└── .github/           → CI and pull request template
```

Each file starts with a short comment: who codes it, its issue, and the functions to write with their shared names. The code is ours to write.

---

## 4. Shared names (everyone uses exactly these)

### Data

| Name | Type | Example (subject's table) |
|---|---|---|
| `tasks` | `dict {task: {"duration": int, "preds": [int]}}` | `{4: {"duration": 4, "preds": [1, 2]}}` |
| `n` | `int` — number of real tasks; vertices go from `0` to `n + 1` | `5` |
| `edges` | `list` of tuples `(start, end, weight)` | `[(0, 1, 0), (1, 3, 1), …]` |
| `matrix` | `list` of `n + 2` lists of `n + 2` cells; `None` = no edge (printed `*`) | `matrix[2][4] == 2` |
| `rounds`, `remaining` | `rounds`: list of lists, the vertices removed at each round; `remaining`: vertices left at the end (`[]` = no cycle) | `[[0], [1, 2], [3, 4], [5], [6]]`, `[]` |
| `ranks` | `dict {vertex: rank}`, or `None` if there is a cycle | `{5: 3}` |
| `earliest`, `latest`, `floats` | `dict {vertex: int}` | `earliest[5] == 6` |
| `critical_paths` | `list` of lists of vertices | `[[0, 2, 4, 5, 6]]` |

### Functions

| Function | Returns | File |
|---|---|---|
| `read_table(path)` | `tasks, n` | `reader.py` |
| `display_constraint_table(tasks)` | — (prints) | `reader.py` |
| `build_edges(tasks, n)` | `edges` | `graph.py` |
| `display_edges(edges, n)` | — (prints) | `graph.py` |
| `build_matrix(edges, n)` | `matrix` | `graph.py` |
| `display_matrix(matrix)` | — (prints) | `graph.py` |
| `predecessors(matrix, v)` / `successors(matrix, v)` | list of vertices | `graph.py` |
| `eliminate_entry_points(matrix, show_trace)` | `rounds, remaining` (prints each round if `show_trace`) | `checks.py` |
| `is_scheduling_graph(matrix)` | `True` / `False` (prints each check) | `checks.py` |
| `compute_ranks(matrix)` | `ranks` or `None` (uses `eliminate_entry_points` without printing the rounds again) | `calendar_calc.py` |
| `earliest_dates(matrix, ranks)` | `earliest` (prints) | `calendar_calc.py` |
| `latest_dates(matrix, ranks, earliest)` | `latest` (prints) | `calendar_calc.py` |
| `compute_floats(earliest, latest)` | `floats` (prints) | `calendar_calc.py` |
| `critical_paths(matrix, earliest, floats)` | `critical_paths` (prints) | `critical.py` |
| `display_results(tasks, ranks, earliest, latest, floats)` | — (prints one aligned table: vertex, duration, rank, E, L, float) | `critical.py` |
| `recording(table_path)` | used as `with recording(path):` — shows everything on screen and saves the same text in `traces/` | `trace.py` |

**Rule:** computing functions **return** their result and **print** the trace the subject asks for. Need a new shared function or name? Tell the group first, then add it here.

---

## 5. Writing rules

| What | Rule | Example |
|---|---|---|
| Functions and variables | `snake_case`, in English, clear names | `compute_ranks`, `entry_points` |
| Functions | start with a verb | `build_matrix()`, `display_edges()` |
| Constants | `UPPER_SNAKE_CASE` | `TABLES_DIR` |
| Each function | one-line docstring saying what it does | `"""Return the list of successors of v."""` |
| No edge in the matrix | `None` in memory, `*` on screen | |
| Vertices | integers: `0` = start (α), `n + 1` = end (ω) | |

---

## 6. How we work with Git

- `main` always works and is protected: code arrives only through a **pull request approved by the checker**, with the CI passing.
- One short branch per task, from the latest `main`, named `firstname/task`: `nancy/value-matrix`, `amine/checks`. Deleted after merge.
- Commit messages: `type(file): what changed` — `feat(graph): build value matrix`, `fix(checks): detect cycle on disconnected graph`, `test: add table with N = 12`.

**For each task**

1. Take your issue on the board, move it to *In progress*.
2. `git checkout main && git pull`, then `git checkout -b firstname/task`.
3. Code in your own file. Run `python -m unittest discover -s tests -v`: your file's tests must pass.
4. `git push -u origin firstname/task`, open a pull request with `Closes #n`, add your checker as reviewer.
5. The checker runs `python main.py` on a few tables, reads the code, makes sure they can explain it, approves and merges.

**CI (GitHub Actions)** runs on every pull request: checks every file compiles, runs our tests, then `python main.py --all` on every table. If it is red, the pull request can't be merged.

---

## 7. Tests

- Each member writes the tests for their file in `tests/` (see `tests/README.md`), using the hand-solved example of the Google Doc (section 2) as expected results.
- Every new table in `tables/` comes with its expected results written by hand (see `tables/README.md`).
