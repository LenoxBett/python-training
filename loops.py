fruits = ["apple", "banana", "cherry", "kiwi"]
for fruit in fruits:
    print(fruit)
print(fruits)

me = range(0,1000)
for i in range(0,1001):
    if i % 2 == 0:
        print (i)

# display numbers divisible by 7
        #  between 0 and 500

divisible_by_7 = []

print(divisible_by_7)

for i in range (0,501):
    if i % 7 == 0:
        divisible_by_7.append(i)
        
print(divisible_by_7)

numbers = list(range(0,500))
print(numbers)
for i in numbers:
    if i % 7 == 0:
        print(i)