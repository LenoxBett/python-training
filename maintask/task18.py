# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 

basic = float(input("enter basic: "))
benefits = float(input("enter benefits: "))
gross_salary = basic + benefits

nhdf = gross_salary * 0.015
if gross_salary <= 18000:
    nssf = gross_salary * 0.06
else:
    nssf = 18000 * 0.06
# print(nssf)

taxable_income = gross_salary - (nssf + nhdf)
print(taxable_income)


