import sys

# check if we have the file name
if len(sys.argv) < 2:
    print("Please provide a file name")
    quit()

file_name = sys.argv[1]

# test if file exist
try:
    file = open(file_name, 'r')
except FileNotFoundError:
    print("File not found")
    quit()

lines = file.readlines()
nums = []
for line in lines:
    # read number for each line
    nums.append(int(line.strip()))

# find the std of nums
mean = sum(nums) / len(nums)
std = 0
for num in nums:
    std += (num - mean) ** 2

print("mean: ", mean)
print("std: ", std)
print("min: ", min(nums))
print("max: ", max(nums))
