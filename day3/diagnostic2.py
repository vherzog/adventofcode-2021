from __future__ import division

def main():
    input_file = "input.txt"
    ox_rating = ""
    c02_rating = ""
    
    # Using readlines()
    file = open(input_file, 'r')
    lines = [list(line.strip()) for line in file.readlines()]
    len_lines = len(lines)
    len_bits = len(lines[0])
    # print(f"Bits length is {len_bits}")

    # Get ox rating
    ox_lines = lines
    for i in range(len_bits):
        print(i)
        bits = [ int(line[i]) for line in ox_lines ]
        print(bits)

        # Get oxygen generator rating:
        # Common bit is 1
        if sum(bits) / len(bits) >= 0.5:
            common_bit = 1
        else:
            common_bit = 0
        len_ox_lines = len(ox_lines)
        print(f"Common bit is {common_bit} and there are {len_ox_lines} ox lines left!")
        ox_lines = [ ox_lines[j] for j in range(len_ox_lines) if bits[j] == common_bit ]
        print(ox_lines)
        
        if len(ox_lines) == 1:
            print("OX Ratings found!")
            ox_rating = ox_lines[0]
            break

    # Get ox rating
    c02_lines = lines
    for i in range(len_bits):
        print(i)
        bits = [ int(line[i]) for line in c02_lines ]
        print(bits)

        # Get oxygen generator rating:
        # Common bit is 1
        if sum(bits) / len(bits) >= 0.5:
            common_bit = 0
        else:
            common_bit = 1
        len_c02_lines = len(c02_lines)
        print(f"Common bit is {common_bit} and there are {len_c02_lines} c02 lines left!")
        c02_lines = [ c02_lines[j] for j in range(len_c02_lines) if bits[j] == common_bit ]
        print(c02_lines)
        
        if len(c02_lines) == 1:
            print("C02 Ratings found!")
            c02_rating = c02_lines[0]
            break
    
    print(int("".join(ox_rating), 2))
    print(int("".join(c02_rating), 2))
    print(int("".join(ox_rating), 2) * int("".join(c02_rating), 2))
    # gamma_rate = int(gamma_bits_str, 2)
    # epsilon_rate = int(epsilon_bits_str, 2)
    # print(f"gamma rate: {gamma_rate}, epsilon rate: {epsilon_rate}")
    # print("Total power consumption is: {}".format(gamma_rate*epsilon_rate))

    # # Loop through report
    # for line in lines:
    #     nav = navigation_map[line[0]]
    #     next_coords = [i*int(line[1]) for i in nav]
    #     coords = [x + y for x, y in zip(coords, next_coords)]

    # print("Final coordinates: {}. Multiplied: {}".format(coords, coords[0]*coords[1]))

if __name__ == '__main__':
    main()