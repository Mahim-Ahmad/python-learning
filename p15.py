#pattern

n=int(input("Enter line number: "))

for x in range(n+1):
    print(x*"*")

n=int(input("Enter line number: "))

for x in range(n+1):
    print((2*x-1)*"*")

n=int(input("Enter line number: "))

for x in range(1, n+1):
    print(" " * (n - x) + "*" * x)