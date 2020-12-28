studentNum = int(input("How many students are there: "))
grades = []
avg_grades = []
for i in range (1, studentNum + 1):
    print("For the student", i , "...")
    mt1 = int(input("Enter 1st midterm grade: "))
    mt2 = int(input("Enter 2nd midterm grade: "))
    fin = int(input("Enter final grade: "))
    grades.append([mt1, mt2, fin])

for grade in grades:
    std_grade = (grade[0] * 0.3) + (grade[1] * 0.3) + (grade[2] * 0.4) 
    avg_grades.append(std_grade)

print("Average grades are: ", avg_grades)

over90 = []
for grade in avg_grades:
    if grade >= 90:
        over90.append(grade)
print ("Average grades that are greater than 90 are: ", over90 )