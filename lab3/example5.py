# Seasons
month = input("Enter month: ")
day = int(input("Enter day: "))

if (month == "March"):
  if day >= 20:
    season = "Spring"
  else:
    season = "Winter"
elif (month == "June"):
  if day >= 21:
    season = "Summer"
  else:
    season = "Spring"
elif (month == "September"):
  if day >= 22:
    season = "Fall"
  else:
    season = "Summer"
elif (month == "December"):
  if day >= 21:
    season = "Winter"
  else:
    season = "Fall"
elif (month == "January" or month == "February"):
  season = "Winter"
elif (month == "October" or month == "November"):
  season = "Fall"
elif (month == "July" or month == "August"):
  season = "Summer"
elif (month == "April" or month == "May"):
  season = "Spring"

print("Season is", season, ".")