my_tuple = ("Lenox", "Simon", "Brina")
print(my_tuple)
my_list = list(my_tuple)
print(my_list)
my_list[0] = "Moha"
# print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days[2])
print(len(days))

day1 = list(days)
day1[3] = "thur"
day2 = tuple(day1)
print(day2)


