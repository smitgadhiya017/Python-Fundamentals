from Calculator_ascii_art import logo
print(logo[0])

def is_addition(num1, num2):
    return num1 + num2

def is_substraction(num1, num2):
    return num1 - num2

def is_multiplication(num1, num2):
    return num1 * num2

def is_division(num1, num2):
    return num1 / num2

number1 = float(input("What's the first number? : "))

print("+\n-\n*\n/")

operator = input("Pick an operation: ")

number2 = float(input("What's the next number? :"))
result = 0
if operator == '+':
    result = is_addition(number1,number2)
elif operator == '-':
    result = is_substraction(number1,number2)
elif operator == '*':
    result = is_multiplication(number1,number2)
elif operator == '/':
    result = is_division(number1,number2)

print(f"{number1} {operator} {number2} = {result}")