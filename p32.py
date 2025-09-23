#class and object

class student:
    roll=""
    gpa=""
karim=student()
print(isinstance(karim,student))
mahim=student()
mahim.roll=705
mahim.gpa=4.00
print(f"Roll:{mahim.roll},GPA:{mahim.gpa}")

tamim=student()
tamim.roll=705
tamim.gpa=4.00
print(f"Roll:{tamim.roll},GPA:{tamim.gpa}")