import random

while True:
    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock,Paper or Scissors?: \n")
        player = player.upper()

    if player == CPU:
        print(f"player({player}) : CPU({CPU})")
        print("It's a tie!!!! Try again.")
        continue
    elif player == "R":
        if CPU == "P":
            print(f"player({player}) : CPU({CPU})")
            print("You lose! CPU wins. Try again.")
            break
        if CPU == "S":
            print(f"player({player}) : CPU({CPU})")
            print("You win!!! CPU lost.")
            break
    elif player == "S":
        if CPU == "R":
            print(f"player({player}) : CPU({CPU})")
            print("You lose! CPU wins. Try again.")
            break
        if CPU == "P":
            print(f"player({player}) : CPU({CPU})")
            print("You win!!! CPU lost.")
            break
    elif player == "P":
        if CPU == "S":
            print(f"player({player}) : CPU({CPU})")
            print("You lose! CPU wins. Try again.")
            break
        if CPU == "R":
            print(f"player({player}) : CPU({CPU})")
            print("You win!!! CPU lost.")
            break
