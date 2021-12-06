from __future__ import division

def main():
    input_file = "input.txt"
    gamma_bits_str = ""
    epsilon_bits_str = ""
    
    # Using readlines()
    file = open(input_file, 'r')
    lines = [list(line.strip()) for line in file.readlines()]
    len_bits = len(lines[0])
    # print(f"Bits length is {len_bits}")

    # Get gamma rate arrays
    for i in range(len_bits):
        print(i)
        bits = [ int(line[i]) for line in lines ]
        if sum(bits) / len(bits) > 0.5:
            gamma_bits_str+="1"
            epsilon_bits_str+="0"
        else:
            gamma_bits_str+="0"
            epsilon_bits_str+="1"
    
    gamma_rate = int(gamma_bits_str, 2)
    epsilon_rate = int(epsilon_bits_str, 2)
    print(f"gamma rate: {gamma_rate}, epsilon rate: {epsilon_rate}")
    print("Total power consumption is: {}".format(gamma_rate*epsilon_rate))

    # # Loop through report
    # for line in lines:
    #     nav = navigation_map[line[0]]
    #     next_coords = [i*int(line[1]) for i in nav]
    #     coords = [x + y for x, y in zip(coords, next_coords)]

    # print("Final coordinates: {}. Multiplied: {}".format(coords, coords[0]*coords[1]))

if __name__ == '__main__':
    main()