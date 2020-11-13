# Power
a = int(input("a = "))
b = int(input("b = "))
result = 1

if(a == 0):
  result = 1
else:
  for i in range (b):
    result *= a

print(result)