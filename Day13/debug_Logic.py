def my_function():
    for i in range(1,21): # before debugged code is - for i in range(1, 20)
        if i == 20:
            print("You got it")

my_function()


from random import randint
dice_image = ["1","2","3","4","5","6"]
dice_num = randint(0,6) # before debugged code is - dice_num = randint(1,6)
print(dice_image[dice_num])


year = int(input("What's your year of birth?"))

if year > 1980 and year < 1997:
    print("You are a millennial")
elif year >= 1997: # before debugged code is - elif year > 1997:
    print("You are a Gen Z.")


# Debug code using PyCharm debugger

import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])