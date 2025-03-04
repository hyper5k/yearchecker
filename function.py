import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)



def play_game():
    money = 1000
    spaces = generate_wheel()

    while True:
        print("you have $" + str(money) + ".")
        bet = input("how much do you want to bet?")
        bet = int(bet)
        color = input("What color do you want to be on")
        
        print("the wheel is spinning. Goood luck")
        time.sleep(2)
        landed = spin_wheel(spaces)
        print("it landed on " + landed + ".")

        if landed == color:
            money = money + bet
            print("Congrats! you now have $" + str(money))
        else:
            money = money - bet
            print("sorry! you now have $" + str(money))
        
        play_again = input("Do you want to play again")
        if play_again == "no":
            break

play_game()