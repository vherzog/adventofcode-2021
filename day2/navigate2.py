def main():
    input_file = "input.txt"
    coords = [0,0,0] # [horizontal, depth, aim]

    navigation_map = {
        "forward": [1,0,0],
        "down": [0,0,1],
        "up": [0,0,-1]
    }
    
    # Using readlines()
    file = open(input_file, 'r')
    lines = file.readlines()
    lines = [line.strip().split(" ") for line in lines]
    len_lines = len(lines)

    # Loop through directions
    for line in lines:
        direction = line[0]
        nav = navigation_map[direction]
        next_coords = [i*int(line[1]) for i in nav]
        if direction == "forward":
            next_coords[1]+= coords[2]*next_coords[0]
        coords = [x + y for x, y in zip(coords, next_coords)]

    print("Final coordinates: {}. Multiplied: {}".format(coords, coords[0]*coords[1]))

if __name__ == '__main__':
    main()