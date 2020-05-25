import math

n = int(input())
max_snow = 0
max_time = 0
max_quality = 0
max_value = 0

for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = int(math.pow((snow / time), quality))

    if value > max_value:
        max_value = value
        max_snow = snow
        max_time = time
        max_quality = quality

print(f'{max_snow} : {max_time} = {max_value} ({max_quality})')
