##########################################

person_id1 = 1
name1 = "Ana"
surname1 = "Apple"
age1 = 25
address1 = ("England", "London")

person1 = {"person_id": 1,
           "name": "Ana",
           "surname": "Apple",
           "age": 25,
           "address": ("England", "London"),
           # hobby: "tennis"  # error: missing "" around the hobby
           }

# keys and values

print(person1)  # {'person_id': 1, 'name': 'Ana', 'surname': 'Apple', 'age': 25, 'address': ('England', 'London')}
print(type(person1))  # <class 'dict'>

person2 = {"person_id": 2,  # quotes necessary
           "name": "Sara"}
print(person2)  # {'person_id': 2, 'name': 'Sara'}

person2["surname"] = "Ray"  # quotes necessary
print(person2)  # {'person_id': 2, 'name': 'Sara', 'surname': 'Ray'}

person3 = dict(person_id=3, name="Leon")  # " " no needed
print(person3)  # {'person_id': 3, 'name': 'Leon'}


print(person1["name"])  # Ana
# print(person1["key"])  # KeyError: when we try to access data that is not in the dictionary


# The person1 does not contain a key value
if 'key' in person1:
    print(person1["key"])
else:
    print("The person1 does not contain a key value")


# The person1 does not contain a key value
try:
    print(person1["key"])
except KeyError:
    print("The person1 does not contain a key value")

print(dir(person1))

print(help(person1.get))
# get(key, default=None, /) method of builtins.dict instance
# Return the value for key if key is in the dictionary, else default.

print(person1.get('key'))  # None


for key in person1.keys():
    value = person1[key]
    print(key, '=', value)

# person_id = 1
# name = Ana
# surname = Apple
# age = 25
# address = ('England', 'London')

for key, value in person1.items():
    print(key, '=', value)
# the same output

person1.pop('name')  # removes specified key
print(person1)  # {'person_id': 1, 'surname': 'Apple', 'age': 25, 'address': ('England', 'London')}

person1.popitem()  # removes last key
print(person1)  # {'person_id': 1, 'surname': 'Apple', 'age': 25}

person1.popitem()
print(person1)  # {'person_id': 1, 'surname': 'Apple'}

person1.clear()  # clears all data from dict
print(person1)  # {}

