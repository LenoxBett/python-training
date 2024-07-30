# Write a program input a password. Give them only 4 attempts
#  to check the passwords entered against “admin@123”. If the password is correct access is granted.
#  After you show them a message , the account is blocked.

attempt = 4
correct_password = "admin@123"

for i in range(1,5):
    password = input("enter password: ")

    if password == correct_password:
        print("access granted")
        break
    else:
        remaining = attempt - 1
        if remaining > 0:
            print("incorrect password re-enter")
        else:
            print("account blocked")




