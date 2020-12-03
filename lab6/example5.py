n = int(input("Please enter a number: "))
list1 = []
list2 = []
result = 0

for j in range(n):
    print("For line", j+1)
    for i in range(n):
        item = int(input("Enter a number: "))
        list1.append(item)
    list2.append(list1)
    list1 = []
    result += list2[j][j]
    

print(list2)
print(result)