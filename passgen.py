# import random
import random

# import charecters
from utils.py import U_LETTERS
from utils.py import L_LETTERS
from utils.py import NUMBERS
from utils.py import SYMBOLS

# set variable for new ps
new_password = generate_new_password()

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
