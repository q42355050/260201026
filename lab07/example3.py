employee_num = 5
employees = {}
salary_list = []

for i in range(employee_num):
  name = input("Enter employee's name: ")
  salary = int(input("Enter employee's salary: "))
  employees[name] = salary 
  salary_list.append(salary)

salary_list.sort()
salary_list.reverse()

for name, salary in employees.items():
  for i in range(3):
    if salary == salary_list[i]:
      print(name)
