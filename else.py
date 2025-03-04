import random


random_num = random.randint(0, 100)
b = 1
guess_try = 1 + (b)
while True:
    guess = int(input("guess a number \n"))
    if guess < random_num:
        print("this number you want is higher")
    elif guess > random_num:
        print("the number you want is lower")
    elif guess == 1 + (b):
        print("this is", guess_try, "number")
    else:
        print("congrats! you guessed it")
        break