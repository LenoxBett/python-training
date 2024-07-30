# Implement a program that takes 3 form inputs or from the terminal,
# and stores them in three variables. Return the largest of the three.
# Do this without using the the inbuilt max () function!


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if(num1 > num2) and (num1 > num3):
    print(f"bigger number is  {num1}")
elif(num2 > num1) and (num2 > num3):
    print(f"bigger number is {num2}") 
else:
    print(f"bigger number is {num3}")


