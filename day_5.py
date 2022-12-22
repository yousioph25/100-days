#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letter = []
nr_symbol = []
nr_number = []
for i in range(0, nr_letters):
    nr_letter.append(random.choice(letters))
for i in range(0, nr_numbers):
    nr_number.append(random.choice(numbers))
for i in range(0, nr_symbols):
    nr_symbol.append(random.choice(symbols))
password =nr_letter + nr_symbol + nr_number

# Easy Challenge
print("Your password is :", *password)

# Hard Challenge
new_password = random.shuffle(password)
print("Your authentic password is: ", *new_password)