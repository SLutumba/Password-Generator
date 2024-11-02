import random
from string import ascii_uppercase, ascii_lowercase, punctuation, digits, ascii_letters


def main():
    all_chars = punctuation + digits + ascii_letters
    print("This program will generate a password based on user inputs.\n")
    while True:
        try:
            length = int(input("Enter the desired length of your password (from 8 to 16 characters) or 0 to end program: "))
            if length == 0:
                print("Program ended.\n")
                break
            elif length < 0:
                print("Enter a positive number.\n")
            elif length > 16:
                print("Length is too long. Use between 8 and 16.")
            elif length < 8:
                print("Length is too short. Use between 8 and 16.")
            else:
                password = ''.join(random.sample(all_chars, k=length))
                print(f"'{password}' is your generated password.\n")
        except ValueError:
            print("Please enter an integer")
if __name__ == "__main__":
    main()