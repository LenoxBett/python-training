# Continue with the same program and find the person's 
# PAYEE using the taxable income above.
# 0 – 24,000	10%
# On the next 8,333	25%
# Remaining amount over 32,333	30%
# Personal Relief: KES 2,400.00 per month
# Minimum Taxable Income: KES 24,001.00 per month

basis_salary = float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))
gross_salary = basis_salary + benefits
# nssf = gross_salary * 0.06
nhdf = gross_salary * 0.015
# relief = 2400
if gross_salary <= 18000:
    nssf = gross_salary * 0.06
else:
    nssf = 18000 * 0.06
# print(nssf)

taxable_income = gross_salary - (nssf + nhdf)


if taxable_income < 24000:
    paye = 0
elif taxable_income > 24000 and taxable_income <= 32333:
    paye = (24000 * 0.1) + ((taxable_income - 24000) * 0.25)
elif taxable_income > 467667 and taxable_income <= 500000:
    paye = (24000 * 0.1) + ((taxable_income - 32333) * 0.25)
    elif taxable_income > 3000

