def pascal_last(n):
  if n == 1:
    print(1) 

  else:
    print (n , pascal_last(n-1))

  print (1)
  

pascal_last(4)