import random

CHOICES = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}


def get_user_choice():
    while True:
        choice = input('Rock, Paper, or Scissors? (r/p/s or q to quit): ').strip().lower()
        if choice == 'q':
            return None
        if choice in CHOICES:
            return choice
        print('Invalid input. Please enter r, p, s, or q.')


def get_computer_choice():
    return random.choice(tuple(CHOICES.keys()))


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'

    winning_pairs = {
        'r': 's',
        'p': 'r',
        's': 'p',
    }
    return 'user' if winning_pairs[user_choice] == computer_choice else 'computer'


def main():
    user_score = 0
    computer_score = 0
    ties = 0

    print('Welcome to Rock, Paper, Scissors!')

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print('\nThanks for playing!')
            print(f'Final score -> You: {user_score}, Computer: {computer_score}, Ties: {ties}')
            break

        computer_choice = get_computer_choice()
        print(f'You chose {CHOICES[user_choice]}.')
        print(f'Computer chose {CHOICES[computer_choice]}.')

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            ties += 1
            print("It's a tie!")
        elif winner == 'user':
            user_score += 1
            print('You win!')
        else:
            computer_score += 1
            print('Computer wins!')

        print(f'Score -> You: {user_score}, Computer: {computer_score}, Ties: {ties}\n')


if __name__ == '__main__':
    main()
