import random

def dice_rolling_game():
    dice_sides = 6
    while True:
        user_input = input('> Roll the dice? (y/n): ').lower()
        if user_input == 'y':
            first_num = random.randint(1, dice_sides)
            second_num = random.randint(1, dice_sides)
            if first_num == second_num:
                print(f"(({first_num}, {second_num}) You rolled doubles! You win!)")
            else: 
                print(f"({first_num}, {second_num})")
        elif user_input == 'n':
            print('Thanks for playing')
            break
        else:
            print('Invalid input. Please enter "y" or "n".')


def number_guessing_game():
    number_to_guess = random.randint(1,100)
    while True: 
        try:
            user_guess = int(input("Guess a number between 1 and 100 inclusive: "))
            if user_guess > number_to_guess:
                print('Too high!')
            elif user_guess < number_to_guess:
                print('Too low!')
            elif number_to_guess == user_guess:
                print("Congratulations! You guessed the number")
                break
        except ValueError:
            print("Please enter a number")
            



def rock_paper_scissors():
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'
    emojis = {ROCK: '🪨', PAPER:'📄', SCISSORS:'✂️'}
    choices = tuple(emojis.keys())
    
    while True:
        user_choice = input("Rock, paper or scissors?(r/p/s): ")
        if user_choice not in choices:
            print("Invalid choice")
            continue
            
        computer_choice = random.choice(choices)
            
        print(f'you chose {emojis[user_choice]}')
        print(f'computer chose {emojis[computer_choice]}')
        
        if user_choice == computer_choice:
            print("Tie!")
        elif (
            (user_choice == ROCK and computer_choice == PAPER) or
            (user_choice == SCISSORS and computer_choice == ROCK) or
            (user_choice == PAPER and computer_choice == SCISSORS)):
            print('You lose')
        else:
            print('You win')
            
        should_continue = input("Continue?(y/n): ")
        if should_continue == 'n':
            print('Thanks for playing')
            break
            
rock_paper_scissors()