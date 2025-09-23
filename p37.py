#Example inheritance

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