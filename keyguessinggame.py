import random

def key_guessing_game():
    # Generates random number for key between 1 and 3
    key = random.randint(1, 3)
    
    while True:
        # prompts user to guess the key
        guess = int(input("Guess which key opens the door(1/2/3): "))
        
        # check if guess is correct
        if guess == key:
            print("Congratulations! You guessed the correct key! You can now open the door.")
            break
        else:
            print("Wrong key! Try again.")
        
key_guessing_game()
