from tokenize import Number


arr = [1, 2, 3, 4, 5]

sort = arr.sort()
print(sort)

# #Task 1 
# for i in arr:
#     print(i)

# #Task 2
# sum = 0
# for i in arr:
#     sum += i
# print(sum)
    
# #Task 3
# sort = arr.sort()
# # reverse 
# # = sort[::-1]
# print(sort)

# #Task 4
# sort1 = arr.sort()
# print(arr[0])

# #Task 5
# search = arr.index(4)
# print(search)

# Task 6: Find Smallest Number
smallest = arr[0]
for i in arr:
    if i < smallest:
        smallest = i
print(smallest)

# Task 7: Find Largest Number
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print(largest)  

# Task 8: Find Average
sum = 0
for i in arr:
    sum += i
average = sum / len(arr)
print(average)  

# Task 9: Find Median
sorted_arr = sorted(arr)
n = len(sorted_arr)
if n % 2 == 0:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
else:
    median = sorted_arr[n // 2]
print(median)

# Task 10: Find Mode
from collections import Counter
counter = Counter(arr)
mode = counter.most_common(1)[0][0]
print(mode)


