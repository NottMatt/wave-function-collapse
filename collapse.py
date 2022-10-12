#!/bin/python3
from calendar import c
import sys

def main():
    # validate and parse arguments
    grid_x = int(sys.argv[1])
    grid_y = int(sys.argv[2])
    cell_file = sys.argv[3]

    print("grid dimensions:     %d by %d" % (grid_x, grid_y))
    print("cell file:           %s" % (cell_file))

    for i in range(grid_y):
        for j in range(grid_x):
            print("[]", end='')
        print('')

    # parse cells from file
    # cell_dimensions,cell_structures,cell_connections = parse_cells(grid_x, grid_y, cell_file)
    parse_cells(grid_x, grid_y, cell_file)
    # generate cell_grid (input x by input y)

    # populate grid with cell identifiers based on entropy calculations

    # generate print_grid ((input x * cell x) by (input y * cell y))

    # populate print_grid based on cell identifiers in cell_grid

def parse_cells(x, y, cfile):
    # open file
    f = open(cfile, 'r')
    
    # get cell dimensions
    f_content = f.read()
    cell_dimensions = f_content.split("{")[0].split("\n")[0].split(" ")[1].split("x")

    cell_x = int(cell_dimensions[0])
    cell_y = int(cell_dimensions[1])

    for i in range(y * cell_y):
        for j in range(x * cell_x):
            print("[]", end='')
        print('')
    

    # create dictionary cell_structures
        # identifier:
            # [
            #   <cell structure> 
            # ]

    # create dictionary cell_connections
        # identifier:
            # [
            #   {up     :   [ids]}
            #   {left   :   [ids]}
            #   {down   :   [ids]}
            #   {rigt   :   [ids]}
            # ]


    print("")
    


main()