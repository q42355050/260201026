gpa = float(input("Enter GPA: "))
lecture_num = int(input("Enter lecture number: "))

if (lecture_num < 47):
  if (gpa < 2.0):
    result = "Not enough number of lectures and GPA!"
  else:
    result = "Not enough number of lectures!"

else:
  if (gpa < 2.0):
    result = "Not enough GPA!"
  else:
    result = "GRADUATED!!!"

print(result)

