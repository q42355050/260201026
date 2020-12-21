def get_reversed(my_list):
  if my_list == []:
    return my_list
  else:
    # [1,2,3,4,5]
    return [my_list[-1]] + get_reversed(my_list[:-1])
                #[5] + #[1,2,3,4]

x = [1,2,3,4,5]

print(get_reversed(x))