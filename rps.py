import random

def userchoice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def computerchoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = userchoice()
        computer_choice = computerchoice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score}")

if __name__ == "__main__":
    main()
