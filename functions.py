# defining function
def hello(a):
    print(f"Hello {a}")

# call the function
name = input("enter your name")
hello(name)

# parameters & arguments

def triangle(b,h):   
    area = 0.5 * (b * h)
    print(area)

base = float(input("enter base: "))
height = float(input("enter height: "))
triangle(base, height)
 
# write a function to 
# calculate the area of a rectangle
# after taking length and width from the user

def rectangle(l,w):
    area = l * w
    print(area)

length = float(input("enter length: "))
width = float(input("enter width: "))
rectangle(length, width)



# Prompt the user for a number either on 
# a form input or the terminal.print
#  Depending on whether the number is even or odd, 
# display  either “odd” or “even” to the user.

def num(p):
    if p % 2 == 0:
        print("even number")
    else:
        print("odd number")

number = float(input("enter number: "))
num(number)