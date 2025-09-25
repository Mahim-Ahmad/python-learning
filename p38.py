#type of inheritance

#hierarchical in...
"""
class shape:
    def __init__(self,dim1,dim2):
      self.dim1=dim1
      self.dim2=dim2
    
    def area(self):
      pass

class tringle(shape):
    def area(self):
      area=0.5 * self.dim1 * self.dim2
      print(area)

class retngular(shape):
    def area(self):
      area=self.dim1 * self.dim2
      print(area)
    


t=tringle(20,30)
t.area()

r=retngular(20,30)
r.area()
"""

#multi-level in..
"""
class A:
    def display1(self):
        print("i am insite A class")

class B(A):
    def display2(self):
        print("i am insite B class")
class C(B):
    def display3(self):
        print("i am insite C class")


ob1 = C()
ob1.display1()
ob1.display2()
ob1.display3()

"""

"""
class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("i am insite C class")

ob1 = C()
ob1.display3()
"""


#multiple in...
class A:
    def display(self):
        print("i am insite A class")

class B:
    def display(self):
        print("i am insite B class")
class C(A,B): #priopity
    def display(self):
        print("i am insite C class")


ob1 = C()
ob1.display() #pririty wise prine