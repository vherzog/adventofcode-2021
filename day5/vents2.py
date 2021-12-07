# from __future__ import division
import numpy as np

def get_slope(point1, point2):
    if point2[0]-point1[0] == 0:
        return float('inf')
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    return m

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
        pair[0] = [int(coord) for coord in pair[0]]
        pair[1] = [int(coord) for coord in pair[1]]
        slope = get_slope(pair[0], pair[1])
        # Vertical lines
        if slope == float("inf"):
            x = pair[0][0]
            y_start = pair[0][1]
            line_len = pair[1][1] - pair[0][1]
            if (line_len < 0):
                direction = -1
            for i in range(abs(line_len)+1):
                coords_map[x][y_start+(i*direction)]+=1
        # Horizontal lines
        elif slope == 0:
            y = pair[0][1]
            x_start = pair[0][0]
            line_len = pair[1][0] - pair[0][0]
            # print("horizontal line")
            # print(line_len)
            if (line_len < 0):
                direction = -1
            for i in range(abs(line_len)+1):
                coords_map[x_start+(i*direction)][y]+=1
        elif abs(slope) == 1:
            y_start = pair[0][1]
            x_start = pair[0][0]
            line_len = pair[1][0] - pair[0][0]
            # Get directions:
            if pair[1][0] > pair[0][0]:
                x_dir = 1
            else:
                x_dir = -1

            if pair[1][1] > pair[0][1]:
                y_dir = 1
            else:
                y_dir = -1

            # Update coordinates    
            for i in range(abs(line_len)+1):
                coords_map[x_start+(i*x_dir)][y_start+(i*y_dir)]+=1

    print(coords_map)
    print(np.count_nonzero(coords_map >= 2))


if __name__ == '__main__':
    main()