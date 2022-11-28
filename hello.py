import math
print("hello world!")
# this is a comment
'this is also a comment'
'''
this is how you would comment a function
or if you have many lines of code to comment
'''

int_example = 5
float_example = 5.5

x = 5
x = "this is a string"

result = 5.5 // 4
print(result)

result = 5.5 % 4
print(result)

squared = 5 ** 2
print(squared)

squared = math.pow(5,2) 
print(squared)

if squared == 25:
    print("correct")
else:
    print("something went wrong")

x = 10
y = 100

if x >= 10 or y < 90:
    print("at least one statement is true")

grade = 90
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
else:
    letter = "D"

print(letter)

first_name = "maya"
last_name = "mcfadden"
full_name = first_name + ' ' + last_name
repeat = first_name * 5

print(full_name)
print(repeat)

# string slicing
first_two = first_name[0:2] # first number is inclusive, second is exclusive
print(first_two)

last_letter = first_name[-1]
print(last_letter)

if 'm' in first_name:
    print("m in first name")


for i in range(len(first_name)):
    if first_name[i] == 'a':
        print("found an a")

lst1 = []
lst1.append(10)
lst1.append(20)
lst1.append(30) 
print(lst1)

# define a function
def hello(name):
    print("Hello", name)

hello("Joe")

def hello_default_arg(name="to whom it may concern"):
    print("Hello", name) 

hello_default_arg("Joe")
hello_default_arg()

def return_two():
    return 1, 5

x, y = return_two()
print(x,y)