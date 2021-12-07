# from __future__ import division
import numpy as np

def main():
    input_file = "input.txt"
    coord_pairs = []
    max_x = 0
    max_y = 0
    
    # Using readlines()
    file = open(input_file, 'r')
    for line in file.readlines():
        coords = [coord.split(",") for coord in line.strip().split(" -> ")]
        for coord in coords:
            max_x = max(max_x, int(coord[0]))
            max_y = max(max_y, int(coord[1]))
        coord_pairs.append(coords)
    
    coords_map = np.zeros((max_y+2)*(max_x+2)).reshape(max_y+2,max_x+2)

    # Map lines from coordinate pairs
    for pair in coord_pairs:
        direction = 1
        # Only check straight lines for now
        if pair[0][0] == pair[1][0]:
            x = int(pair[0][0])
            y_start = int(pair[0][1])
            line_len = int(pair[1][1]) - int(pair[0][1])
            if (line_len < 0):
                direction = -1
            for i in range(abs(line_len)+1):
                coords_map[x][y_start+(i*direction)]+=1
        elif pair[0][1] == pair[1][1]:
            y = int(pair[0][1])
            x_start = int(pair[0][0])
            line_len = int(pair[1][0]) - int(pair[0][0])
            if (line_len < 0):
                direction = -1
            for i in range(abs(line_len)+1):
                coords_map[x_start+(i*direction)][y]+=1

    print(np.count_nonzero(coords_map >= 2))


if __name__ == '__main__':
    main()