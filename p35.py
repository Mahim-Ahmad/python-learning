#Inheritance

class phone:
    def call(self):
        print("You can call")
    
    def messg(self):
        print("You can message")

class samsung(phone):
    def photo(self):
        print("You can take phote")

s=samsung()

s.call()
s.messg()
s.photo()

print(issubclass(samsung,phone))       