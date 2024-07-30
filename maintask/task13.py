# Write a program that takes the email and password as input from a user and checks 
# if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print 
#  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

attempt = 3

# email = input("enter email:" )
# password = input("enter password: ")

correct_email = "admin@mail.com"
correct_password = "admin@123"

for i in range(1,4):
    email = input("enter email: ")
    password = input("enter password: ")
    if email == correct_email and password == correct_password:
        print("access granted")
        break
    else:
        # attempt += 1
        remaining = attempt - i
        if remaining > 0:
           print(f"inavlid {remaining}")
        else:
            print("you have been blocked")
        





