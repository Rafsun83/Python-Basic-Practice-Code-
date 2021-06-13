from random import randint

for x in range(1,5):
    n = int(input("Enter the guessing number: "))
    randomNumber = randint(1, 5)
    if n == randomNumber:
       print("you won")
    else:
       print("you loss")
       print("your random number was: ", randomNumber)