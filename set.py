
set1 = {"apple", "banana", "cherry", "apple"}

# no duplicate values: {'apple', 'cherry', 'banana'}

print(set1)

# len(set)

print(len(set1))  # 3

# type(set)

print(type(set1))  # <class 'set'>

set2 = {"abc", 34, True, 40, "male", 40}

print(set2)  # {True, 34, 'abc', 40, 'male'}

set3 = {"apple", "banana", "cherry", "apple", "banana", "cherry"}

print(set3)  # {'banana', 'cherry', 'apple'}

# set4 = set([1, 2, 3, 4, 5])

set4 = {1, 2, 3, 4, 5}

print(set4)  # {1, 2, 3, 4, 5}

print(type(set4))  # <class 'set'>

# create empty set (empty_set=set() no: {} -> dictionary)

set5 = set()

print(set5)  # set()

set5.add(1)
set5.add(2)
set5.add(1)
set5.add(3)

set5.update([4, 5, 6])  # add more values

set6 = {7, 8, 9, 9, 7, 10}

set5.update(set6)  # add set

print(set5)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set5.pop()  # pop from beginning

print(set5)  # {2, 3, 4, 5, 6, 7, 8, 9, 10}

# my_set.remove()

set5.remove(4)

set5.remove(2)

# set5.remove(11)  KeyError: 11 -> no value of 11

# myset.discard()

set5.discard(11)  # no error if there is no value of 11

print(set5)  # {3, 5, 6, 7, 8, 9, 10}

