from abc import ABC, abstractmethod

class Appliance(ABC): #Abstract Base Class
    def __init__(self,brand:str,version_no:int)->None:
        self.brand=brand
        self.version_no=version_no
        self.is_turned_on:bool=False

    @abstractmethod
    def turn_on(self)->None:
        pass
    @abstractmethod
    def turn_off(self)->None:
        pass

class Lamp(Appliance):
    def __init(self,brand:str,version_no:int)->None:
        super().__init__(brand, version_no)


        def turn_on(slef)->None:
            if self.is_turned_on:
                print(f"{self.brand} is already turned on!")
            else:
                self.is_turned_on==True

        def turn_off(Self)->None:

