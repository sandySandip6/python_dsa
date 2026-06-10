num = [0,1, 2, 3, 4, 5]

# Using list comprehension to create a new list with squares of the original numbers
squares = [x**2 for x in num]
print("Original list:", num)
print("Squares:", squares)
# Using list comprehension to create a new list with only even numbers from the original list
even_numbers = [x for x in num if x % 2 == 0]
print("Even numbers:", even_numbers)
# Using list comprehension to create a new list with the length of each number as a string
num_strings = [str(x) for x in num]
print("Number strings:", num_strings)

num_int = [int(x) for x in num_strings]
print("Number integers:", num_int)

odd_numbers = [x for x in num if x % 2 != 0]
print("Odd numbers:", odd_numbers)
words = ["python", "java", "c++"]
uppercase_strings = [x.upper() for x in words]
print("Uppercase strings:", uppercase_strings)
