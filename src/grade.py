from utils import U_LETTERS, L_LETTERS, NUMBERS, SYMBOLS

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
