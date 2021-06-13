class student:
    def __init__(self,roll, intake, section):
        self.roll = roll
        self.intake = intake
        self.section = section
    def S_roll(self):
        print(f"Student Roll is = {self.roll} \nStudent intake is = {self.intake} \nStudent Section is = {self.section}")

class teacher(student):

    def __init__(self, id, roll, intake, section):


        super().__init__(roll, intake, section)
        self.id = id
    def T_id(self):

        print("Teacher Id is = ", self.id)
t = teacher(12, 34,23,34)
t.T_id()
t.S_roll()



