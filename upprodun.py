import math

num_rooms = input().strip()
num_rooms = float(num_rooms)

num_teams = input().strip()
num_teams = float(num_teams)

if num_teams % num_rooms == 0:
    max_stars = num_teams / num_rooms
    min_stars = max_stars
    times_min = 0
else:
    max_stars = math.ceil(num_teams / num_rooms)
    min_stars = max_stars - 1
    times_min = (num_teams % num_rooms) - 1

times_max = num_rooms - times_min

for i in range(int(times_max)):
    for i in range(int(max_stars)):
        print("*", end = "")
    print();

for i in range(int(times_min)):
    for i in range(int(min_stars)):
        print("*", end = "")
    print();
