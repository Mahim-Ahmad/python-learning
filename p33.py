#class ar under a method

class student:
    roll=""
    gpa=""
    def details(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll : {self.roll}, Gpa:{self.gpa}")


mahim=student()
mahim.details(705,4.00)
mahim.display()

tamim=student()
mahim.details(858,3.88)
mahim.display()