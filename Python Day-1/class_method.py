""" from typing import Self
class Car:
    limiter: int=200

    def __init__(self,brand:str,max_speed:int) -> None:
        self.brand=brand
        self.max_speed=max_speed

    @classmethod #decoraters
    def change_limit(cls, new_limit:int) ->None:
        cls.limiter=new_limit

    def display_info(self)->None:
        print(f"{self.brand} (max={self.max_speed}, limiter={self.limiter})")

def main()->None:
    bmw:Car=Car("BMW", 240)
    toyota:Car=Car("Toyota",195)
    bmw.display_info()
    toyota.display_info()
    Car.change_limit(150)#calling the class function changes the value for the class not an instance
    #if toyota.limiter=150, it is instance so it inly changes value for instance not class
    bmw.display_info()
    toyota.display_info()
if __name__=="__main__":
    main()
 """
#factory method
from typing import Self
class Car:
    limiter: int=200

    def __init__(self,brand:str,max_speed:int) -> None:
        self.brand=brand
        self.max_speed=max_speed

    @classmethod #decoraters
    def change_limit(cls, new_limit:int) ->None:
        cls.limiter=new_limit

    @classmethod
    def autogenerate_max_speed(cls, brand:str)-> Self:
        lowered:str=brand.lower()
        max_Speed:int=200
        if lowered=='toyota':
            max_speed=270
        elif lowered=='bmw':
            max_speed=290
        elif lowered=='volvo':
            max_speed=300
        else:
            max_speed=300
        return cls(brand,max_speed)

    def display_info(self)->None:
        print(f"{self.brand} (max={self.max_speed}, limiter={self.limiter})")

def main()->None:
   volvo:Car=Car.autogenerate_max_speed('volvo')
   volvo.display_info()
if __name__=="__main__":
    main()
                 