N = int(input("How many numbers are there? : "))

count = 0
evenCount = 0
while count < N:
    num = int(input("Enter an integer: "))
    count += 1
    if num % 2 == 0:
        evenCount += 1
    

result = evenCount / count * 100
print(result, "% of numbers are even numbers.")
    