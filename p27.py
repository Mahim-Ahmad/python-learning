#list comprehensions


num=[1,2,3,4]

result=[x*x for x in num]

print(result)

num=[1,2,3,4]

result=[x for x in num if x%2==0]

print(result)


#zip function

roll=[1,2,3,4,5,6,7,8,9,10]
name=["mahim","tamim","masud","tayeb","sagor","mahim","tamim","masud","tayeb","sagor"]

x=list(zip(roll,name))
print(x)

roll=[1,2,3,4,5,6,7,8,9,10]
name=["mahim","tamim","masud","tayeb","sagor","mahim","tamim","masud","tayeb","sagor"]

x=list(zip(roll,name,"ASDFGHJKLB"))
print(x)