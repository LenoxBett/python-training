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
 
basic_salary = float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))
# gross_salary = basic_salary + benefits

# def salary(a,b):
    # gross = a + b
    # return(gross)
# basic_sala/ry
# benefits

# gross_salary = salary(basic_salary, benefits)
def calc_gross(a,b):
    gross = a + b
    return gross

gross_salary = calc_gross(basic_salary,benefits)
print(gross_salary)

def calc_nhif(a):
    if a < 6000:
        nhif = 150
    elif a >= 6000 and a < 8000:
        nhif = 300
    elif a >= 8000 and a < 12000:
        nhif = 400
    elif a >= 12000 and a < 15000:
        nhif = 500
    elif a >= 15000 and a < 20000:
        nhif = 600
    elif a >= 20000 and a < 25000:
       nhif = 750
    elif a >= 25000 and a < 30000:
       nhif = 850
    elif a >= 30000 and a < 35000:
       nhif = 900
    elif a >= 35000 and a < 40000:
       nhif = 950
    elif a >= 40000 and a < 45000:
       nhif = 1000
    elif a >= 45000 and a < 50000:
       nhif = 1100
    elif a >= 50000 and a < 60000:
       nhif = 1200
    elif a >= 60000 and a < 70000:
       nhif = 1300
    elif a >= 70000 and a < 80000:
       nhif = 1400
    elif a >= 80000 and a < 90000:
       nhif = 1500
    elif a >= 90000 and a < 100000:
      nhif = 1600
    else:
      nhif = 1700
    return nhif

nhif = calc_nhif(gross_salary)
print(nhif)


# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

def calc_nssf(a, b=0.06):
   if a <= 18000:
      nssf_contribution = a * b
   else:
      nssf_contribution = 18000 * b
   return nssf_contribution

nssf = calc_nssf(gross_salary)
print(nssf)


# Continue with the same program and calculate an individual’s NHDF using:

def calc_nhdf(a, b=0.015):
   nhdf_contribution = a * b
   return nhdf_contribution

nhdf = calc_nhdf(gross_salary)
print(nhdf)









