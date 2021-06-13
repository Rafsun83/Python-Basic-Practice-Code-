from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def area(self):
        pass

class area(shape):
     def area(self):
         result = 0.5*self.base*self.height
         print(f"The area is {result}")

class ractangle(shape):
     def area(self):
         result2 = self.base*self.height
         print(f"the area is {result2}")

a = ractangle(20,30)
a.area()
b = area(20,30)
b.area()

