# The code below asks the user for some inputs that will be used
# to create a random password.
import random
# below is a list of upper & lower case letters that can be used
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# below is a list of numbers that can be used
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# below is a list of special characters that can be used
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt the user for how many letters, numbers and special chars to use
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# create a list that will be appended and shuffled into a random password
password_list = []
for char in range(1, nr_letters + 1):
	password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
	password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
	password_list += random.choice(numbers)
random.shuffle(password_list)
password = “”
for char in password_list:
	password += char
print(f”Your password is: {password})
