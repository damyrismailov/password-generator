letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
ran1 = letters + numbers
ran2 = symbols
ran3 = ran1 + ran2

import random
print("Welcome to the PyPassword Generator!")
choice1 = input("Would you like a 'RANDOM' password or to 'CREATE' a password?\n").lower()
password = ""
if choice1 == 'create':

  nr_letters = int(input("How many letters would you like in your password?\n"))
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
  for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)
  for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)
  password_as_list = list(password)
  random.shuffle(password_as_list)
  password = "".join(password_as_list)
  print(password)

if choice1 == 'random':
 nr_random = int(input(f"How many characters would you like in your password?\n"))
 for ran in range(1,nr_random + 1):
  password += random.choice(ran3)

 password_as_list = list(password)
 random.shuffle(password_as_list)
 password = "".join(password_as_list)
 print(password)
