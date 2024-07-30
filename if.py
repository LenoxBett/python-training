a = 12
b = 5

# checking if a is greater than b
if(a>b):
    print("a is greater than b")

else:
    print("b is greater than a")

# take input from a user 
# above 50 give it a pass
#below 50 give a fail 
marks = int(input("enter marks? "))
if(marks > 50) and (marks < 50):
    print("passed")
else:
    print("failed")

    # 80=>100 = A
    # 70=>80 = B
    # 60=>70 = C
    # 50=>60 = D
    # BELOW 50 = E

points = int(input("enter marks ? "))

if(points >= 80) and (points <= 100):
    print("grade is A")
elif(points >= 70) and (points < 80):
    print("grade is B")
elif(points >= 60) and (points <70):
    print("grade is C")
elif(points >= 50 ) and (points < 60):
    print("grade is D")
else:
    print("grade is E")

    # take a number from input
    # write a program that checks if
    # the number is a prime number

num = float(input("enter number? "))
if (num%2!=0):
    print("odd number")
else:
    print("even number")

# the number is even number

if (num%2==0):
    print("even number")
else:
    print("odd number")
