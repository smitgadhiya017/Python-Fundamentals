print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
split_bill = int(input("How many people to split the bill?"))
ans = (total_bill * tip/100 + total_bill) / split_bill
print(f"Each person should pay: ${round(ans,2)}")