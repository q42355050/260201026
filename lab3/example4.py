# Ticket Discount
age = int(input("Please enter your age: "))
price = 3

if (age < 6 or age > 60):
  price = 0
elif (age >= 6 and age <= 18):
  price -= price / 2

print("Ticket price is", price, "TL.")

