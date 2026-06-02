class myClass:
    def __init__(self):
        self.name = ""
        self.age = 0
        
    def myDetails(self):
        r = "My name is " + self.name + " and I am " + str(self.age) + " years old."
        print(r)
        return r
       

mc = myClass()

mc.name = "sandy"
mc.age = 22

mc.myDetails()

    