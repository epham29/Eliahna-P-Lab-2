import random

game_number = random.randint(1,10)
#print(game_number)

attempts = 0

while(True):
    guess = int(input("Enter a number between 1 and 10: "))
    attempts += 1

    if guess > game_number:
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else:
        print("You Win!")
        if attempts >= 5:
            print("Do better next time!")
        else:
            print("Great job!")
        break