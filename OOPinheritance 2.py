class shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class area(shape):
     def area(self):
         result = 0.5*self.base*self.height
         print(f"The area is {result}")

class ractangle(area):
     def ractangle(self):
         result2 = self.base*self.height
         print(f"the area is {result2}")

a = ractangle(20,30)
a.area()
a.ractangle()
