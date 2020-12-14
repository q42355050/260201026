def sum_of_list(a_list):
  total = 0
  for i in a_list:
    total += i

  result = total**2
  return result

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(sum_of_list(a_list))
