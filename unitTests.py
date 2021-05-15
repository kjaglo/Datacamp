from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("Radius must be a number")
    return pi * (r ** 2)


# Test function
array = [2, 0, -3, 2 + 5j, True, "radius"]

message = "Area of circles with r = {radius} is {area}."

# for r in array:
    # Area = circle_area(r)
    # print(message.format(radius=r, area=Area))
# Area of circles with r = 2 is 12.566370614359172.
# Area of circles with r = 0 is 0.0.
# Area of circles with r = -3 is 28.274333882308138.
# Area of circles with r = (2+5j) is (-65.97344572538566+62.83185307179586j).
# Area of circles with r = True is 3.141592653589793.
# return pi * (r ** 2)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
