# tables/
Our constraint tables (.txt), then the teacher's official ones. Owner: Nancy (issue #2) — every member adds two tables of their own.

- Name them `table_NN_short-description.txt` so they appear in order in the menu.
- One line per task: `task duration predecessors...`
- For each table, write the expected results by hand (ranks, dates, critical path) before trusting the program.

| File | What it tests | Expected |
|---|---|---|
| `table_01_subject_example.txt` | The subject's example (Google Doc, section 2) | Valid; critical path 0 → 2 → 4 → 5 → 6, length 11 |
| `table_02_cycle.txt` | A cycle 1 → 2 → 3 → 1 | Not a scheduling graph, no ranks |

### The teacher's tables (received 17 Nov)

`table_T01_teacher.txt` to `table_T14_teacher.txt` are the official files, **copied byte for byte**: Windows line endings (`\r\n`), spaces at the end of lines, an empty first line in T13, no final newline in T13 and T14. `read_table` must accept all of that. The teacher will give more files like these on the day of the defense.

| File | N | Expected |
|---|---|---|
| `table_T01_teacher.txt` | 13 | **Cycle** (4 → 5 → 6 → 13 → 4): not a scheduling graph, no ranks |
| `table_T02_teacher.txt` | 13 | Valid |
| `table_T03_teacher.txt` | 12 | Valid |
| `table_T04_teacher.txt` | 11 | Valid |
| `table_T05_teacher.txt` | 13 | Valid |
| `table_T06_teacher.txt` | 12 | Valid |
| `table_T07_teacher.txt` | 10 | Valid |
| `table_T08_teacher.txt` | 10 | Valid |
| `table_T09_teacher.txt` | 10 | Valid |
| `table_T10_teacher.txt` | 8 | Valid |
| `table_T11_teacher.txt` | 8 | Valid (task 8 lasts **0**) |
| `table_T12_teacher.txt` | 12 | **Cycle** (3 → 9 → 10 → 3): not a scheduling graph, no ranks |
| `table_T13_teacher.txt` | 4 | Valid (empty first line, no final newline) |
| `table_T14_teacher.txt` | 4 | Valid (no final newline) |

Ranks, dates and critical paths: to be solved by hand and added here as we go.

| File | Author | What it tests | Expected |
|---|---|---|---|
| `table_01_subject_example.txt` | — | The subject's example (Google Doc, section 2) | Valid; critical path 0 → 2 → 4 → 5 → 6, length 11 |
| `table_02_cycle.txt` | — | A cycle 1 → 2 → 3 → 1, every task in it | Not a scheduling graph: 0 and N+1 are both entry and exit points, and there is a cycle; no ranks |
| `table_03_cycle_middle.txt` | Audrey | A cycle in the middle: tasks 2 and 3 wait for each other | Not a scheduling graph (cycle); no ranks |
| `table_04_two_chains.txt` | Audrey | Two separate chains 1 → 3 and 2 → 4, joined by 0 and 5 | Valid; critical path 0 → 2 → 4 → 5, length 5 |
| `kirolos_large.txt` | Kirolos | 12 tasks (two-digit vertices, aligned matrix), two parallel branches | Valid; length 12, **two** critical paths |
| `kirolos_negative.txt` | Kirolos | A task with a negative duration (task 2 lasts −2) | Not a scheduling graph: "no negative edge" fails; no ranks |
| `kirolos_unknown_predecessor.txt` | Kirolos | Task 2 waits for task 9, which is not in the table (issue #15) | Refused right after reading: "Task 2 has predecessor 9, which is not in the table"; no crash, back to the menu |

**Full hand-calculated results** (edges, matrix, elimination rounds, E / L / floats, critical paths): `kirolos_expected.md` for Kirolos's tables, `audrey_expected.md` for Audrey's tables. Each member adds their own `firstname_expected.md` for their two tables.
