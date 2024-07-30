# Prompt the user for a number either on a form input or the terminal.print
#  Depending on whether the number is even or odd, 
# display  either “odd” or “even” to the user.

user = input("enter number: ")

number = int(user)

if number % 2 == 0:
    print(f"{number} even number")
else:
    print(f"{number} odd number")


