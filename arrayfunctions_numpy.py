from numpy import *

a1 = arange(12)
print('a1', a1)

a2 = reshape(a1,(2,6))
print('a2',a2)

a3 = reshape(a1, (2,2,3))
print('a3',a3)
print(a3.flatten())

print(eye(3))
print(ones((2,3), int))
print(zeros((2,3), int))



'''
1. answer : runs slow
2. answer : true
3. answer: all above
4. answer : True
5. Which of the following function can be used to find the type of data a variable is holding
type()
6.All data types in python are object types and have a associated class
True
7.A binary literal start with which of the following
0B
Pregunta 8:
Which of the following is a hexa decimal literal in python
0XFF
Pregunta 9:
What is the result of the following print(10>20)
false
Pregunta 10:
Which of the following function can be used to convert string to integer
int
Pregunta 11:
Which of the following can be used to initialize a multi line string
triple  quotes
Pregunta 12:
Which of the following will give the length of a string str
len(str)
Pregunta 13:
How to slice a string str from 2nd element all the way to the end
[2:]
Pregunta 14:
Which of the following is not using a slicing step
s[:3]
Pregunta 15:
Which of the following string methods can be using to search for a substring with in a given string
find
Pregunta 16:
A list can be initialized using which of the following syntax
[]
Pregunta 17:
Which of the following  type can be used to store key value pairs
dictionary
Pregunta 18:
Which of the following will reverse the sort order
lst.sort(reverse=True)
Pregunta 19:
We can create a tuple from a list
True
Pregunta 20:
Which of the following will delete a element in a Dictionary
del dict[1]
Pregunta 21:
Which of the following is the floor division operator?
//
Pregunta 22:
Which of the following is a equality comparison operator?
==
Pregunta 23:
Which of the following is a invalid syntax
x=y+
Pregunta 24:
Which of the following operator will evaluate to true only if all the statements are true
and
Pregunta 25:
Which of the following functions can be used along with the input function to deal with more than one input
split
Pregunta 26:
Which of the following indicates a decimal point number while working with print() function
%f
Pregunta 27:
Which of the following are used as placeholders while using the string format method?
{}
Pregunta 28:
Which of the following will seperate the values being printed with a comma
print(a,b,sep=";")
Pregunta 29:
Which of the following loop should be used while working with a sequence
for
Pregunta 30:
Which of the following should be used to skip the current iteration of a loop
continue
Pregunta 31:
If the assert expression evaluates to false then an Assert Error is raised
True
Pregunta 32:
In a if-else ladder the else block code will be executed always even when if or one of the elif blocks gets executed
False
Pregunta 33:
Which module helps us work with command line arguments
sys
Pregunta 34:
What is the name of the  command line arguments array on the sys module
argv
Pregunta 35:
Functions can return multiple values in python
True
Pregunta 36:
Functions defined inside other functions can be used outside of those functions
False
Pregunta 37:
A function that calls itself is called a?
recursive function
Pregunta 38:
We can access a variable defined inside a function outside the function
False
Pregunta 39:
What is the right way to pass keyword arguments to the following function product(x,y)
product(y=20,x=30)
Pregunta 40:
Lambdas are defined using the def keyword
False
Pregunta 41:
Which of the following functions should be used to create a new list from a given list while applying a logic
filter
Pregunta 42:
The reduce function is a part of which of the following modules?
functools
Pregunta 43:
Which of the following symbols is used to apply a decorator
@
Pregunta 44:
Which of the following function applies a function/lambda on every element of the list and gives us a new list
map()
Pregunta 45:
Which of the following can be used to create custom sequences
generator
Pregunta 46:
Which of the following methods is used to create and initialize fields on a class
__init(self)
Pregunta 47:
Which of the following operator is used to access method on a object
.
Pregunta 48:
Which of the following is not one of the four OOP principle
Static
Pregunta 49:
A method shold be marked with which of the following to make it static
@staticmethod
Pregunta 50:
To create a object of the inner class we use the object of the outer class
True
Pregunta 51:
Which of the following is used as a prefix to a field to hide that field
__
Pregunta 52:
Encapsulation is the process binding the methods and data/fields together so that only those methods can access that data
True
Pregunta 53:
Which of the following is inheritance syntax
class x(y)
Pregunta 54:
The process of implementing the same method that is present in the parent class in the child class is called?
overriding
Pregunta 55:
When we define the same exact method as in the parent class in the child class what is it called
overriding
Pregunta 56:
Which of the following is inheritance syntax
class x(y)
Pregunta 57:
The process of implementing the same method that is present in the parent class in the child class is called?
overriding
Pregunta 59:
Which class should a class inherit from to be abstract
ABC
Pregunta 60:
Which of the following should be used to mark a abstract method
@abstractmethod
Pregunta 61:
If all the methods in a class are abstract it is a
iinterface
Pregunta 62:
If we do not handle an exception the program execution will continue after the exception line.
False
Pregunta 63:
The finally block is executed only when a exception is thrown
False
Pregunta 64:
Which of the following should be passed as a mode to write to a file
w
Pregunta 65:
Which of the following method is used to check if the file exists
isfile()
Pregunta 66:
The process of writing an object to a stream is called
pickle
Pregunta 67:
Which of the following method is used to Unpickle
load
Pregunta 68:
Which of the following should be used to check for a pattern match at the end of the String
\Z
Pregunta 69:
Which of the following methods replaces a string with another during a regular expression match
sub
Pregunta 70:
Which of the following quantifiers should be use for 1 or more
+
Pregunta 71:
The sleep method accepts time in milli seconds
False
Pregunta 72:
Which of the following methods on datetime will give use current date and time
today()
Pregunta 73:
Which moudle is the sleep method a part of
time
Pregunta 74:
Which of the following will create a date and time using date and time
datetime.combine(d,t)
Pregunta 75:
Which of the following is the correct syntax to create thread using functions
t = Thread(target=displayNumbers)
Pregunta 76:
t.run() will run a thread
False
Pregunta 77:
Which of the following method should  be overridden when extending a Thread class
run()
Pregunta 78:
When a thread use wait() method what shold be invoked when it is done with its work so that other thread can run
notify()
Pregunta 79:
What are the parameters that we pass to the Socket bind method
host, port
Pregunta 80:
Which of the following will create a email server object?
smtplib.SMTP('smtp.gmail.com' ,587)
Pregunta 81:
Which of the below are the parameters passed to the connect method?
host, database, username,password
Pregunta 82:
Which object holds the data that comes back from a select query
cursor
Pregunta 83:
The commit method exists on which of the following object
connection
Pregunta 84:
Which method on the cursor object is used to run sql queries
execute


'''

