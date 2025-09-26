import random

# import charecters
from utils import U_LETTERS, L_LETTERS, NUMBERS, SYMBOLS

# generate new ps
def generate_new_password() -> str:
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
