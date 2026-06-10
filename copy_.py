# Python program to illustrate the difference between shallow and deep copy
import copy


class Car:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors


# Create a Honda car object
honda_colors = ["Red", "Blue"]
honda = Car("Honda", honda_colors)

# Deepcopy of Honda
deepcopy_honda = copy.deepcopy(honda)
deepcopy_honda.colors.append("Green")
print("Deepcopy:", deepcopy_honda.colors)
print("Original:", honda.colors)

# Shallow Copy of Honda
copy_honda = copy.copy(honda)
copy_honda.colors.append("Green")
print("Shallow Copy:", copy_honda.colors)
print("Original:", honda.colors)


# import copy 

# a = [1, 2, 3, 4, 5]
# b = a

# print("a:", a)
# print("b:", b)
# copy_b = copy.copy(b)
# copy_b.append(6)
# addedcopy_b = copy.copy(copy_b)
# addedcopy_b.append(7)
# print("addedcopy_b:", addedcopy_b)
# addedcopy_b.append(8)
# print("a:", a)
# print("b:", b)
# print("copy_b:", copy_b)
# print("addedcopy_b:", addedcopy_b)

# copy_b_b = copy.copy(copy_b)

