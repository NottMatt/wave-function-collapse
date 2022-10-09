# Wave Function Collapse

## Arguments

The main python program takes in the **dimensions** for the desired grid and the **cell file** that enumerates the cells and valid connections.

```
python3 collapse.py <columns> <rows> <cell-file>.cell
```

## Dimensions

The grid is generated based on the dimension arguments, first the columns in the **x-axis** and the rows in the **y-axis**.
```
2 2  [][]      4 2  [][][][]      2 4  [][]      4 4  [][][][]
     [][]           [][][][]           [][]           [][][][]
                                       [][]           [][][][]
                                       [][]           [][][][]
```

## Cell File

The program takes a file with the extension "*.cell*".
```
maze.cell
```
This file describes the size of the cell at the beginning of the file.
```
CELL 4x4
```
The rest of the file will enumerate the cells and then list that cells viable connections on orthogonal sides.
The blocks describing the cells containt:
 - with a unique identifier (name or number, unique string)
 - the cell itself
 - valid cells for **up** direction
 - valid cells for **left** direction
 - valid cells for **down** direction
 - valid cells for **right** directions
```
{
foo_c
;
0110
1001
1001
0110
;
foo_u1
foo_u2
;
foo_l1
foo_l2
;
foo_d1
foo_d2
;
foo_r1
foo_r2
}
```