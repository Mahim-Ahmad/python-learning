#Exception .....Error thik kora

try:
    list=[20,0,10]
    result=list[0]/list[3]
    print(result)
    print("done")
except ZeroDivisionError:
    print("dividing by zero is not possible")
except IndexError:
    print("index error")
finally:
    print("successfully")