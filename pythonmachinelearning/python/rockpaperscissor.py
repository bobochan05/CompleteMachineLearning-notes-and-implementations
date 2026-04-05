#rock paper scissor exercise 
#WAP to play rock paper scissor game
import random
choices= ['rock', 'paper', 'scissor']
user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
if user_choice not in choices:
 {
    print("Invalid choice! Please choose rock, paper, or scissor.")
 }
else:
    def play_game():
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
 
            play_game()
        else:
            print("Thanks for playing!")
    play_game()
    play_game()
# This code implements a simple rock-paper-scissors game where the user can play against the computer.

