# Write a program which accepts email as form input or
#  from terminal. Validate the email by checking if it's a valid email. 

email = input("enter the email: ")


# if email.count("@") == 1 and email.count(".") > 0:
#     print("email is valid")
# else:
#     print("email is invalid")

for i in range(0,len(email)):
    print(email[i])
    if "@" in email and "."in email:
        if email[i] == "@":
          at = i
          print(at)
        elif email[i] == ".":
          dot = i
          print(dot)
        # else:
        #   print("invalid")

          if at < dot and at > 1 and dot < len(email)-1:
            print("valid")
else:
    print("invalid")
