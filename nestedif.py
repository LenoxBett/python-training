marks = int(input("enter your marks"))
# check if the marks are btwn 0 and 10
# if marks are between 0 and 100 display the grades in 
# following categories
# 90 => 100 A
# 80 => 90 B 
# 70 => 80 C
# 60 => 70 D
# 50 => 60 E
# Below 50 FAIL

# otherwise diplay valid marks

if (marks >= 0 ) and (marks <= 100):
    if(marks >= 90):
        grade = "A"
    elif(marks >= 80) and (marks < 90):
        grade = "B"
    elif(marks >= 70) and (marks < 80):
        grade = "C"
    elif(marks >= 60) and (marks < 70):
        grade = "D"
    elif(marks >= 50) and (marks < 60):
        grade = "E"
    else:
        grade = "FAIL"
else:
    grade = ("invalid marks")
print(grade)
 





