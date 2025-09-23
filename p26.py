#Lamda function

#lambda perameter : exprationss

a=(lambda a,b : a*a + 2*a*b  + b*b)(2,3)
print(a)

print((lambda a,b : a*a + 2*a*b  + b*b)(2,3))


a=(lambda a : a*a*a)(2)
print(a)



#map and filter function

#map use for list

def square(x):
    return x*x

num=[1,2,3,4]

result=list(map(square,num))

print(result)


#filtaring

num=[1,2,3,4,5,6,7,8,9]

result=list(filter(lambda x : x%2==0,num))

print(result)
