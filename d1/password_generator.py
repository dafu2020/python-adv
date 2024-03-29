# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter_list = []
symbol_list = []
num_list = []
for i in range(0, nr_letters):
    letter_list.append(random.choice(letters))


for i in range(0, nr_symbols):
    symbol_list.append(random.choice(symbols))


for i in range(0, nr_numbers):
    num_list.append(random.choice(numbers))

final_list = letter_list + symbol_list + num_list
# print(final_list)

final_pw = ''

while len(final_list) > 0:
    i = random.choice(final_list)
    final_pw += i
    final_list.remove(i)

print(f"Your password is: {final_pw}")
