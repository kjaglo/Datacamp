import random


def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'E', "W", "S"])
        if step == 'N':
            y = y + 1
        if step == 'S':
            y = y - 1
        if step == 'E':
            x = x + 1
        if step == 'W':
            x = x - 1
    return (x, y)


for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

print("-" * 100)


def random_walk_2(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# (3, 3) Distance from home =  6
# (-2, -2) Distance from home =  4
# (-2, -2) Distance from home =  4
# (1, -3) Distance from home =  4
# (-2, -2) Distance from home =  4
# (-4, -2) Distance from home =  6
# (-2, 2) Distance from home =  4
# (1, 5) Distance from home =  6
# (-2, -2) Distance from home =  4
# (2, 0) Distance from home =  2
# (4, 4) Distance from home =  8
# (-1, -1) Distance from home =  2
# (0, 2) Distance from home =  2
# (-5, 1) Distance from home =  6
# (-3, -5) Distance from home =  8
# (-6, 0) Distance from home =  6
# (1, 1) Distance from home =  2
# (-1, 1) Distance from home =  2
# (-6, -2) Distance from home =  8
# (1, -1) Distance from home =  2
# (-4, -4) Distance from home =  8
# (-2, -2) Distance from home =  4
# (-3, -5) Distance from home =  8
# (2, 0) Distance from home =  2
# (3, -1) Distance from home =  4

# monte carlo
number_of_walks = 100000
for walk_length in range(1, 31):  # 1-30
    no_transport = 0  # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percent = no_transport / number_of_walks * 100
    print("walk length", walk_length, " :", no_transport_percent, "%")

# walk length 1  : 100.0 %
# walk length 2  : 100.0 %
# walk length 3  : 100.0 %
# walk length 4  : 100.0 %
# walk length 5  : 87.849 %
# walk length 6  : 93.891 %
# walk length 7  : 76.413 %
# walk length 8  : 86.50099999999999 %
# walk length 9  : 67.335 %
# walk length 10  : 79.333 %
# walk length 11  : 59.75 %
# walk length 12  : 72.759 %
# walk length 13  : 53.679 %
# walk length 14  : 67.291 %
# walk length 15  : 48.696 %
# walk length 16  : 62.504000000000005 %
# walk length 17  : 44.483 %
# walk length 18  : 57.857 %
# walk length 19  : 41.005 %
# walk length 20  : 54.342 %
# walk length 21  : 38.094 %
# walk length 22  : 50.778 %
# walk length 23  : 35.464 %
# walk length 24  : 47.881 %
# walk length 25  : 33.241 %
# walk length 26  : 45.497 %
# walk length 27  : 31.11 %
# walk length 28  : 42.779 %
# walk length 29  : 29.374 %
# walk length 30  : 40.879 %