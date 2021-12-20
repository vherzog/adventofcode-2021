# from __future__ import division
import numpy as np

directions = ["up", "down", "left", "right"]

def find_lowest(matrix, max_row, max_col, row, col):
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

def traverse_directions(matrix, max_row, max_col, row, col):
    next_directions = []

    for direction in directions:
        if (direction == "up" and row == 0) or (direction == "down" and row == (max_row - 1)) or (direction == "left" and col == 0) or (direction == "right" and col == (max_col - 1)):
            pass
        elif direction == "up":
            if matrix[row-1, col] != 9 and matrix[row-1, col] > matrix[row, col]:
                # print("adding {}".format([row-1, col]))
                next_directions.append([row-1, col])
        elif direction == "down":
            if matrix[row+1, col] != 9 and matrix[row+1, col] > matrix[row, col]:
                # print("adding {}".format([row+1, col]))
                next_directions.append([row+1, col])
        elif direction == "left":
            if matrix[row, col-1] != 9 and matrix[row, col-1] > matrix[row, col]:
                # print("adding {}".format([row, col-1]))
                next_directions.append([row, col-1])
        elif direction == "right":
            if matrix[row, col+1] != 9 and matrix[row, col+1] > matrix[row, col]:
                # print("adding {}".format([row, col+1]))
                next_directions.append([row, col+1])
    
    return next_directions

def find_basin(matrix, max_row, max_col, low_row, low_col):
    directions = [[low_row, low_col]]
    basin_coords = [[low_row, low_col]]
    basin = True
    while basin:
        next_directions = []
        # print(f"Current directions are {directions}")
        for direction in directions:
            # print(f"=> direction is: {direction}")
            traversal = traverse_directions(matrix, max_row, max_col, direction[0], direction[1])
            # print(f"==> traversal is: {traversal}")
            next_directions+=traversal
        if len(next_directions) == 0:
            basin = False
        else:
            # print("=> adding more to basin")
            # print(next_directions)
            for next_dir in next_directions:
                add = True
                # print(basin_coords)
                for coord in basin_coords:
                    if coord == next_dir:
                        # print("not adding!!")
                        add = False
                if add:
                    # print("adding {}".format([next_dir[0], next_dir[1]]))
                    basin_coords.append([next_dir[0], next_dir[1]])
            directions = next_directions
            # print("=> directions updated")

    return basin_coords

# def get_max_num(nums, count):
#     max_nums = []
#     for c in range(count):
#         max_index = 0
#         for i in range(len(nums)-1):
#             if nums[i] < nums[i+1]:
#                 max_index = i+1
#         print("Max value is {}".format(nums[max_index]))
#         max_nums.append(nums[max_index])
#         nums.pop(max_index)
#     return max_nums

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

    # print(f"Row: {max_row}")
    # print(f"Col: {max_col}")

    heights_matrix = np.array(all_heights)

    # print("adjacents to [0,0]")
    adjacents = find_lowest(heights_matrix, max_row, max_col, 0, 0)
    # print(adjacents)

    lowests = []

    for row in range(max_row):
        for col in range(max_col):
            lowest = find_lowest(heights_matrix, max_row, max_col, row, col)
            if lowest:
                # print("Lowest [{},{}]: {}".format(row, col, heights_matrix[row,col]))
                lowests.append((row,col))
    
    print(lowests)

    basin_sizes = []
    
    for lowest in lowests:
        basin = find_basin(heights_matrix, max_row, max_col, lowest[0], lowest[1])
        print("Basin found with size {} ! ==> {}".format(len(basin), basin))
        basin_sizes.append(len(basin))
    
    print(f"Basin sizes: {basin_sizes}")

    # max_basins = get_max_num(basin_sizes, 3)

    basin_sizes.sort(reverse=True)
    max_basins = basin_sizes[:3]
    print("Result is: {}".format(np.prod(max_basins)))


if __name__ == '__main__':
    main()