print("Enter the parameters (a, b, c) of a quadratic equation represented as: ax2 + bx + c. \n" )
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = (b ** 2) - (4 * a * c)

if(delta > 0):
  result = "There are two real roots."
elif(delta == 0):
  result = "There is one real root."
else:
  result = "There are two complex roots."

print(result)
