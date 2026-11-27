# Hand-calculated results — Audrey

## table_03_cycle_middle.txt

```
1 1
2 2 1 3
3 3 2
4 1 3
```

4 real tasks, 6 vertices, 6 edges. Edges (start, end, weight):

```
0 1 0
1 2 1
2 3 2
3 2 3
3 4 3
4 5 1
```

```
    0  1  2  3  4  5
 0  *  0  *  *  *  *
 1  *  *  1  *  *  *
 2  *  *  *  2  *  *
 3  *  *  3  *  3  *
 4  *  *  *  *  *  1
 5  *  *  *  *  *  *
```

Tasks 2 and 3 wait for each other: cycle 2 → 3 → 2.

## conditions for a valid scheduling graph

- One entry: 0. One exit: 5.
- Elimination of entry points:
    - Round 0: entry points 0 → remaining 1 2 3 4 5
    - Round 1: entry points 1 → remaining 2 3 4 5
    - Round 2: no entry point (2 waits for 3, 3 waits for 2, 4 waits for 3, 5 waits for 4) → **cycle**, remaining 2 3 4 5
- Same outgoing weights: pass (row 3 has 3 and 3). 
- Edges leaving 0 weigh 0: pass. 
- No negative edge: pass.

Final verdict: **not a scheduling graph** (failed: no cycle). No ranks, calendars or critical path.

## table_04_two_chains.txt

```
1 2
2 3
3 1 1
4 2 2
```

4 real tasks, 6 vertices, 6 edges. Two separate chains 1 → 3 and 2 → 4, joined by 0 and 5. Edges (start, end, weight):

```
0 1 0
0 2 0
1 3 2
2 4 3
3 5 1
4 5 2
```

```
    0  1  2  3  4  5
 0  *  0  0  *  *  *
 1  *  *  *  2  *  *
 2  *  *  *  *  3  *
 3  *  *  *  *  *  1
 4  *  *  *  *  *  2
 5  *  *  *  *  *  *
```
## conditions for a valid scheduling graph
- One entry: 0. One exit: 5.
- Elimination rounds: [0], [1, 2], [3, 4], [5] → no cycle.
- Same outgoing weights: pass. 
- Edges leaving 0 weigh 0: pass. 
- No negative edge: pass.

Final verdict: **valid scheduling graph**.

| Vertex | Duration | Rank | E | L | Float |
|---|---:|---:|---:|---:|---:|
|0|0|0|0|0|0|
|1|2|1|0|2|2|
|2|3|1|0|0|0|
|3|1|2|2|4|2|
|4|2|2|3|3|0|
|5|0|3|5|5|0|

Forward calculation: E(3)=0+2=2; E(4)=0+3=3; E(5)=max(2+1, 3+2)=5.

Backward calculation: L(3)=5-1=4; L(4)=5-2=3; L(1)=4-2=2; L(2)=3-3=0; L(0)=min(2-0, 0-0)=0.

Project duration: 5. Critical path:
- 0 → 2 → 4 → 5