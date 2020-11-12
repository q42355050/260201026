car1_speed = 80  # km/h
car2_speed = 70  # km/h

distance1 = 490 # km
distance2 = 150 # km

car1_speed_min = car1_speed / 60 # km/min
car2_speed_min = car2_speed / 60 # km/min

time = (distance1 - distance2)  / (car1_speed_min + car2_speed_min)
# t = x / v 
print(time, "minutes")
