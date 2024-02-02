import random

def get_user_choice():
    """Get the user's choice."""
    print("\n1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("Enter your choice: "))
    while user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please choose again.")
        user_choice = int(input("Enter your choice: "))
    return user_choice

def get_computer_choice():
    """Get the computer's choice."""
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    """Determine the winner."""
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    winning_combinations = {(1, 3): 'breaks', (2, 1): 'covers', (3, 2): 'cuts'}

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice, computer_choice) in winning_combinations:
        return f"You win! {choices[user_choice]} {winning_combinations[(user_choice, computer_choice)]} {choices[computer_choice]}"
    else:
        return f"You lose! {choices[computer_choice]} beats {choices[user_choice]}"

def play_game():
    """Play the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()