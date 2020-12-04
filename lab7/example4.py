password = input("Enter your password: ")
isValid = False
lower = 0
upper = 0
number = 0

if len(password) >= 8:
  for i in password:
    if i.islower():
      lower += 1
    if i.isupper():
      upper += 1
    if i.isdigit():
      number += 1

    if (lower > 0 and upper > 0 and number > 0):
      isValid = True
else:
  isValid = False

print(isValid)