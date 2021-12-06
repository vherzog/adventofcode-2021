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
    print(coord_pairs)
    print(f"Max X is {max_x}. Max Y is {max_y}.")

    coords_map = np.zeros((max_y+2)*(max_x+2)).reshape(max_y+2,max_x+2)
    print(coords_map)

    # Map lines from coordinate pairs
    for pair in coord_pairs:
        direction = 1
        # Only check straight lines for now
        if pair[0][0] == pair[1][0]:
            x = int(pair[0][0])
            y_start = int(pair[0][1])
            line_len = int(pair[1][1]) - int(pair[0][1])
            print(f"This is a vertical line {pair} with length {line_len} starting at {x}, {y_start}")
            print("{} minus {} is {}".format(int(pair[1][1]), int(pair[0][1]), line_len))
            if (line_len < 0):
                print("negative")
                direction = -1
            for i in range(abs(line_len)+1):
                print(i)
                coords_map[x][y_start+(i*direction)]+=1
        elif pair[0][1] == pair[1][1]:
            print("This is a horizontal line...")
            y = int(pair[0][1])
            x_start = int(pair[0][0])
            line_len = int(pair[1][0]) - int(pair[0][0])
            print(f"This is a horizontal line {pair} with length {x_start} starting at {x_start}, {y}")
            print("{} minus {} is {}".format(int(pair[1][1]), int(pair[0][1]), line_len))
            if (line_len < 0):
                print("negative")
                direction = -1
            for i in range(abs(line_len)+1):
                print(i)
                coords_map[x_start+(i*direction)][y]+=1

    print(coords_map)
    print(np.count_nonzero(coords_map >= 2))

    # call_numbers = lines[0].split(",")
    # # print(call_numbers)

    # # Get all boards
    # for i in range(1, len_lines):
    #     if lines[i-1] == "":
    #         board = []
    #         for j in range(i, i+5):
    #             line = [ int(number) for number in lines[j].split(" ") if number != "" ]
    #             board.append(line)
    #         boards.append(board)
    # winner = False
    # winning_num = 0
    # winning_num_index = 0
    # winning_board = 0
    # # Make board points
    # board_points = []
    # for b in range(len(boards)):
    #     column_count = [0,0,0,0,0]
    #     row_count = [0,0,0,0,0]
    #     board_points.append([column_count, row_count])
    #     print(boards[b])
    # for calls in range(len(call_numbers)):
    #     call_num = call_numbers[calls]
    #     num = int(call_num)
    #     for row in range(0, len(boards[b])):
    #         for col in range(0, len(boards[b])):
    #             for b in range(len(boards)):
    #                 board_num = boards[b][row][col]
    #                 if board_num == num:
    #                     print(f"Num found! {num}")
    #                     board_points[b][0][row]+=1
    #                     board_points[b][1][col]+=1
    #                 if board_points[b][1][col] == 5:
    #                     print(f"Board {b} wins with column {col}!")
    #                     winner = True
    #                     winning_num = num
    #                     winning_num_index = calls
    #                     winning_board = b
    #                     break
    #                 if board_points[b][0][row] == 5:
    #                     print(f"Board {b} wins with row {row}!")
    #                     winner = True
    #                     winning_num = num
    #                     winning_num_index = calls
    #                     winning_board = b
    #                     break
    #             if winner:
    #                 break
    #         if winner:
    #             break
    #     if winner:
    #         break

    # print(f"Board {winning_board} wins with bingo number {winning_num} in place {winning_num_index}")
    # board = boards[winning_board]
    # board_total = 0
    # for row in range(0, len(board)):
    #     print("Before: {}".format(board[row]))
    #     for col in range(0, len(board)):
    #         for calls in range(winning_num_index+1):
    #             if board[row][col] == int(call_numbers[calls]):
    #                 print("Match!")
    #                 board[row][col] = 0
    #     print("After: {}".format(board[row]))
    #     board_total+=sum(board[row])
    # # Calculate winning score
    # print(board_total)
    # print(board_total * winning_num)

    # # print(boards)

if __name__ == '__main__':
    main()