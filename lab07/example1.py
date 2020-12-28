n = int(input("How many people: "))
people = []

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    person = (name,age)
    people.append(person)

for person in people:
    if person[1] > 18:
        print(person[0])
        
