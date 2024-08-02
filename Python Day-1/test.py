class person:
    def __init__(self, name:str, age:int)-> None:
        self.name = name
        self.age = age
    def __str__(self)-> str:
        return f'{self.name} is {self.age} years old'

def main()-> None:
    pass
