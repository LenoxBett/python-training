# Write a python program that takes from 
# a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks 
# another the average marks ,then a functions that 
# finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

maths = float(input("enter math score: "))
eng = float(input("enter eng score: "))
swa = float(input("enter swa score: "))
sci = float(input("enter sci score: "))
sos = float(input("enter sos score: "))

def total_marks(a,b,c,d,e):
    total_marks = a + b + c + d + e
    print(total_marks)

total_marks = maths + eng + swa + sci + sos


def average_marks(a,b,c,d,e):
    average_marks = (a + b + c + d +e) / 5
    print(average_marks)

average_marks = maths + eng + swa + sci + sos

def grade(a,b,c,d,e):
    average_marks = (a + b + c + d + e) / 5
    results = average_marks
    if results > 79:
        grade = "A"
    elif results >= 60 and results < 79:
        grade = "B"
    elif results >= 49 and results < 60:
        grade = "C"
    elif results >= 40 and results < 50:
        grade = "D"
    else:
        grade = "E"
    print(f"{grade}")

grade(maths, eng, swa, sci, sos)


# Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254..
#  or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 

def validate_and_convert_phone_number(phone_number):

    if phone_number [0:4] == "+254" and len(phone_number == 13):
        num = (phone_number, "is valid number")
    elif phone_number[0:2] == ("07" or "01") and len(phone_number) == 10:
        num = ("+254" + phone_number[1:])
    elif phone_number[0:3] == "254" and len(phone_number) == 12:
        num = ("+" + phone_number)
    elif phone_number[0:1] == ("1" and "7" )and len(phone_number) == 9:
        num = ("+254" + phone_number)
    else:
        num = ("inavlid number")
    return num

phone_number = input("enter phone number: ")
check_in = validate_and_convert_phone_number(phone_number)
print(check_in)

# Implement a program that takes 3 form inputs or from the terminal,
# and stores them in three variables. Return the largest of the three.
# Do this without using the the inbuilt max () function!

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

def numbers(num1, num2, num3):
    if(num1 > num2) and (num1 > num3):
        valid=(f"bigger number is  {num1}")
    elif(num2 > num1) and (num2 > num3):
       valid=(f"bigger number is {num2}") 
    else:
       valid=(f"bigger number is {num3}")
    return valid

check = numbers(num1, num2, num3)
print(check)