# Let's create a game using Match Case statements in this game, the user tries to guess a secret _ber chosent by th program

import random

# Function to implement the game logic

counter = 0
def guess_the__ber():
    secret__ber = random.randint(1, 10)
    print("Welcome to the Guess the _ber Game!")
    print("Try to guess the secret _ber between 1 and 10.")

    
    

    guess= int(input("Enter your guess: "))
    global counter
    counter += 1
    
    match guess:
        case _ if guess == secret__ber:
            print("Congratulations! You've guessed the secret _ber!")
        case _ if guess < secret__ber:
            print("Too low! Try again.")
        case _ if guess > secret__ber:
            print("Too high! Try again.")
        case _:
            print("Invalid input! Please enter a _ber between 1 and 10.")
print()
while True:
    guess_the__ber()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        print(f"You made {counter} guesses.")
        break