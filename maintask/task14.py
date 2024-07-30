# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only or otherwise 
# display an error “invalid character entered” and take the user to re-enter the inputs .

while True:
    try:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        result = num1 + num2
        print("result")
        break
    except ValueError:
        print("invalid character enered")

