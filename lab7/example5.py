numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

numbers1 = set(numbers1)
numbers2 = set(numbers2)
intersection = []
union = []

for i in numbers1:
  if i in numbers2:
    intersection.append(i)

print("Intersection :", intersection)

for i in numbers1:
  union.append(i)

for j in numbers2:
  union.append(j)

union = list(set(union))

print("Union :", union)