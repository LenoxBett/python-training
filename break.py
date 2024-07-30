numbers = list(range(1,11))

for i in numbers:
    if i == 6:
        print(f"{i} found")
        break
    else:
        print(f"{i}not found")

print("loop ended")

# write a program that checks if the inputed
#  pin is correct if not give 3 attempts

attempt = 3
corrct_pin = "1978"

for i in range(1,4):
    pin = (input("enter pin: "))

    if pin == corrct_pin:
        print("access granted")
        break
    else:
        remaining = attempt - i
        if remaining > 0 : 
            print("incorrect pin re-enter")
        else:
            print("blocked")








