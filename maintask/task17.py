# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

basic = float(input("enter basic: "))
benefits = float(input("enter benefits: "))
gross_salary = basic + benefits

nhdf = gross_salary * 0.015
print(nhdf)

