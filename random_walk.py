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
    print(walk, "Distance from home = ", abs(walk[0]+abs(walk[1])))