#reading file
# use all function one by one .

file=open("student.txt","r+")
print(file.readable())
print(file.writable())

text= file.readlines()[0]
print(text)

text=file.read()
print(text)

sizefile=len(text)
print(sizefile)

text= file.readlines()
print(text)

file.close()

# file writing
file=open("student1.txt","a")

file.write("\nmahim - swe")

file.close()