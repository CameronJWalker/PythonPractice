# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print 
# out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

p1 = input("rock, paper, scissors, SHOOT: ")
p2 = input("rock, paper, scissors, SHOOT: ")

rock = "rock"
scissors = "scissors"
paper = "paper"

while p1 == "rock":
    if p2 == "scissors":
        print("Player 1 wins!")
    elif p2 == "paper":
        print("Player 2 wins!")
    else:
        print("Draw!")
    break
while p1 == "paper":
    if p2 == "scissors":
        print("Player 2 wins!")
    elif p2 == "rock":
        print("Player 1 wins!")
    else:
        print("Draw!")
    break
while p1 == "scissors":
    if p2 == "rock":
        print("Player 2 wins!")
    elif p2 == "paper":
        print("Player 1 wins!")
    else:
        print("Draw!")
    break