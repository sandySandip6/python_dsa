class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next 

class SinglList:
    def __init__(self, head = None):
        self.head = head 
        
    def insert_at_end(self, data):
        temp = Node(data)
        if (self.head != None):
            temp1 = self.head
            while (temp1.next != None):
                temp1 = temp1.next
            temp1.next = temp
        else:
            self.head = temp
            
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end = " ")
            temp = temp.next

s = SinglList()
s.insert_at_end(10)
s.insert_at_end(20)
s.insert_at_end(30)
s.display()  
