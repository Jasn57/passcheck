import random

# Get password
password = input("Enter your password: ")
print(f'Your password is {password}')

# Define characters
u_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%"

# Set default points
points = 0

# Set password tier
good_ps = 10

# Add points 
if any(char in l_letters for char in password):
    points += 1

if any(char in u_letters for char in password):
    points += 2

if any(char in numbers for char in password):
    points += 3

if any(char in symbols for char in password):
    points += 4

# Print total
print(f'You have {points} points')

# Rank password
if points > good_ps:
    print('Your password is great')

elif points == good_ps:
    print('Your password is good')
    response = input('Would you like to make your password better? (y or n): ').lower()

    if response == 'y':
        new_number = random.choice(numbers)
        new_symbol = random.choice(symbols)
        new_ps = password + new_symbol + new_number
        print(f'Your new password is {new_ps}')

    elif response == 'n':
        print('Okay, keeping your password.')

else:
    print('Your password is bad')
    response = input('Would you like a new password? (y or n): ').lower()

    if response == 'y':
        new_l_letter1 = random.choice(l_letters)
        new_l_letter2 = random.choice(l_letters)
        new_l_letter3 = random.choice(l_letters)
        new_l_letter4 = random.choice(l_letters)
        new_l_letter5 = random.choice(l_letters)
        new_l_letter6 = random.choice(l_letters)

        new_u_letter1 = random.choice(u_letters)
        new_u_letter2 = random.choice(u_letters)

        new_number = random.choice(numbers)
        new_symbol = random.choice(symbols)

        new_ps = (new_u_letter1 + new_l_letter1 + new_l_letter2 + new_l_letter3 + new_l_letter4 +
                  new_number + new_l_letter5 + new_l_letter6 + new_u_letter2 + new_symbol)

        print(f'Your new password is {new_ps}')

    elif response == 'n':
        print('Okay, keeping your password.')
