import requests
from aocd import get_data

DATA = get_data(day=1, year=2023)

sum = 0
lines = DATA.split("\n")

for line in lines:
    temp_list = []
    for x in line:
        try:
            i = int(x)
            temp_list.append(x)
        except Exception:
            pass

    if len(temp_list) == 1:
        temp = temp_list[0] * 2
    else:
        temp = temp_list[0] + temp_list[-1]

    sum = sum + int(temp)

print(sum)
