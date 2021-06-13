class student():
    roll = ""
    cgpa = ""
    def __init__(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa
    def display(self):
        print(f"Roll = {self.roll}, Cgpa = {self.cgpa}")


Rahim = student(101, 3.7)
Rahim.display()
