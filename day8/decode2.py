from collections import Counter


def main():
    input_file = "input.txt"

    # Get notes
    # [{ "signal_pattern": ["x", ...], "four digit output value": ["x", ...] }, ...]
    notes = [ segments.strip().split(" | ") for segments in open(input_file, 'r').readlines() ]
    segments_map = [ { "signal_pattern": seg[0].split(" "), "output_value": seg[1].split(" ") } for seg in notes]
    
    print(segments_map)
    unique_count = 0
    total_count = 0
    unique_lens = [2, 3, 4, 7]
    for seg in segments_map:
        for val in seg["output_value"]:
            print(f"Val {val} with len {len(val)}")
            total_count+=1
            if len(val) in unique_lens:
                unique_count+=1


    print(f"total {total_count}, unique {unique_count}")



if __name__ == '__main__':
    main()