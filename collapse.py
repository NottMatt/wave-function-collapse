#!/bin/python3
import sys

def main():
    # validate and parse arguments
    grid_x = int(sys.argv[1])
    grid_y = int(sys.argv[2])
    cell_file = sys.argv[3]

    print("grid dimensions:     %d by %d" % (grid_x, grid_y))
    print("cell file:           %s" % (cell_file))


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
    cell_dimensions_str = f_content.split("{")[0].split("\n")[0].split(" ")[1].split("x")

    cell_x = int(cell_dimensions_str[0])
    cell_y = int(cell_dimensions_str[1])

    cell_dimensions = [cell_x, cell_y]

    # for i in range(y * cell_y):
    #     for j in range(x * cell_x):
    #         print("[]", end='')
    #     print('')

    
    # divide into cells

    cells = f_content.split("{")[1:]

    for i in range(len(cells)):
        cells[i] = cells[i].split("}")[0].split(";")

    cell_structures = {}

    for i in range(len(cells)):
        cell_structures[cells[i][0].replace("\n", "")] = cells[i][1].replace("\n", "")

    
    for i in range(cell_y):
        for j in range(cell_x):
            print(cell_structures["six"][j + (i * cell_x)], end='')
        print("")

    # create dictionary cell_structures
        # identifier:
            # [
            #   <cell structure> 
            # ]


    cell_connections = {}

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