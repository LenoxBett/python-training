# Write a program called stars. It should prompt the user for a number, 
# and it should print the number of stars till the number entered.

num_stars = int(input("enter number: "))

# if num_stars > 0:
#    for  range(num_stars):
#     print('*')
# else:
#     print()


for i in range(0,num_stars):
    print('*' * i)
