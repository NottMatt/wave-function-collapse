#!/bin/python3
import sys

def main():
    for arg in sys.argv:
        print(arg)

    grid_x = int(sys.argv[1])
    grid_y = int(sys.argv[2])
    cell_file = sys.argv[3]
    # validate and parse arguments

    # parse cells from file
    parse_cells(grid_x, grid_y, cell_file)
    # generate cell_grid (input x by input y)

    # populate grid with cell identifiers based on entropy calculations

    # generate print_grid ((input x * cell x) by (input y * cell y))

    # populate print_grid based on cell identifiers in cell_grid

def parse_cells(x, y, cfile):
    for i in range(y):
        for j in range(x):
            print("[]", end='')
        print('')

main()