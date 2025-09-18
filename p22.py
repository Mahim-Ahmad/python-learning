#stack 

name=[]

name.append("mahim")
name.append("tamim")
name.append("masud")

print(name)

name.pop()
print(name)
print("top is : ",name[-1])

name.pop()
print(name)
print("top is : ",name[-1])

name.pop()
if not name:
    print("no name")