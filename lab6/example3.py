list = [5, 91, 55, 20, 69, 19, 5, 20, 69, 78, 78]
unique_list = []

for num in list:
    if num not in unique_list:
        unique_list.append(num)
        
unique_list.sort()
unique_list.reverse()

print(unique_list)