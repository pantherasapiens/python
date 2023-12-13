class Parent:
    name = ""
    age = ""
    def dust(self,x,y):
        self.name = x
        self.age = y

class Child(Parent):
    def __init__(self):
        self.name = "Anand"
        self.age = "No"
    

p1 = Child()
print(f"My name is {p1.name} and age is given as {p1.age}")
p2 = Parent()
p2.dust(x = "Vaibhaw", y = "Ye")
print(f"My name is {p2.name} and age is given as {p2.age}")