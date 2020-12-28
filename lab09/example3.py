def get_evens(my_list):
  if len(my_list) == 0:
    return 0
  else:
    if my_list[0] % 2 == 0:
      return 1 + get_evens(my_list[1:])
    else:
      return 0 + get_evens(my_list[1:])

x = get_evens([0,4,3,2,6,7,5,1,32])
print(x)
