#guessing a number
import random

random_number=random.randint(1,50)
guess=int(input("Guess a number:"))

count = 1
while random_number != guess:

    if random_number > guess:
        print("Your guess is too low")
    elif random_number < guess:
        print("Your guess is too high")
    elif random_number == guess:
        print("You guess the correct answer.")

    guess=int(input("Guess a number"))
    count += 1
    if count == 3:
        print("You ran out the chance.")
        break

#Loop
i=0
while i<11:
    print(i)
    i+=1

i=10
while i>=0:
    print(i)
    i-=1