import random

computer_number = random.randint(1, 100)
counter = 0
while True:
    player_input = input('Guess the number (1-100): ')
    counter += 1

    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue

    player_number = int(player_input)
    if player_number == computer_number:
        print('You guess it!')
        if counter < 3:
            print('Excellent!!!')
        else:
            print('Good job!')
        print(f'Number of attempts: {counter}')
        break
    elif player_number > computer_number:
        print('Too Hight!')
    else:
        print('Too Low!')