
'''
Python program that simulates a game of Rock, Paper, Scissors between the user and the computer.
The program Define the possible choices, 
Get the user's choice, Generate a random choice for the computer, 
Determine the winner based on the rules of Rock, Paper, Scissors.
'''
import random

# Score dictionary
score = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

# Possible choices
choices = ['rock', 'paper', 'scissors']

def pick_computer_move():
    return random.choice(choices)

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        return "You win"
    else:
        return "You lose"

def update_score(result):
    if result == "You win":
        score["wins"] += 1
    elif result == "You lose":
        score["losses"] += 1
    else:
        score["ties"] += 1

def show_score():
    print(f"Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop.")

    while True:
        player_move = input("\nYour move: ").strip().lower()
        if player_move == 'quit':
            break
        if player_move not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_move = pick_computer_move()
        result = determine_winner(player_move, computer_move)

        print(f"You played: {player_move}")
        print(f"Computer played: {computer_move}")
        print(result)

        update_score(result)
        show_score()

    print("\nFinal score:")
    show_score()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
