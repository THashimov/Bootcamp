import re
import math

input_file = open("24/input.txt", "r", encoding="UTF-8")
output_file = open("24/output.txt", "w+", encoding="UTF-8")

def get_max(nums):
    return max(nums)

def get_min(nums):
    return min(nums)

# Cast the chars in the list for ints
def get_avg(nums):
    nums = [int(x) for x in nums]
    return sum(nums) / len(nums)

# Remove the first element and save it in a variable as that value is the value of the percentile
# Cast the list to int and sort
def get_percentile(nums) :
    nums = [int(x) for x in nums]
    percentile = nums[0] / 100
    nums.remove(percentile * 100)
    nums.sort()

    return percentile * len(nums)

# Iterate over the lines in input.txt
# Use a regex to remove anything that isn't a number and replace it with a space
# Use split to convert the line to a list
# Pass that list to the corresponding function, based on the first 3 characters of the line
for line in input_file :
    nums = re.sub("[^0-9]", " ", line).split()
    if line.strip()[:3] == "max" :
        output_file.write(f"The max of {nums} is {get_max(nums)}.\n")
    elif line.strip()[:3] == "avg" :
        output_file.write(f"The average of {nums} is {get_avg(nums)}.\n")
    elif line.strip()[:1].lower() == 'p' :
        output_file.write(f"The {line.strip()[1:3]}th percentile of {nums} is {math.ceil(get_percentile(nums))}.\n")
    else :
        output_file.write(f"The min of {nums} is {get_min(nums)}.\n")

input_file.close()
output_file.close()