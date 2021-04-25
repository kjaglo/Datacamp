# tuple

list1 = [1, 2, 3, 4, 5, 6]

tuple1 = (1, 2, 3, 4, 5, 6)


# length
print(len(list1))  # 6
print(len(tuple1))  # 6

# for loop
for l in list1:
    print(l)

for t in tuple1:
    print(t)

# methods
print(dir(list1))  # lists have more methodsprint(dir(tuple1))

import sys

print(dir(sys))

print(help(sys.getsizeof))#getsizeof(...)  getsizeof(object, default) -> int  Return the size of object in bytes. None

print(80*'-')  # --------------------------------------------------------------------------------

# lists occupy more memory than tuples

print(sys.getsizeof(list1))  # 60 bytes
print(sys.getsizeof(tuple1))  # 52 bytes

# lists: add, remove, change data
# tuples: cannot be changed (immutable), made quickly

import timeit

list_time = timeit.timeit(stmt="[1, 2, 3]",  # statement
                          number=10_000_000)  # number of times to perform
print(list_time)  # 0.667


tuple_time = timeit.timeit(stmt="(1, 2, 3)",  # statement
                           number=10_000_000)  # number of times to perform

print(tuple_time)  # 0.121

empty_tuple = ()
tuple_1 = ("a")  # It is not a tuple: the tuple containing a single element is a string
# ! a comma at the end
tuple_1_ = ("a",)
tuple_2 = ("a", "b")
tuple_3 = ("a", "b", "c")

print(empty_tuple)  # ()

print(tuple_1)  # a # not a tuple !!!
print(type(tuple_1))   # <class 'str'>

print(tuple_1_)  # ('a',)
print(tuple_2)  # ('a', 'b')
print(tuple_3)  # ('a', 'b', 'c')

empty_list = []
list_1 = ["a"]
list_1_ = ["a", ]  # the same
list_2 = ["a", "b"]
list_3 = ["a", "b", "c"]

print(empty_list)  # ()
print(list_1)  # a # not a tuple !!!
print(list_1_)  # ('a',)
print(list_2)  # ('a', 'b')
print(list_3)  # ('a', 'b', 'c')

# another way to make a tuple

tuple__1 = 1,
tuple__2 = 1, 2
tuple__3 = 1, 2, "ana"

print(tuple__1)  # (1,)
print(tuple__2)  # (1, 2)
print(tuple__3)  # (1, 2, 'ana')

print(type(tuple__1))  # <class 'tuple'>
print(type(tuple__2))  # <class 'tuple'>
print(type(tuple__3))  # <class 'tuple'>

print(type(tuple_1))   # <class 'str'>

print(80*'-')  # --------------------------------------------------------------------------------

# (height, weight, sex)

person1 = (181, 75, "male")

height1 = person1[0]
weight1 = person1[1]
sex1 = person1[2]

print("Person1:")
print("Height: ", height1)
print("Weight: ", weight1)
print("Sex: ", sex1)

print(80*'-')  # --------------------------------------------------------------------------------

person2 = (160, 50, "female")

height2, weight2, sex2 = person2

print("Person2:")
print("Height: ", height2)
print("Weight: ", weight2)
print("Sex: ", sex2)

print(80*'-')  # --------------------------------------------------------------------------------

a, b, c = [1, 2, 3]

print(a, b, c)

# error: k, l, m = (1, 2, 3, 4)
# error: k, l, m = (1, 2)

