# Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254..
#  or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 

user = input("enter phone number: ")

if user [0:4] == "+254" and len(user == 13):
    print(user, "is valid number")
elif user[0:2] == ("07" or "01") and len(user) == 10:
    print("+254" + user[1:])
elif user[0:3] == "254" and len(user) == 12:
    print("+" + user)
elif user[0:1] == ("1" and "7" )and len(user) == 9:
    print("+254" + user)
else:
    print("inavlid number")
   




