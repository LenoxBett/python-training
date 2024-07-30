# Write a program that prints the largest of
#  4 inputs taken in from a user. 
# Assume that the user would not enter any 
# two numbers which are the same.

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))
num4 = float(input("enter the fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"largest number is {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"largest number is {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"largest number is {num3}")
else:
    print(f"largest number is {num4}")



