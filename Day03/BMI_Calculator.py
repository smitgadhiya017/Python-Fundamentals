print("Welcome to BMI Weight Calculator")
weight = float(input("What is your Weight?"))
height = float(input("What is your Height?"))

bmi = weight / (height ** 2)
if bmi < 18.5 :
    print("Under Weight")
elif bmi < 25:
    print("Normal Weight")
else:
    print("Over Weight")