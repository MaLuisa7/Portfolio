#reverse string #1
'''s = input('Enter a string')
print(s[::-1])'''

#reverse string #2
import shlex

'''s = input('Enter a string')
i = len(s)-1
result = ''
while i >=0:
    result = result +s[i]
    i = i -1
print(result)
'''
#JOIN #3
'''s = '-'.join(['a', 'b', 'c'])
print(s)'''

#reverse string #3
'''s = input('Enter a string')
print(''.join(reversed(s)))'''

#WORD REVERSED
s = 'All the power is with in you'
temp = s.split()
result = []
i = len(temp) -1
while i >= 0 :
    result.append(temp[i])
    i = i-1
print(result)

output = ' '.join(result)
print(output)

#WORD REVERSE AND SENTENCE REVERSE
s = 'Python is cool'
temp = s.split()
print(temp)
result = []
i =  0
while i < len(temp) :
    result.append(temp[i][::-1])
    i = i +1
print(result)
output = ' '.join(result)
print(output)

#remove duplicates chars
s = 'abbbcccZZZIII'
temp = []
for c in s:
    if c not in temp:
        temp.append(c)
print(c)

output = ''.join(temp)
print(output)

#Count the characters
s = 'abbbcccZZZIII'
d = {}
for c in s:
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c]= 1
for k,v in d.items():
    print('{} = {} times'.format(k,v))

#print right angled triangle

'''n = int(input('Enter the number of rows: '))
for i in range(1, n+1):
    for j in range(1,i+1):
        print('*', end= '')
    print()'''

'''n = int(input('Enter the number of rows: '))
for i in range(1, n+1):
    print('*'*i)'''

#print pyramid pattern
n = int(input('Enter the number of rows: '))
for i in range(1, n+1):
    print(' '*(n-i), end='')
    print('* '*i)

#find substrings in a given string
s = 'Take up one idea and make that idea your life. Think and dream of that idea and leave every other idea alone'
subs = 'idea'
found = False
pos = -1
lenght = len(s)
while True:
    pos = s.find(subs, pos +1, lenght)
    if pos==-1:
        break
    print('Found the string at position ', pos)
    found = True
if found ==False:
    print('Substring not found')
