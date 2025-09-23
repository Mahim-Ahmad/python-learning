# xargs and xxargs

#xargs

def details(*x):
    print(x)
    print(x[0])
    print(x[1:])


details(1,"mahim",242)
details(2,"tamim",242)


def number(*num):
    sum=0
    for x in num:
        sum=sum+x
    print(sum)

number(1,2)
number(1,2,3)
number(1,2,3,4)


#xxargs

def details(**student):
    print(student)
    print(student["id"])


details(id=101,name="mahim")

