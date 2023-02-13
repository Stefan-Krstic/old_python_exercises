import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(f"{'-' * 49}\nWelcome to Stefan's [Password Generator] program!\n{'-' * 49}")
nr_letters = int(input(f"How many letters would you like in your password?\n     "))
nr_symbols = int(input(f"{'-' * 27}\nHow many symbols would you like?\n     "))
nr_numbers = int(input(f"{'-' * 27}\nHow many numbers would you like?\n     "))

a = []

for q in range(0, nr_letters):
    a += random.choice(letters)

for q in range(0, nr_symbols):
    a += random.choice(symbols)

for q in range(0, nr_numbers):
    a += random.choice(numbers)

random.shuffle(a)

password = ""

for q in a:
    password += q

print(f"\nYour new Password is:\n {'-' * 25}\n  {password}\n {'-' * 25}")
