import random

# Define characters
U_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SYMBOLS = "!@#$%"

GOOD_PS = 10  # threshold for password strength points


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


def generate_new_password() -> str:
    # Generate a new password
    parts = [
        random.choice(U_LETTERS),
        random.choice(L_LETTERS),
        random.choice(L_LETTERS),
        random.choice(L_LETTERS),
        random.choice(L_LETTERS),
        random.choice(NUMBERS),
        random.choice(L_LETTERS),
        random.choice(L_LETTERS),
        random.choice(U_LETTERS),
        random.choice(SYMBOLS),
    ]
    return "".join(parts)


def main():
    request = input('Want to fix your password (type 1) or make a new one (type 2): ').strip()

    if request == '1':
        password = input("Enter your password: ")
        print(f'Your password is {password}')

        # calculate points
        points = calculate_points(password)
        print(f'You have {points} points')

        # if great
        if points > GOOD_PS:
            print('Your password is great')

        # if good
        elif points == GOOD_PS:
            print('Your password is good')
            response = input('Would you like to make your password better? (y or n): ').lower()
            if response == 'y':
                new_password = password + random.choice(SYMBOLS) + random.choice(NUMBERS)
                print(f'Your new password is {new_password}')
            else:
                print('Okay no changes made.')

        # if bad
        else:
            print('Your password is bad')
            response = input('Would you like a new password? (y or n): ').lower()
            if response == 'y':
                new_password = generate_new_password()
                print(f'Your new password is {new_password}')
            else:
                print('Okay, no changes made.')

    elif request == '2':
        new_password = generate_new_password()
        print(f'Your new password is {new_password}')

    else:
        print("Invalid option. Please type '1' or '2'.")


if __name__ == "__main__":
    main()
