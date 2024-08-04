class Calculator:
    def __init__(self, version:int)->None:
        self.version=version

    @staticmethod #decorator static doesn't require self
    def add(*numbers:float)->float:
        return sum(numbers)
    
    def get_version(self)->int:
        return self.version # here is there is no self., it will be static i.e doesnt use instance
    
def main()->None:
    # calc:Calculator=Calculator(1)
    result:float=Calculator.get_version() #requires instance beacuse it is not static
    result:float=Calculator.add(1,2,3,4) #doesnot require instance beacuse it is static
    print(result)

if __name__ == "__main__":
    main()  