import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','&','*','(',')']

print("Welcome to the PyPassword Generator!")
letter_of_pass = int(input("How many letters would you like in your password?\n"))
symbol_of_pass = int(input("How many symbols would you like?\n"))
numbers_of_pass = int(input("How many numbers would you like?\n"))

# # Easy Level to Create password
# password = ""
# for char in range(1,letter_of_pass+1):
#     password += random.choice(letters)
#
# for sym in range(1, symbol_of_pass+1):
#     password += random.choice(symbol)
#
# for num in range(1, numbers_of_pass+1):
#     password += random.choice(numbers)
#
# print(f"Your Password : {password}")

# Hard Level
password_list = []
for char in range(1,letter_of_pass+1):
    password_list.append(random.choice(letters))

for sym in range(1, symbol_of_pass+1):
    password_list.append(random.choice(symbol))

for num in range(1, numbers_of_pass+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

# password = ""
# for i in password_list:
#     password += random.choice(password_list)

print(f"Your Password : {password}")