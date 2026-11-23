# Hand-calculated results — Kirolos

## kirolos_large.txt

12 real tasks, 14 vertices, 15 edges. Edges (start, end, weight):

```
0 1 0
0 2 0
1 3 2
2 4 2
3 5 1
4 5 1
5 6 2
6 7 0
6 8 0
7 9 3
8 10 1
9 11 1
10 11 1
11 12 2
12 13 1
```

All other matrix cells are None. All six scheduling checks pass.

| Vertex | Duration | Rank | E | L | Float |
|---|---:|---:|---:|---:|---:|
|0|0|0|0|0|0|
|1|2|1|0|0|0|
|2|2|1|0|0|0|
|3|1|2|2|2|0|
|4|1|2|2|2|0|
|5|2|3|3|3|0|
|6|0|4|5|5|0|
|7|3|5|5|5|0|
|8|1|5|5|7|2|
|9|1|6|8|8|0|
|10|1|6|6|8|2|
|11|2|7|9|9|0|
|12|1|8|11|11|0|
|13|0|9|12|12|0|

Forward calculation: E(5)=max(2+1,2+1)=3; E(11)=max(8+1,6+1)=9; E(13)=11+1=12.
Backward calculation: L(11)=11-2=9; L(9)=L(10)=9-1=8; L(7)=8-3=5; L(8)=8-1=7; L(6)=min(5-0,7-0)=5.

Project duration: 12. Critical paths:
- 0 → 1 → 3 → 5 → 6 → 7 → 9 → 11 → 12 → 13
- 0 → 2 → 4 → 5 → 6 → 7 → 9 → 11 → 12 → 13

## kirolos_negative.txt

3 real tasks, 5 vertices, 4 edges: (0,1,0), (1,2,3), (2,3,-2), (3,4,4).

```
    0  1  2  3  4
 0  *  0  *  *  *
 1  *  *  3  *  *
 2  *  *  * -2  *
 3  *  *  *  *  4
 4  *  *  *  *  *
```

One entry: 0. One exit: 4. No cycle (elimination rounds: [0], [1], [2], [3], [4]). Same outgoing weights: pass. Start weights zero: pass. No negative edge: fail because 2 → 3 weighs -2. Final verdict: invalid scheduling graph. Do not compute calendar or critical paths.
