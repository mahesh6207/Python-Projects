import random
number = random.randint(1,10)
guess = int(input("guess a number betweenm 1 and 10:"))
if guess == number:
    print("Correct !")
else:
    print("Wrong! The number was",number)