#control statement

mark=int(input("enter number : "))

if mark==0:
    print("zero")

elif mark%2==0:
    print("even")
else:
    print("odd")



name=input("enter number : ")
pas=input("enter pass : ")


if "mahim"==name:
    if("123"==pas):
        print("successfull login")
    else:
        print("wrong pass")

else:
        print("try again")