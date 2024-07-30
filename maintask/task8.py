# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.

speed = float(input("enter speed in (km/hr)"))
speed_limit = 70
demerits_points = 0

# if speed > speed_limit:
#     # print("ok")
#     excess_speed = speed - speed_limit
#     demerits_points = excess_speed // 5
# else:
#     demerits_points


# speed = float(input("enter speed in(km/hr)"))

if speed < speed_limit:
    print("ok")
else:
    excess_speed = speed - speed_limit
    demerits_points = excess_speed // 5
    print(f"{demerits_points}")
    if demerits_points > 12:
        print("license suspended")
    else:
        print(f"you have {demerits_points} points ")





