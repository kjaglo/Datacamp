import urllib

print(dir(urllib))

from urllib import request

print(dir(request))

resp = request.urlopen("https://www.wikipedia.org/")

print(type(resp))  # <class 'http.client.HTTPResponse'>

print(dir(resp))

# .code
print(resp.code)  # 200 - OK

# .length
print(resp.length)  # 73360 - size in bytes

# .peek()
print(resp.peek())
# b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n<head>\n<meta charset="utf-8">\n<title>Wikipedia</title>...
# b' - bytes

# .read()
data = resp.read()

print(data)
print(type(data))  # <class 'bytes'>
print(len(data))  # 73360 - size in bytes

# .decode()
html = data.decode("UTF-8")

print(type(html))  # <class 'str'>

print(html)  # the entire html from a website

# .read() again
data2 = resp.read()
print(data2)  # b'' - nothing left

# resp2 = request.urlopen("https://www.google.com/search?q=abc")
# print(resp2.code) # 403 - forbidden

# https://www.youtube.com/watch?v=LosIGgon_KM&t=5m30s

# v - video id
# t - start time

from urllib import parse

parameters = {"v": "LosIGgon_KM", "t":"5m30s"}
query_string = parse.urlencode(parameters)

print(query_string)
build_url = "https://www.youtube.com/watch?"+query_string

resp3 = request.urlopen(build_url)
print(resp3.code)  # 200 - ok
print(resp3.isclosed())  # False

read_= resp3.read().decode("UTF-8")
print(resp3.isclosed())  # True (read closes)
print(read_[:100])
# <!DOCTYPE html><html style="font-size: 10px;font-family: Roboto, Arial, sans-serif;" lang="pl-PL" ty

