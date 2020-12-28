email = input("Please enter your e-mail: ")
email = email.lower()

is_same = bool()

number_of_at_signs = email.count("@")

if number_of_at_signs == 1:

  before_at = email.split("@")[0]
  after_at = email.split("@")[1]

  before_at = before_at.replace("." , "")

  email = before_at + "@" + after_at

  if email == "ceng113@example.com":
    is_same = True
  else:
    is_same = False

else:
  is_same = False

if is_same:
  print("Yes, it is ceng113@example.com")
else:
  print("No, it is not ceng113@example.com")
