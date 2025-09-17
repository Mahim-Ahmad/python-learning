#seris

n=int(input("Enter the last number: "))
sum=0

for x in range(1,n+1,1):
    sum=sum + x
print("Sum is",sum)

sum=0 

for x in range(1,n+1,1):
    sum=sum + (x*x)
print("Sum is",sum)


sum=1

for x in range(1,n+1,1):
    sum=sum * x
print("Sum is",sum)

#prime number and gcd , lmc