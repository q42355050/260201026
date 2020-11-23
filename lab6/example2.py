number_of_students = int(input("How many students are there?: "))
grades = []
for i in range(1, number_of_students + 1):
  print("For the", i , "th student...")
  mt1 = int(input("Enter midterm 1 grade: "))
  mt2 = int(input("Enter midterm 2 grade: "))
  final = int(input("Enter final grade: "))

  grade = [mt1,mt2,final]
  grades.append(grade)


average_grades = []

for grade in grades:
  mt1 = grade[0]
  mt2 = grade[1]
  final = grade[2]
  average = mt1 * 0.3 + mt2 * 0.3 + final * 0.4
  average_grades.append(average)

print ("Average grades : " , average_grades)

  