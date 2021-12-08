# credit/source: https://github.com/schamanegeist/adventofcode2021/blob/master/day8/part2.py
from collections import Counter


def main():
    input_file = "input.txt"
    input_data = [ segments.strip().split(" | ") for segments in open(input_file, 'r').readlines() ]
    digits = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9"}

    numbers = []
    for line in input_data:
        counts = Counter(line[0].replace(" ",""))
        trans = {x[0]: {4:"e",6:"b",9:"f"}[x[1]]for x in counts.items() if x[1] in (4,6,9)}

        for each in line[0].split():
            if len(each) == 2:
                trans.update({seg: "c" for seg in each if seg not in trans})
        
        trans.update({x[0]: "a" for x in counts.items() if x[1] == 8 and x[0] not in trans})

        for each in line[0].split():
            if len(each) == 4:
                trans.update({seg: "d" for seg in each if seg not in trans})

        trans.update({x[0]: "g" for x in counts.items() if x[1] == 7 and x[0] not in trans})
        deciphered = line[1].translate(str.maketrans(trans)).split()

        numbers.append(int("".join([digits["".join(sorted(term))] for term in deciphered])))

    print(sum(numbers))
    # Get notes
    # [{ "signal_pattern": ["x", ...], "four digit output value": ["x", ...] }, ...]
    # notes = [ segments.strip().split(" | ") for segments in open(input_file, 'r').readlines() ]
    # print(notes)
    # segments_map = [ { "signal_pattern": [sorted(seg[0].split(" "))], "output_value": sorted(seg[1].split(" ")) } for seg in notes]
    
    # print(segments_map)
    # unique_count = 0
    # total_count = 0
    # unique_lens = [2, 3, 4, 7]
    # for line in open("test_one.txt").readlines():
    #     data = sorted(list(map(set,line.strip().split()[:10])), key=len)
    #     print(data)
        # seg["signal_pattern"].append([])
        # digit_conversion = {}
        # digit_mapping = {}
        # for pattern in seg["signal_pattern"][0]:
        #     if len(pattern) in unique_pattern_lens.keys():
        #         seg["signal_pattern"][1].append(unique_pattern_lens[len(pattern)])
        #     else:
        #         seg["signal_pattern"][1].append(-1)
        # print(seg["signal_pattern"])
        
        # # Go through valid numbers:
        # for i in range(len(seg["signal_pattern"][1])):
        #     if seg["signal_pattern"][1][i] in unique_pattern_lens.values():
        #         digit_mapping[seg["signal_pattern"][1][i]] = seg["signal_pattern"][0][i]
        # print(digit_mapping)

        # # Try to match with known patterns
        # if 7 in digit_mapping and 1 in digit_mapping:
        #     for letter in digit_mapping[7]:
        #         if letter not in digit_mapping[1]:
        #             digit_conversion[letter] = ["a"]
        #         else:
        #             digit_conversion[letter] = ["c", "f"]
        # if 7 in digit_mapping and 4 in digit_mapping:
        #     for letter in digit_mapping[7]:
        #         if letter not in digit_mapping[4]:
        #             digit_conversion[letter] = ["a"]
        #         else:
        #             digit_conversion[letter] = ["c", "f"]
        #     for letter in digit_mapping[4]:
        #         if letter not in digit_mapping[7]:
        #             digit_conversion[letter] = ["b", "d"]

        # for pattern in seg["signal_pattern"][0]:
        #     sorted_pattern = "".join(sorted(pattern))
        #     # Check for a 0, 6, or 9 (len 6)
        #     if len(sorted_pattern) == 6:
        #         print("Either 0, 6 or 9...")
        #         for num in [0, 6, 9]:
        #             if num not in digit_mapping:
        #                 digit_mapping[num] = [sorted_pattern]
        #             elif pattern not in digit_mapping[num]:
        #                 digit_mapping[num].append(sorted_pattern)
        #     # Check for a 2, 3, or 5 (len 5)
        #     if len(sorted_pattern) == 5:
        #         print("Either 2, 3, or 5...")
        #         for num in [2, 3, 5]:
        #             if num not in digit_mapping:
        #                 digit_mapping[num] = [sorted_pattern]
        #             elif pattern not in digit_mapping[num]:
        #                 digit_mapping[num].append(sorted_pattern)

        # # More checking
        # if 4 in digit_mapping and 9 in digit_mapping:
        #     remove = []
        #     for pattern in digit_mapping[9]:
        #         print("4: {} -> 9: {}".format(digit_mapping[4], pattern))
        #         count = 0
        #         for letter in digit_mapping[4]:
        #             if letter in pattern:
        #                 # print("{} could not be a 9".format(pattern))
        #                 count+=1
        #         if count == 4:
        #             real = digit_mapping[9][0]
        #             print("9 found! -> {}".format(real))
        #     if real:
        #         print("Setting real 9!")
        #         digit_mapping[9] = real
        #         # for letter in pattern:
        #         #     if letter not in digit_mapping[4]:
        #         #         print(letter)
        #         #         digit_conversion[letter] = ["a", "g"]


        # print(digit_mapping)
        # print(digit_conversion)





    # print(f"total {total_count}, unique {unique_count}")
    # print(segments_map)



if __name__ == '__main__':
    main()