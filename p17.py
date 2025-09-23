#list input from user

n=input("Enter a text of number: ")

list= n.split()
sum=0

for x in list:
    sum=sum+int(x)
print(sum)

#practice website pynative

numofword=0
numofletter=0
numofdigit=0
n=input("Enter a text of number: ")

for x in n:
    x=x.lower()
    if x>='a' and x<='z':
       numofletter=numofletter+1 

    elif x>='0' and x<='9':
        numofdigit=numofdigit+1

    elif x==' ':
        numofword=numofword+1

print(numofword+1)
print(numofletter)
print(numofdigit)