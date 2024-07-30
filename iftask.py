# Take three inputs from a user, separately. Print the largest of the numbers.
    # Hint: Determine what type of data is taken in as input

num1 = int(input("enter the 1st number"))
num2 = int(input("enter the 2nd number"))
num3 = int(input("enter the 3rd number"))

if(num1 > num2) and (num1 > num3):
    print(f"bigger number is  {num1}")
elif(num2 > num1) and (num2 > num3):
    print(f"bigger number is {num2}") 
else:
    print(f"bigger number is {num3}")

# Take as input from a user the temperature if the temperature is above 30°C display
    #  “The temperature is too high”, otherwise display “Normal temperature”

temperature = float(input("Enter the temperature in Celsius: "))

# Check if the temperature is above 30°C 
if temperature >= 30:
    print("The temperature is too high")
else:
    print("Normal temperature")
     
# take as input from a user the temperature
    # if the temp is above 30 c display
    #"the temp is too high", btwn 15 and 30 display
    # "mormal temp " otherwise display low temp

temp = float(input("enter temperature"))

if (temp > 30):
    print("temp is too high")
elif(temp >=15 ):
    print("normal temp")
else:
    print()






# write a program to check whether a person is eligible for voting or not

# Get age input from the user
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")






