fibo = [0,1]
num = int(input("How many fibonacci numbers: "))
count = 1
while (count < num):
    nextNum = fibo[count] + fibo[count-1]
    fibo.append(nextNum)
    count += 1
    
    
print (fibo)