#list function

name = ["mahim","tamim","sagor","masud","tayeb"]

print(len(name)) #length

name.append("kamal") #add in list
print(name)

name.insert(2,"jamal")
print(name)

name.remove("masud")
print(name)

name.sort()
print(name)

num=[2,4,1,5,8,9]

num.sort()
print(num)

num.reverse()
print(num)

num.pop()
print(num)

num.clear()
print(num)

num=[2,4,1,5,8,9]
num2=num.copy()

print(num2)

position=name.index("mahim")
print(position)

name = ["mahim","tamim","sagor","masud","tayeb","mahim","mahim"]

count=name.count("mahim")
print(count)

#rang function 
number = list(range(10))
print(number)
 
number = list(range(5,10))
print(number)
 
number = list(range(2,31,2)) #last 2 use for different into two number
print(number)