# tables/
Our constraint tables (.txt), then the teacher's official ones. Owner: Nancy (issue #2) — every member adds two tables of their own.

- Name them `table_NN_short-description.txt` so they appear in order in the menu.
- One line per task: `task duration predecessors...`
- For each table, write the expected results by hand (ranks, dates, critical path) before trusting the program.

| File | What it tests | Expected |
|---|---|---|
| `table_01_subject_example.txt` | The subject's example (Google Doc, section 2) | Valid; critical path 0 → 2 → 4 → 5 → 6, length 11 |
| `table_02_cycle.txt` | A cycle 1 → 2 → 3 → 1 | Not a scheduling graph, no ranks |
