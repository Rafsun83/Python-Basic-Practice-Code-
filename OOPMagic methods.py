class bike:
    def __init__(self, name , color ):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name==other.name and self.color==other.color

    def __str__(self):
       return (f"Name: {self.name} color: {self.color} ")
    def display(self):

        print(f"Name: {self.name} color: {self.color} ")


bike1 = bike("Suzuki SF", "Blue")
bike2 = bike("Suzuki SF", "Blue")
print(bike1==bike2)