while True:
    import random
        
    print("------------------------------------------")
    print("Rock Paper Scissors")
    print("------------------------------------------")


    list = ["Rock", "Paper", "Scissors"]

    guess = str(input("Rock, Paper or Scissors?\n: ")).capitalize()

    if guess not in list:
        print("------------------------------------------")
        print("ERROR: Enter only Rock, Paper or Scissors.")
        print("------------------------------------------")
        exit()

    computer_guess = random.choice(list)


    print("-----------------------------------")
    print("Computer guess:",computer_guess + ".")
    print("-----------------------------------")
    print("Your guess:", guess + ".")
    print("-----------------------------------")


    if computer_guess == guess:
        print("Draw!")
    elif computer_guess == "Rock" and guess.lower() == "scissors":
        print("You Lost!")
    elif computer_guess == "Rock" and guess.lower() == "paper":
        print("You Won!")

    elif computer_guess == "Scissors" and guess.lower() == "rock":
        print("You Won!")
    elif computer_guess == "Scissors" and guess.lower() == "paper":
        print("You lost!")

    elif computer_guess == "Paper" and guess.lower() == "rock":
        print("You lost!")
    elif computer_guess == "Paper" and guess.lower() == "scissors":
        print("You Won!")

    else:
        print("Error!")

    print("-----------------------------------")

    while True:
        play_again = str(input("Want to play again? y/n\n: "))

        if play_again.lower() in ("y", "yes", "n", "no"):
            break
        print("ERROR: Enter only y/n.")
    if play_again.lower() == "y" and "yes":
        continue
    elif play_again.lower() == "n" and "no":
        print("Bye!")
        break
    else:
        print("Enter y/n.")
        break
