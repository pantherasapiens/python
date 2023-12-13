from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def adrive(self):
        pass

class Child(Parent):
    name = ""
    age = ""
    def adrive(self):
        self.name = "Anand"
        self.age = "yeee"

P1 = Child()
P1.adrive()
print(P1.name,P1.age)