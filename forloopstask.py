# 1. Write a program that displays a
#  numbers 1 to 50 inside a list.
num = list(range(1,51))
print(num)

# 2. From 1 above display the ones
#  divisible by 7 or 5 inside a list.
num2 = []
for i in num2:
    if (i % 7 == 0) or (i % 5 == 0):
        num2.append(i)
print(num2)    

# 3. Find sum and average of values in
#  the range between 10 to 40
sum = 0 
num3 = []
for i in range(10,41):
    sum = sum + i 
    num3.append(i)
    avg = sum / len(num3)
print(avg)

# 4. Put in a list the first 10 odd numbers between 10 to 50.
    
# Initialize an empty list to store the odd numbers
odd_numbers = []

for i in range(10,51):
    if i % 2!= 0:
        odd_numbers.append(i)
        # num1 = odd_numbers[:10]

print(odd_numbers[:10])
# Loop through numbers from 10 to 50 and add odd numbers to the list
# for num in range(11, 51, 2):
#     odd_numbers.append(num)

# Print the list of odd numbers
# print(odd_numbers)

# 5. write a program that takes a number as input and prints 
# its multiplication table up to 10 using a for loop.

# Python program to print the multiplication table of a number up to 10

# Take user input for the number
number = int(input("Enter a number: "))

# Print the multiplication table using a for loop
# print(f"Multiplication table for {number}:")

for i in range(0, 11):
    result = number * i
    print(result)

# 6. write a program that counts and prints the number 
# of even numbers between 1 and 50 using a for loop
# Python program to count and print the number of even numbers between 1 and 50

# Initialize a counter for even numbers
even_count = 0

# Loop through numbers from 1 to 50 and count even numbers
for num in range(1, 51):
    if num % 2 == 0:
        even_count += 1

# Print the count of even numbers
print(f"The number of even numbers between 1 and 50 is: {even_count}")
 

# display = []
# for i in range(1,51):
#     if i % 2 == 0:
#         display.append

# print(display)
# print(len(display))



count = 0 
for i in range(1,51):
    if i % 2 == 0:
        count = count + 1
        print(count)