##                Scissors cuts Paper
##                Paper covers Rock
##                Rock crushes Lizard
##                Lizard poisons Spock
##                Spock smashes Scissors
##                Scissors decapitates Lizard
##                Lizard eats Paper
##                Paper disproves Spock
##                Spock vaporises Rock
##                and as it always has
##                Rock crushes Scissors.



choice1 = input("Player 1? ").lower()
choice2 = input("Player 2? ").lower()
p1 = "Player 1 wins."
p2 = "Player 2 wins."
if choice1 == "scissors":
    if choice2 == "paper" or choice2 == "lizard":
        print(p1)
    elif choice2 == "spock" or choice2 == "rock":
        print(p2)
elif choice1 == "paper":
    if choice2 == "spock" or choice2 == "rock":
        print(p1)
    elif choice2 == "lizard" or choice2 == "scissors":
        print(p2)
elif choice1 == "rock":
    if choice2 == "lizard" or choice2 == "scissors":
        print(p1)
    elif choice2 == "spock" or choice2 == "paper":
        print(p2)
elif choice1 == "lizard":
    if choice2 == "spock" or choice2 == "paper":
        print(p1)
    elif choice2 == "rock" or choice2 == "scissors":
        print(p2)
elif choice1 == "spock":
    if choice2 == "rock" or choice2 == "scissors":
        print(p1)
    elif choice2 == "paper" or choice2 == "lizard":
        print(p2)
