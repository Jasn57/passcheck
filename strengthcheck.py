# import charecters
from utils.py import U_LETTERS
from utils.py import L_LETTERS
from utils.py import NUMBERS
from utils.py import SYMBOLS

GOOD_PS = 10  # threshold for password strength points

# calculate points
def calculate_points(password: str) -> int:
    points = 0
    if any(char in L_LETTERS for char in password):
        points += 1
    if any(char in U_LETTERS for char in password):
        points += 2
    if any(char in NUMBERS for char in password):
        points += 3
    if any(char in SYMBOLS for char in password):
        points += 4
    return points

    # calculate points
        points = calculate_points(password)
        print(f'You have {points} points')

        # if great
        if points > GOOD_PS:
            print('Your password is great')

        # if good
        elif points == GOOD_PS:
            print('Your password is good')
            response = input('Would you like to make your password better y or n: ').lower()
            if response == 'y':
                new_password = password + random.choice(SYMBOLS) + random.choice(NUMBERS)
                print(f'Your new password is {new_password}')
            else:
                print('Okay no changes made.')

        # if bad
        else:
            print('Your password is bad')
            response = input('Would you like a new password? y or n: ').lower()
            if response == 'y':
                new_password = generate_new_password()
                print(f'Your new password is {new_password}')
            else:
                print('Okay no changes made.')

    elif request == '2':
        new_password = generate_new_password()
        print(f'Your new password is {new_password}')

    else:
        print("Invalid option Please type 1 or 2.")
