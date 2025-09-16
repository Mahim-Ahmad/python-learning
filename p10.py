# using loop

i=1
while i<=10:
    print(i,end=" ")
    i=i+1
print("\nEnd")


#break and continue

i=1
while i<=10: 
    print(i,end=" ")
    i=i+1
    if i==5:
        break
print("\nEnd")

i=1
while i<=10:
    if i==5:
        i=i+1
        continue
    print(i,end=" ")
    i=i+1
print("\nEnd")