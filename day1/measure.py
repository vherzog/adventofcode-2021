input_file = "input.txt"
 
# Using readlines()
file = open(input_file, 'r')
lines = file.readlines()
 
# Get line and convert to integer
total = 0
increase_count = -1 # First measurement does not count
previous = 0
for line in lines:
    measurement = int(line.strip())
    if measurement > previous:
        increase_count+=1
    total+=1
    previous = measurement


print("Of {} meaurements, {} increased in depth".format(total, increase_count))