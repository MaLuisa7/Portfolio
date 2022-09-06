import re

str = 'Take up one idea. One idea 45 at a time'

result =re.search(r'o\w', str)
print(result.group())

result1 =re.findall(r'o\w\w', str)
print(result1)

result2 = re.match(r'T\w\w', str)
print(result2.group())

#split
str1 = 'Take 1 up One 23 idea. One idea at a Time'
result = re.split(r'\d+', str1)
print(result)

#Substitute
result = re.sub(r'One', 'two', str)
print(result)

#Using quantifiers
result1 =re.findall(r'O\w?', str1)
print(result1)
result1 =re.findall(r'O\w+', str1)
print(result1)
result1 =re.findall(r'O\w*', str1)
print(result1)
result1 =re.findall(r'O\w{1}', str1)
print(result1)
result1 =re.findall(r'O\w{2}', str1)
print(result1)
result1 =re.findall(r'O\w{3}', str1)
print(result1)
result1 =re.findall(r'O\w{1,2}', str1)
print(result1)

#matching dates
str2 = 'Take 1 up 1-3-2019 One 23 idea. One idea at a Time 12-11-2020'
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str2)
print(result)

#special characters
str3 = 'Take 1 up 1-3-2019 One 23 idea. One idea at a Time 12-11-2020'
result = re.findall(r'^T\w*', str3)
print(result)


