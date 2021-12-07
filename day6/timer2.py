from collections import Counter


def main():
    input_file = "input.txt"
    days = 256
    
    # Get current fish timers
    fish_timers = open(input_file, 'r').readlines()[0].strip().split(",")
    fish_timers = [int(timer) for timer in fish_timers]
    fish_counter = Counter(fish_timers)
    # print(f"Initial state: {fish_counter}")
    # print(type(fish_counter))

    # Loop through days
    for day in range(days):
        new_fish_counter = {}
        # Check 8 first
        if 8 in fish_counter:
            new_fish_counter[7] = fish_counter[8]
        # Spawn new fish and reset counter
        if 0 in fish_counter:
            new_fish_counter[6] = fish_counter[0]
            new_fish_counter[8] = fish_counter[0]
        # Count down fish timers
        for i in range(1, 8):
            if i == 7:
                if 7 in fish_counter:
                    if 6 in new_fish_counter:
                        new_fish_counter[6]+=fish_counter[7]
                    else:
                        new_fish_counter[6]=fish_counter[7]
            else:
                if i in fish_counter:
                    new_fish_counter[i-1] = fish_counter[i]
        fish_counter = new_fish_counter
        # print(f"After {day+1} day: {fish_counter}")
    
    # print(f"After {days} day: {fish_counter}")
    
    print(sum(fish_counter.values()))
    
    


if __name__ == '__main__':
    main()