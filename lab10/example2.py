def hailstone(x):
  print(x)
  
  if x == 1:
    return

  else:
    if x % 2 == 0:      
      hailstone(x//2)
    else:      
      hailstone(3*x+1)

hailstone(11)
