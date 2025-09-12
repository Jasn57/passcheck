import random

# Get password
password = input("Enter your password: ")
print(f'Your password is {password}')

# define characters
u_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%"

# Set default points
points = 0

# set password tier
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

# rank password
if points > good_ps:
    print('Your password is great')

elif points == good_ps:
    print('Your password is good')

    # fix good password 
    new_number = random.choice(numbers)
    new_symbol = random.choice(symbols)
    new_ps = password + new_symbol + new_number
    print(f'Your new password is {new_ps}')

else:
    print('Your password is bad')

    # fix bad password 
    new_number = random.choice(numbers)
    new_symbol = random.choice(symbols)
    new_uletter = random.choice(u_letters)
    new_lletter = random.choice(l_letters)

    new_ps = password + new_uletter + new_lletter + new_symbol + new_number
    print(f'Your stronger password is {new_ps}')
