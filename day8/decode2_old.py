from collections import Counter


def main():
    input_file = "test_one.txt"

    #  aaaa      
    # b    c 
    # b    c 
    #  dddd  
    # e    f 
    # e    f 
    #  gggg 
    #  0000      
    # 1    2 
    # 1    2 
    #  3333  
    # 4    5 
    # 4    5 
    #  6666 
    normal_grid = {
        "a": 0, 
        "b": 1, 
        "c": 2, 
        "d": 3, 
        "e": 4, 
        "f": 5, 
        "g": 6
    }

    normal_digit_mapping = {
        0: "abcefg",
        1: "cf", # unique num
        2: "acdef",
        3: "acdfg",
        4: "bcdf", # unique num
        5: "abdfg",
        6: "abdefg", 
        7: "acf", # unique num
        8: "abcdefg", # unique num
        9: "abcfg"
    }

    normal_digit_len_mapping = {
        0: 6,
        1: 2, # unique num
        2: 5,
        3: 5,
        4: 4, # unique num
        5: 5,
        6: 6, 
        7: 3, # unique num
        8: 7, # unique num
        9: 5
    }

    unique_pattern_lens = {
        2: 1, # unique num
        4: 4, # unique num
        3: 7, # unique num
        7: 8, # unique num
    }

    

    # Get notes
    # [{ "signal_pattern": ["x", ...], "four digit output value": ["x", ...] }, ...]
    notes = [ segments.strip().split(" | ") for segments in open(input_file, 'r').readlines() ]
    segments_map = [ { "signal_pattern": [sorted(seg[0].split(" "))], "output_value": sorted(seg[1].split(" ")) } for seg in notes]
    
    print(segments_map)
    # unique_count = 0
    # total_count = 0
    # unique_lens = [2, 3, 4, 7]
    for seg in segments_map:
        seg["signal_pattern"].append([])
        digit_conversion = {}
        digit_mapping = {}
        for pattern in seg["signal_pattern"][0]:
            if len(pattern) in unique_pattern_lens.keys():
                seg["signal_pattern"][1].append(unique_pattern_lens[len(pattern)])
            else:
                seg["signal_pattern"][1].append(-1)
        print(seg["signal_pattern"])
        
        # Go through valid numbers:
        for i in range(len(seg["signal_pattern"][1])):
            if seg["signal_pattern"][1][i] in unique_pattern_lens.values():
                digit_mapping[seg["signal_pattern"][1][i]] = seg["signal_pattern"][0][i]
        print(digit_mapping)

        # Try to match with known patterns
        if 7 in digit_mapping and 1 in digit_mapping:
            for letter in digit_mapping[7]:
                if letter not in digit_mapping[1]:
                    digit_conversion[letter] = ["a"]
                else:
                    digit_conversion[letter] = ["c", "f"]
        if 7 in digit_mapping and 4 in digit_mapping:
            for letter in digit_mapping[7]:
                if letter not in digit_mapping[4]:
                    digit_conversion[letter] = ["a"]
                else:
                    digit_conversion[letter] = ["c", "f"]
            for letter in digit_mapping[4]:
                if letter not in digit_mapping[7]:
                    digit_conversion[letter] = ["b", "d"]

        for pattern in seg["signal_pattern"][0]:
            sorted_pattern = "".join(sorted(pattern))
            # Check for a 0, 6, or 9 (len 6)
            if len(sorted_pattern) == 6:
                print("Either 0, 6 or 9...")
                for num in [0, 6, 9]:
                    if num not in digit_mapping:
                        digit_mapping[num] = [sorted_pattern]
                    elif pattern not in digit_mapping[num]:
                        digit_mapping[num].append(sorted_pattern)
            # Check for a 2, 3, or 5 (len 5)
            if len(sorted_pattern) == 5:
                print("Either 2, 3, or 5...")
                for num in [2, 3, 5]:
                    if num not in digit_mapping:
                        digit_mapping[num] = [sorted_pattern]
                    elif pattern not in digit_mapping[num]:
                        digit_mapping[num].append(sorted_pattern)

        # More checking
        if 4 in digit_mapping and 9 in digit_mapping:
            remove = []
            for pattern in digit_mapping[9]:
                print("4: {} -> 9: {}".format(digit_mapping[4], pattern))
                count = 0
                for letter in digit_mapping[4]:
                    if letter in pattern:
                        # print("{} could not be a 9".format(pattern))
                        count+=1
                if count == 4:
                    real = digit_mapping[9][0]
                    print("9 found! -> {}".format(real))
            if real:
                print("Setting real 9!")
                digit_mapping[9] = real
                # for letter in pattern:
                #     if letter not in digit_mapping[4]:
                #         print(letter)
                #         digit_conversion[letter] = ["a", "g"]


        print(digit_mapping)
        print(digit_conversion)





    # print(f"total {total_count}, unique {unique_count}")
    # print(segments_map)



if __name__ == '__main__':
    main()