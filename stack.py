def stack(self):    
    arr = [5, 10, 15, 20, 25]
    res = len(self.arr)-1
    
    return print(res)


# # Class representing a Stack
# class Stack:

#     def __init__(self):
#         self.arr = [0]*5
#         self.top = -1

#     # Method to push element
#     def push(self, x):
#         if self.top == 4:
#             print("Stack Overflow")
#             return
#         self.top += 1
#         self.arr[self.top] = x

#     # Method to pop element
#     def pop(self):
#         if self.top == -1:
#             print("Stack Underflow")
#             return
#         self.top -= 1

#     # Method to display stack
#     def display(self):
#         for i in range(self.top, -1, -1):
#             print(self.arr[i], end=" ")
#         print()

# # driver code
# if __name__ == "__main__":

#     # Creating stack object
#     s = Stack()

#     # Performing operations
#     s.push(10)
#     s.push(20)
#     s.push(30)
#     s.push(40)
#     s.push(50)
    

#     print("Stack elements: ", end="")
#     s.display()

#     s.pop()

#     print("After pop: ", end="")
#     s.display()