#guessing game
import random
for x in range(1,5):
    n=int(input("Enter you guess number: "))

    randomnumber=random.randint(1,10)
    
    if n==randomnumber :
        print("congress")
    else:
        print("try again")
        print(randomnumber)
    


