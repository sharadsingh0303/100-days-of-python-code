import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Pypassword Generator")
nr_letters = input("How many letter would you like in your password?\n")
nr_symbols = input("How many symbols would you like?\n")
nr_numbers = input("How many letter would you like?\n")


if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    print("Invalid value, enter a number instead.")
else:
    password = []

    random_letter = random.randint(0, 51)
    for i in range(0, int(nr_letters)):
        random_letter = random.randint(0, 51)
        password.append(letters[random_letter])
