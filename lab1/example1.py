num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

if num1 <= num2 and num1<= num3:
  min_num = num1

elif num2 <= num3:
  min_num = num2

else:
  min_num = num3

print("Minimum number is :", min_num)
