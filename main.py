# Get password
password = input("Enter your password: ")
print(f'Your password is {password}')

# define charecters
u_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%"

# Set default points
points = 0

# Add points based
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
