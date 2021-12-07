# from __future__ import division
import numpy as np

def main():
    input_file = "test.txt"
    days = 80
    
    # Get current fish timers
    fish_timers = open(input_file, 'r').readlines()[0].strip().split(",")
    fish_timers = [int(timer) for timer in fish_timers]
    # print(f"Initial state: {fish_timers}")

    # Loop through days
    for day in range(days):
        num_fish = len(fish_timers)
        for i in range(num_fish):
            if fish_timers[i] == 0:
                fish_timers[i] = 6
                fish_timers.append(8)
            elif fish_timers[i] > 0:
                fish_timers[i]-=1
    
    print(f"After {days} day: {fish_timers}")
    
    print(len(fish_timers))
    
    


if __name__ == '__main__':
    main()