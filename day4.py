import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# This is a basic rock paper scissors game
print("Welcome to the rock paper scissors game")
# It ask for an input from the user
player_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))

game = ["Rock", "Paper", "Scisssors"]
# This line changes the index chosen by the player to a string
player_choice = game[player_choice]
print(player_choice)

# Using the random module the computer choise is chosen automatically
computer = random.randint(0, len(game) -1)
computer_choice = game[computer]
print(computer_choice)

# The logic behind the game
if player_choice == "Rock":
    print(f"Player plays rock {rock}")
    if computer_choice == "Rock":
        print(f"Computer plays rock {rock}")
        print("The game is a draw")
    elif computer_choice == "Paper":
        print(f"computer plays paper {paper}")
        print("Computer Wins")
    else: 
        print(f"Computer plays scissors {scissors}")
        print("Player wins")
if player_choice == "Paper":
    print(f"Player plays paper {paper}")
    if computer_choice == "Rock":
        print(f"Computer plays rock {rock}")
        print("Player wins")
    elif computer_choice == "Paper":
        print(f"computer plays paper {paper}")
        print("The game ends in a draw")
    else: 
        print(f"Computer plays scissors {scissors}")
        print("Computer wins")
if player_choice == "Scissors":
    print(f"Player plays scissors {scissors}")
    if computer_choice == "Rock":
        print(f"Computer plays rock {rock}")
        print("Computer wins")
    elif computer_choice == "Paper":
        print(f"computer plays paper {paper}")
        print("Player Wins")
    else: 
        print(f"Computer plays scissors {scissors}")
        print("The game ends in a draw")
