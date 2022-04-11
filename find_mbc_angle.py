import math

# calulate the angle between the two lengths


def find_angle(a, b):
    angle = math.degrees(math.atan(a/b))
    return angle


a = int(input())
b = int(input())

print(f"{round(find_angle(a, b))}\N{DEGREE SIGN}")
