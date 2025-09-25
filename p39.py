#abstraction.....aita use korle aita onno class a use korle bitorer abstract function use e korte hobe and class ar object banano jai nah

from abc import ABC,abstractmethod

class shape:
    def __init__(self,dim1,dim2):
      self.dim1=dim1
      self.dim2=dim2
    @abstractmethod
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