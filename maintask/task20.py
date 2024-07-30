# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

basis_salary = float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))
gross_salary = basis_salary + benefits


if gross_salary < 6000:
    nhif = 150
elif gross_salary >= 6000 and gross_salary < 8000:
    nhif = 300
elif gross_salary >= 8000 and gross_salary < 12000:
    nhif = 400
elif gross_salary >= 12000 and gross_salary < 15000:
    nhif = 500
elif gross_salary >= 15000 and gross_salary < 20000:
    nhif = 600
elif gross_salary >= 20000 and gross_salary < 25000:
    nhif = 750
elif gross_salary >= 25000 and gross_salary < 30000:
    nhif = 850
elif gross_salary >= 30000 and gross_salary < 35000:
    nhif = 900
elif gross_salary >= 35000 and gross_salary < 40000:
    nhif = 950
elif gross_salary >= 40000 and gross_salary < 45000:
    nhif = 1000
elif gross_salary >= 45000 and gross_salary < 50000:
    nhif = 1100
elif gross_salary >= 50000 and gross_salary < 60000:
    nhif = 1200
elif gross_salary >= 60000 and gross_salary < 70000:
    nhif = 1300
elif gross_salary >= 70000 and gross_salary < 80000:
    nhif = 1400
elif gross_salary >= 80000 and gross_salary < 90000:
    nhif = 1500
elif gross_salary >= 90000 and gross_salary < 100000:
    nhif = 1600
else:
    nhif = 1700

print(nhif)
