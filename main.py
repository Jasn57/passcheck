def main():
    request = input('Want to fix your password type 1 or make a new one type 2: ').strip()

    if request == '1':
        password = input("Enter your password: ")
        print(f'Your password is {password}')

        