import random

dir(random)

print(help(random.random))  # random() -> x in the interval [0, 1).

for i in range(10):
    print(i)  # 0,1,2...9
    print(random.random())  # [0,1)

for i in range(10):
    random_number_3_7 = random.random() * 4 + 3
    print(random_number_3_7)  # [3,7)

print(help(random.uniform))
#  Get a random number in the range [a, b) or [a, b] depending on rounding.
for i in range(10):
    print(random.uniform(3, 7))  # [3,7)

print(help(random.normalvariate))

# normalvariate(mu, sigma) method of random.Random instance
#   Normal distribution.
#   mu is the mean, and sigma is the standard deviation.

a = []
for i in range(10000):
    a.append(random.normalvariate(mu=0, sigma=1))
from matplotlib import pyplot as plt

plt.hist(a)
plt.show()

for i in range(10000):
    a.append(random.normalvariate(mu=0, sigma=9))
from matplotlib import pyplot as plt

plt.hist(a)
plt.show()

print(help(random.randint))

# randint(a, b) method of random.Random instance
# Return random integer in range [a, b], including both end points.

for i in range(10):
    print(random.randint(1, 10))



print(help(random.choice))

#choice(seq) method of random.Random instance
#Choose a random element from a non-empty sequence.


game = ['paper', 'rock', 'scissors']

for i in range(10):
    print(random.choice(game))



