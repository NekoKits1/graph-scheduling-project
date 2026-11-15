# tests/
Automatic tests (Python `unittest`), one file per module: `test_reader.py`, `test_graph.py`… Each member writes the tests for their file.

Use the hand-solved example (Google Doc, section 2) as expected results:
ranks `{0:0, 1:1, 2:1, 3:2, 4:2, 5:3, 6:4}` · earliest `{…, 5:6, 6:11}` · critical path `[[0, 2, 4, 5, 6]]`.

Run them with: `python -m unittest discover -s tests -v`
