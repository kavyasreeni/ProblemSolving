# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap=False
    if year%400==0:
        return True
    elif (year%4==0 and not (year%100==0)) :
        return True
    return leap

year_pass = is_leap(int(input('Enter number: ')))
print(year_pass)
