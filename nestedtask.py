# 1. write a program that takes a student's score input 
# checks if the scores are between 0 and 100 and
#  prints their grade (A, B, C, D, or F) based on the following conditions:
# A: 90 and above
# B: 80 - 89
# C: 70 - 79
# D 60 - 69
# F: below 60
# otherwise print invalid sore

# Get input for the student's score
score = float(input("Enter the student's score: "))

# Check if the score is within the valid range (0 - 100)
if 0 <= score <= 100:
    # Determine the grade based on the score
    if score >= 90:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    else:
        grade = 'F'

    # Print the grade
    print(f"The student's grade is: {grade}")

else:
    # Print an error message for an invalid score
    print("Invalid score. Please enter a score between 0 and 100.")



# 2 .Write a program that asks the user to input two numbers
# checks if  both numbers are  are positive and then checks if the sum of the numbers is
    #  even or odd.otherwise  print "negative numbers."

# Get input for the first number
num1 = float(input("Enter the first number: "))

# Get input for the second number
num2 = float(input("Enter the second number: "))

# Check if both numbers are positive
if num1 > 0 and num2 > 0:
    # Calculate the sum of the numbers
    sum_of_numbers = num1 + num2

    # Check if the sum is even or odd
    if sum_of_numbers % 2 == 0:
        print(f"The sum of {num1} and {num2} is even.")
    else:
        print(f"The sum of {num1} and {num2} is odd.")
else:
    # Print a message for negative numbers
    print("Negative numbers.")



# 3. Create program that takes the user's input for a 
    # time in 24-hour format and converts it to 12-hour format.
    #  Consider handling cases for noon and midnight appropriately.


# Get input for the time in 24-hour format
time_24_hour = input("Enter the time in 24-hour format (HH:MM): ")

# Split the input into hours and minutes
hours, minutes = map(int, time_24_hour.split(':'))

# Check if the entered time is valid
if 0 <= hours < 24 and 0 <= minutes < 60:
    # Convert to 12-hour format
    am_pm = "AM" if hours < 12 else "PM"
    hours_12_hour = hours % 12 if hours % 12 != 0 else 12

    # Print the converted time
    time_12_hour = f"{hours_12_hour:02d}:{minutes:02d} {am_pm}"
    print(f"The time in 12-hour format is: {time_12_hour}")
else:
    # Print an error message for an invalid time
    print("Invalid time. Please enter a valid time in 24-hour format.")




