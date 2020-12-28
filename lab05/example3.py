num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

list_num1 = []
list_num2 = []
match = 0

for i in num1:
    list_num1.append(i)
for i in num2:
    list_num2.append(i)
    
list_num1.reverse()
list_num2.reverse()

for i in range((min(len(list_num1),len(list_num2)))):
    if list_num1[i] == list_num2[i]:
        match += 1
        
print(match)