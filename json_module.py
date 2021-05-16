import json

# Java Script Object Notation
print(dir(
    json))  # ['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']

# load data from a file

json_file = open("data_json\\json_example.txt", "r", encoding="utf-8")

print(json_file)  # <_io.TextIOWrapper name='data_json\\json_example.txt' mode='r' encoding='utf-8'>

# open the file

json_load = json.load(json_file)  # (null -> None true  -> True false -> False)

# close the file

json_file.close()

print(json_load)  # {'quiz': {
# 'sport': {
# 'q1': {'question': 'Which one is correct team name in NBA?',
# 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'],
# 'answer': 'Huston Rocket'}},
# 'maths': {
# 'q1': {'question': '5 + 7 = ?', 'options': [None, '11', '12', '13'],
# 'answer': '12'},
# 'q2': {'question': '12 - 8 = ?', 'options': ['1', '2', '3', '4'],
# 'answer': '4'},
# 'q3': {'question': '1 - 1 = 0?', 'options': [True, False],
# 'answer': True}}}}

print(type(json_load))  # <class 'dict'>

print(json_load['quiz']['sport'])
# {'q1': {'question': 'Which one is correct team name in NBA?',
# 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriors', 'Huston Rocket'],
# 'answer': 'Huston Rocket'}}

print(json_load['quiz']['sport']['q1']['question'])  # Which one is correct team name in NBA?

json_string = json.dumps(json_load)  # dumps(json_load, ensure_ascii=False) to avoid wrong conversion eg: ł

print(json_string)  # change dict to string (None -> null) True -> true False->false
print(json_string[0])  # {

# json_file_string = open("data_json\\json_string.txt", "r", encoding="utf-8")

# json_loads = json.loads(json_file_string)
# json_file_string.close()

# print(json_loads)

dictionary = {}
dictionary["title"] = "Abc"
dictionary["director"] = "Ron Smith"
dictionary["year"] = 2020
dictionary["actors"] = ["Mąrk Apple", "Sara Use", "Ana Babel"]
dictionary["is_cool"] = True
dictionary["budget"] = 200000000

file = open("data_json\\json_file_save.txt", "w", encoding="utf-8")
# {"title": "Abc", "director": "Ron Smith", "year": 2020,
# "actors": ["M\u0105rk Apple", "Sara Use", "Ana Babel"], "is_cool": true, "budget": 200000000}
json.dump(dictionary, file)
file.close()

# ensure_ascii=False
file = open("data_json\\json_file_save.txt", "w", encoding="utf-8")
# {"title": "Abc", "director": "Ron Smith", "year": 2020,
# "actors": ["Mąrk Apple", "Sara Use", "Ana Babel"], "is_cool": true, "budget": 200000000}
json.dump(dictionary, file, ensure_ascii=False)
file.close()