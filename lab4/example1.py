# Sum of the last two digits
num = input("Please enter an integer number: ")

if(len(num) > 1):
  result = int(num[-1]) + int(num[-2]) 
else:
  result = int(num)

print("Result is", result)