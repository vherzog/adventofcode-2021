from collections import Counter


def main():
    input_file = "input.txt"
    
    # Get crab positions
    crab_positions = [ int(pos) for pos in open(input_file, 'r').readlines()[0].strip().split(",") ]
    crab_positions = Counter(crab_positions)

    # Order crab positions
    crab_positions = crab_positions.most_common()
    print(f"Initial state: {crab_positions}")

    # Get most common and range
    most_common_position = crab_positions[0]
    print(f"Most common: {most_common_position}")
    max_position = max(crab_positions)[0]
    min_position = min(crab_positions)[0]
    print(f"Max: {max_position}. Min: {min_position}")
    # print(type(fish_counter))

    # Calculate target orders:
    target_positions = []
    for i in range(len(crab_positions)):
        if i == len(crab_positions)-1:
            target_positions.append(crab_positions[i][0])
        else:
            direction = 1
            if crab_positions[i][0] > crab_positions[i+1][0]:
                direction = -1
            for j in range(crab_positions[i][0], crab_positions[i+1][0] + (1*direction), direction):
                if j not in target_positions:
                    target_positions.append(j)
    
    print(target_positions)

    cheapest_position = target_positions[0]
    cheapest_fuel = -1
    
    for position in target_positions:
        fuel = 0
        for crab in crab_positions:
            added_fuel = 0
            distance_to_move = abs((crab[0]-position))
            for i in range(1, distance_to_move+1):
                added_fuel+=i*crab[1]
            fuel+=added_fuel
            # print(f"Target {position} -> Position {crab} -> total fuel added {added_fuel}")
        print(f"***** Target {position} -> Fuel total: {fuel} *****")

        # Check for first iteration
        if cheapest_fuel == -1:
            cheapest_fuel = fuel
        # Check if current fuel is better than previous
        elif fuel < cheapest_fuel:
            cheapest_fuel = fuel
            cheapest_position = position

    print(f"Target position should be {cheapest_position} with fuel {cheapest_fuel}")



if __name__ == '__main__':
    main()