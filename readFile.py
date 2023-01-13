# import sys

# print('hello')
#sys.argv
#sys.stdin = open('input.txt', 'r')
#f = open("C:\\Users\\tanapon\\Desktop\\welcome.txt", "r")
#print(f.read())

# mean std min max  

# from statistics import mean, median
# # sys.stdin = open('input.txt', 'r')
# # f = open("C:\\Users\\tanapon\\Desktop\\welcome.txt", "r")
# f = open("C:\\Users\\tanapon\\Desktop\\welcome.txt", "r")
# total = 0
# lst = []
# for x in f:
#     if (x.isnumeric):
#         lst.append(x)
    
    
# avg_value = mean(lst)
# median_value = median(lst)
# # std_val = std(lst)
# min_val = min(lst)
# max_val = max(lst)
# print(avg_value)    
# print(median_value)
# print(min_val)
# print(max_val)
# # print(std_val)
#     # else print(x + 'this is not numeric')

import fileinput
from statistics import mean
for line in fileinput.input():
    lst = []
    if (line.isnumeric):
        lst.append(int(line))

print(lst)            
print('mean'+ mean(lst))
print('std')
print('max' + max(lst))
print('min' + min(lst))
