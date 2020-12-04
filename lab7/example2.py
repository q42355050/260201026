books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for book in books:
  characters = len(book)
  unique_characters = len(set(book))
  value = (characters, unique_characters)
  book_dict[book] = value

for key, value in book_dict.items():
  print (key, "->", value)

for book in book_dict:
  characters, unique_characters = book_dict[book]
  average = (characters + unique_characters) / 2
  book_dict[book] = (characters, unique_characters, average)

for key, value in book_dict.items():
  print(key, "->", value)
