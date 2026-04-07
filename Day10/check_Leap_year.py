def is_leap_year(year):
    if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
        return True
    else:
        return False

input_year = int(input("Which year to you check? "))
print(is_leap_year(input_year))