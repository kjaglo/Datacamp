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

person2 = {"person_id": 2,
           "name": "Sara"}
print(person2)  # {'person_id': 2, 'name': 'Sara'}

person2["surname"] = "Ray"
print(person2)  # {'person_id': 2, 'name': 'Sara', 'surname': 'Ray'}

person3 = dict(person_id=3, name="Leon")  # " " no needed
print(person3)  # {'person_id': 3, 'name': 'Leon'}
