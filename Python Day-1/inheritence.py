""" class animal:
    def __init__(self,name:str) -> None:
        self.name=name

    def drink(self)-> None:
        print(f"{self.name} is drinking.")

    def eat(self)->None:
        print(f"{self.name} is eating.")
    
#Inherit class
class dog(animal):#animal is parent, dog is derived
    def __init__(self, name: str) -> None:
        super().__init__(name) #super() initializes the parent class

    def bark(self)-> None:
        print(f"{self.name} is barking.")

    def routine(self) ->None:
        self.eat()
        self.bark()
        self.drink()
class cat(animal):
    def __init__(self,name:str)-> None:
        super().__init__(name)
    def meow(self)-> None:
        print(f"{self.name} is meowing.")

def main()->None:
    Dog:dog=dog("Tommy")
    Cat:cat=cat("Kitty")

    Dog.bark()
    Cat.meow()

if __name__ == "__main__":
    main()


 """
#super()
from typing import override
class Shape:
    def __init__(self, name:str, sides:int)-> None:
        self.name=name
        self.sides=sides

    def describe(self)-> None:
        print(f"{self.name} has {self.sides} sides.")

    def shape_method(self)-> None:
        print(f"{self.name}: shape_method()")
class Square(Shape):
    def __init__(self, size:float)-> None:
        super().__init__('Square',4)
        self.size=size

    @override
    def describe(self)->None:
        print(f"I am a {self.name} with {self.sides} side")

class Rectangle(Shape):
    def __init__(self,length:float,breadth:float)->None:
        super().__init__('Rectangle',4)
        self.length=length
        self.breadth=breadth
    @override
    def describe(self)->None:
        print("This overrided the original fucntion 'describe'")
def main()->None:
    rectangle:Rectangle=Rectangle(10,5)
    rectangle.describe()
if __name__ == "__main__":
    main()
