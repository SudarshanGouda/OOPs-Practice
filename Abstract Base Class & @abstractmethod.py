from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Retangle(shape):

    def __init__(self,Length,Breadth):
        self.lenth=Length
        self.breadth=Breadth

    def printarea(self):
        return f'Area is {self.lenth*self.breadth}'


rec=Retangle(5,4)

print(rec.printarea())
