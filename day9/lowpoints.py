# from __future__ import division
import numpy as np

directions = ["up", "down", "left", "right"]

def check_adjacent(matrix, max_row, max_col, row, col):
    current = matrix[row, col]
    adjacents = {}
    lowest = True
    for direction in directions:
        if (direction == "up" and row == 0) or (direction == "down" and row == (max_row - 1)) or (direction == "left" and col == 0) or (direction == "right" and col == (max_col - 1)):
            pass
        elif direction == "up":
            if matrix[row-1, col] <= current:
                lowest = False
        elif direction == "down":
            if matrix[row+1, col] <= current:
                lowest = False
        elif direction == "left":
            if matrix[row, col-1] <= current:
                lowest = False
        elif direction == "right":
            if matrix[row, col+1] <= current:
                lowest = False
    return lowest

def main():
    input_file = "input.txt"
    # coord_pairs = []
    max_row = 0
    max_col = 0
    
    # Using readlines()
    file = open(input_file, 'r')
    all_heights = []
    for line in file.readlines():
        heights = [int(height) for height in line.strip()]
        all_heights.append(heights)
        max_row+=1
        max_col=len(heights)

    print(f"Row: {max_row}")
    print(f"Col: {max_col}")

    heights_matrix = np.array(all_heights)

    print("adjacents to [0,0]")
    adjacents = check_adjacent(heights_matrix, max_row, max_col, 0, 0)
    print(adjacents)

    lowests = []

    for row in range(max_row):
        for col in range(max_col):
            lowest = check_adjacent(heights_matrix, max_row, max_col, row, col)
            if lowest:
                print("Lowest [{},{}]: {}".format(row, col, heights_matrix[row,col]))
                lowests.append(heights_matrix[row,col])
    
    lowests = [lowest + 1 for lowest in lowests ]
    print(sum(lowests))
            



    
    
    # for coord in coords:
    #     max_row = max(max_row, int(coord[0]))
    #     max_col = max(max_col, int(coord[1]))
    # coord_pairs.append(coords)
    
    # coords_map = np.zeros((max_col+2)*(max_row+2)).reshape(max_col+2,max_row+2)

    # # Map lines from coordinate pairs
    # for pair in coord_pairs:
    #     direction = 1
    #     # Only check straight lines for now
    #     if pair[0][0] == pair[1][0]:
    #         x = int(pair[0][0])
    #         y_start = int(pair[0][1])
    #         line_len = int(pair[1][1]) - int(pair[0][1])
    #         if (line_len < 0):
    #             direction = -1
    #         for i in range(abs(line_len)+1):
    #             coords_map[x][y_start+(i*direction)]+=1
    #     elif pair[0][1] == pair[1][1]:
    #         y = int(pair[0][1])
    #         x_start = int(pair[0][0])
    #         line_len = int(pair[1][0]) - int(pair[0][0])
    #         if (line_len < 0):
    #             direction = -1
    #         for i in range(abs(line_len)+1):
    #             coords_map[x_start+(i*direction)][y]+=1

    # print(np.count_nonzero(coords_map >= 2))


if __name__ == '__main__':
    main()