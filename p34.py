#construct


class student:
    roll=""
    gpa=""
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll : {self.roll}, Gpa:{self.gpa}")


mahim=student(705,4.00)
mahim.display()

tamim=student(858,3.88)
mahim.display()