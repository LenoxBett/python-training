# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 


basic = float(input("enter basic: "))
benefits = float(input("enter benefits: "))
gross_salary = basic + benefits

if gross_salary <= 18000:
    nssf = gross_salary * 0.06
else:
    nssf = 18000 * 0.06
print(nssf)












