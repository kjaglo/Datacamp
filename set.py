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
set5.discard(10)

print(set5)  # {3, 5, 6, 7, 8, 9} -> delete 4,2,10

new_list = [1, 2, 3, 2, 1, 3, 3, 4]
print(new_list)  # [1, 2, 3, 2, 1, 3, 3, 4]

set_from_list = set(new_list)
print(set_from_list)  # {1, 2, 3, 4}

###############################################

# intersection, difference, issubset

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s4 = {1, 2, 3, 4}

set_intersection_1_2 = s1.intersection(s2)
print(set_intersection_1_2)  # {2, 3}

set_intersection_1_2_3 = s1.intersection(s2, s3)
print(set_intersection_1_2_3)  # {3}

set_difference_1_2 = s1.difference(s2)
print(set_difference_1_2)  # {1}

set_difference_3_1 = s3.difference(s1)
print(set_difference_3_1)  # {4, 5}

set_issubset_1_2 = s1.issubset(s2)
print(set_issubset_1_2)  # False

set_issubset_1_4 = s1.issubset(s4)
print(set_issubset_1_4)  # True



