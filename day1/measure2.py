def main():
    input_file = "input.txt"
    
    # Using readlines()
    file = open(input_file, 'r')
    lines = file.readlines()
    lines = [int(line) for line in lines]
    len_lines = len(lines)
    
    total = 0
    increase_count = -1
    previous = 0

    # Range only go up to second to last line
    for i in range(len_lines-2):
        measurement = sum(lines[i:i+3])
        print("Window {} has sum {}".format(lines[i:i+3], measurement))
        if measurement > previous:
            increase_count+=1
        total+=1
        previous = measurement


    print("Of {} windows, {} increased in depth".format(total, increase_count))

if __name__ == '__main__':
    main()