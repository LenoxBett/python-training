# Write a program that takes input of someone's basic
# salary and benefits, adds them to find the gross salary 
# then uses  the gross salary to find the NHIF.

# Employee's Monthly Gross Salary(Kshs)	Monthly NHIF Contribution (Kshs)
# 5,999	150
# 6,000 - 7,999	300
# 8,000 - 11,999	400
# 12,000 - 14,999	500
# 15,000 - 19,999	600
# 20,000 - 24,999	750
# 25,000 - 29,999	850
# 30,000 - 34,999	900
# 35,000 - 39,999	950
# 40,000 - 44,999	1,000
# 45,000 - 49,999	1,100
# 50,000 - 59,999	1,200
# 60,000 - 69,999	1,300
# 70,000 - 79,999	1,400
# 80,000 - 89,999	1,500
# 90,000 - 99,999	1,600
# 100,000 and above	1,700

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

