from Calculator_ascii_art import logo

def is_addition(num1, num2):
    return num1 + num2

def is_substraction(num1, num2):
    return num1 - num2

def is_multiplication(num1, num2):
    return num1 * num2

def is_division(num1, num2):
    return num1 / num2


operations = {
    "+" : is_addition,
    "-" : is_substraction,
    "*" : is_multiplication,
    "/" : is_division
}

def calculator():
    print(logo[0])
    should_accumulate = True
    number1 = float(input("What's the first number? : "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operator = input("Pick an operation: ")

        number2 = float(input("What's the next number? :"))

        result = operations[operator](number1,number2)
        print(f"{number1} {operator} {number2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.").lower()

        if choice == "y":
            number1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()