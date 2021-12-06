from __future__ import division

def main():
    input_file = "input.txt"
    boards = []
    
    # Using readlines()
    file = open(input_file, 'r')
    lines = [line.strip() for line in file.readlines()]
    len_lines = len(lines)
    # print(lines)

    call_numbers = lines[0].split(",")
    # print(call_numbers)

    # Get all boards
    for i in range(1, len_lines):
        if lines[i-1] == "":
            board = []
            for j in range(i, i+5):
                line = [ int(number) for number in lines[j].split(" ") if number != "" ]
                board.append(line)
            boards.append(board)
    max_boards = len(boards)
    winners = [0] * max_boards
    print(winners)
    winning_num = 0
    winning_num_index = 0
    winning_board = 0
    # Make board points
    board_points = []
    for b in range(max_boards):
        column_count = [0,0,0,0,0]
        row_count = [0,0,0,0,0]
        board_points.append([column_count, row_count])
        print(boards[b])
    for calls in range(len(call_numbers)):
        call_num = call_numbers[calls]
        num = int(call_num)
        for row in range(0, len(boards[b])):
            for col in range(0, len(boards[b])):
                for b in range(max_boards):
                    board_num = boards[b][row][col]
                    if board_num == num:
                        print(f"Num found! {num}")
                        board_points[b][0][row]+=1
                        board_points[b][1][col]+=1
                    if board_points[b][1][col] == 5:
                        print(f"Board {b} wins with column {col}!")
                        winners[b] = 1
                        winning_num = num
                        winning_num_index = calls
                        winning_board = b
                    if board_points[b][0][row] == 5:
                        print(f"Board {b} wins with row {row}!")
                        winners[b] = 1
                        winning_num = num
                        winning_num_index = calls
                        winning_board = b
                    if sum(winners) == max_boards:
                        print(f"Last one to win found... Board {b}")
                        break
                if sum(winners) == max_boards:
                        break
            if sum(winners) == max_boards:
                        break
        if sum(winners) == max_boards:
                        break

    print(f"Board {winning_board} wins with bingo number {winning_num} in place {winning_num_index}")
    board = boards[winning_board]
    board_total = 0
    for row in range(0, len(board)):
        print("Before: {}".format(board[row]))
        for col in range(0, len(board)):
            for calls in range(winning_num_index+1):
                if board[row][col] == int(call_numbers[calls]):
                    print("Match!")
                    board[row][col] = 0
        print("After: {}".format(board[row]))
        board_total+=sum(board[row])
    # Calculate winning score
    print(board_total)
    print(board_total * winning_num)

    # print(boards)

if __name__ == '__main__':
    main()