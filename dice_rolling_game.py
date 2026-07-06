# Ask: roll the dice?
# If user enters 'yes'
# Show the result (Thanks for playing!)
# Loop back to ask again
# Roll the dice
# If user enters 'no'
# Exit the game (Thanks for playing!)

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        result1 = random.randint(1, 6)
        result2 = random.randint(1, 6)
        print(f'You rolled a {result1} and a {result2}. Thanks for playing!')
    elif choice == 'n':
        print('Maybe another time.')
        break
    else:
        print('Invalid input. Please enter "y" or "n".')