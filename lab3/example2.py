num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))

if(num1 < num2 and num1 < num3):
  min_number = num1
elif(num2 < num3 and num2 < num1):
  min_number = num2
else:
  min_number = num3

print("Minimum number is:", min_number)