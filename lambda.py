# function
def f(x):
    return 2 ** x


print(f(5))  # 32

# anonymous function = lambda expression

l = lambda: print("Hello!")  # no arguments
l()  # Hello!

g = lambda x: 2 ** x
print(g(5))  # 32

full_name = lambda first, last: first.strip().title() + " " + last.strip().title()
# title() - capitalize the first letter
# strip() - removes spsaces
print(full_name("James", " bond  "))  # James Bond
print(full_name("JAMES", " bond  "))  # James Bond

add = lambda x, y, z: x + y + z

print(add(2, 3, 4))  # 9

people = ["Ann Bryce", "Gary Odd", "Zack Brave", "Frank Bury", "Douglas James Adams", "H. G. Wells"]
print(help(people.sort))  # sort(*, key=None, reverse=False) method of builtins.list instance    Stable sort *IN PLACE*.
people.sort(key=lambda name: name.split(" ")[-1].lower())
print(people)
# lower() - lowercase
# sorted by last name
# ['Douglas James Adams', 'Zack Brave', 'Ann Bryce', 'Frank Bury', 'Gary Odd', 'H. G. Wells']

l = [1, 2, 3, 4, 5]

print(l[-1])  # 5
print(l[-1:])  # [5]
print(l[-2])  # 4
print(l[-2:])  # [4, 5]
print(l[1:])  # [2, 3, 4, 5]


def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx +c"""
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic_function(1, 2, 1)
print(f(0))  # 1
print(f(1))  # 4
print(f(-1))  # 0

print(build_quadratic_function(3, 0, 0)(3))  # 3x^2 for x=3 = 27
