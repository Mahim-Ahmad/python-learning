  #tarnarry operator
num1=10
num2=12

max=num1 if num1>num2 else num2

print("maximum= ",max)


#logical ope

num1=10
num2=20
num3=12

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


ch="g"

if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("vowel")
else:
    print("consonent")