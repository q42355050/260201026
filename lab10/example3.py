def sum_of_nested_list(x):
  if len(x) == 0:
    return 0

  else:
    if isinstance(x[0], list):
      return sum_of_nested_list(x[0]) + sum_of_nested_list(x[1:])
    else:
      return x[0] + sum_of_nested_list(x[1:])

print(sum_of_nested_list([1,2,3,[4,5]]))