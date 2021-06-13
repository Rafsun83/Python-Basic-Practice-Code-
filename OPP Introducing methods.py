class student():
    roll = ""
    cgpa = ""

    def set_value(self, roll, cgpa):
        self.roll=roll
        self.cgpa=cgpa

    def value(self):
        print(f"Roll={self.roll} cgpa={self.cgpa}")


Rahim = student()
Rahim.set_value(101,3.8)
Rahim.value()
