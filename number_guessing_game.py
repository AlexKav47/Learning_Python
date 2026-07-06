# User asked to guess number between 1 and 100
# User guesses a number 
# If guessed correctly, show a message (You guessed correctly!)
# If gussed incorrectly, show a message (Try Again!)
# Look back to ask again

import random

secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < secret_number:
            print('Too Low!')
        elif guess > secret_number:
            print('Too High!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')