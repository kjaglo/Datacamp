import datetime


class User:
    pass


user1 = User()

user1.first_name = "Selena"
user1.last_name = "Bourne"
user1.age = 22

print(user1.first_name)  # Selena
print(user1.last_name)  # Bourne
print(user1.age)  # 22

first_name = "Fiona"
last_name = "Richard"

user2 = User()
user2.first_name = first_name
user2.last_name = last_name
user2.country = "Italy"
print(user2.first_name)  # Fiona
print(user2.last_name)  # Richard
print(user2.country)  # Richard


class Person:
    # help(Person v) """ ... """
    """
    Store name and birthday.
    """

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyy-mm-dd

        names = full_name.split(" ")

        self.first_name = names[0]
        self.last_name = names[-1]

    def count_age(self):
        """ Return the age of the person in years"""
        year_now = datetime.date.today().year
        birth_year = int(self.birthday[0:4])
        return year_now - birth_year


person1 = Person("Kaine Martinez", "1993-05-13")

print(person1.name)  # Kaine Martinez
print(person1.birthday)  # 1993-05-13
print(person1.first_name)  # Kaine
print(person1.last_name)  # Martinez
print(person1.count_age())  # 28

help(Person)
