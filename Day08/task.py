# # function
from pygments.lexer import combined

# def greet():
#     print("Hello")
#     print("How Are You?")
#     print("Byy")
#
# greet()
#
# # Functions that allow for inputs
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# name = input("What's your name :")
# greet_with_name(name)

# # Life in Weeks Exercise
#
# def life_in_week(age):
#     remaining_years = 90 - age
#     remaining_week = remaining_years * 52
#     print(f"Total remaining week for reach 90 years : {remaining_week}")
#
# age = int(input("What's your Age :"))
# life_in_week(age)


# # Functions with more than 1 input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
# name = input("What's your name :")
# location = input("What's your location :")
# greet_with(name,location)


# Love Calculator Exercise
def calculate_love_score(name1, name2):
    combined = name1 + name2
    count_True = 0
    count_Love = 0
    for letter in combined:
        if letter in "true":
            count_True += 1

        if letter in "love":
            count_Love += 1

    total = str(count_True) + str(count_Love)
    print(total)

print("True Love Calculator")
name1 = input("Enter First name :").lower()
name2 = input("Enter Second number :").lower()
calculate_love_score(name1, name2)

