name = "Maria"

print(name[1:])  # aria
print(name[-1:])  # a
print(name[-2:])  # ia
print(name[-3:])  # ria

s1 = "How to learn everything? xd"
print(s1.split(" "))  # ['How', 'to', 'learn', 'everything?', 'xd']

space = " "
j1 = space.join(["What", "is", "the", "purpose", "of", "life?"])
print(j1)  # What is the purpose of life?

print(name.startswith("M"))  # True
print(name.endswith("a"))  # True

print(name.rstrip("a"))  # Mari
print(name)  # Maria
print(name.lstrip("a"))  # Maria - nothing changed
print(name.lstrip("M"))  # aria

name2 = "anna"
print(name2.strip("a"))  # nn

s2 = "   spaces "
print(s2)  # spaces
print(s2.strip())  # spaces - removes spaces

s3 = "Ana"
s4 = "Smith"

print(s3 + " " + s4)  # Ana Smith

james_bond = 7
print(str(james_bond).zfill(3))  # 007
