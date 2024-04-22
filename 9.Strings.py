#string as an array
a="Hello"
print(a[1])

"""""
The for loop in Python is used to iterate over a sequence 
(such as a list, tuple, string, or range) and 
perform an action for each item in the sequence. 
It is often used when you know how many times you 
want to loop or when you want to iterate over a known sequence of elements.
"""
#for in loop through an array
numbers=[1,2,3,4,5]
for number in numbers:
    print(number)

#for in loop through an string
b="Hello world"
for res in b:
    print(res)

#see the lenght
print(len(b))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
#it returns boolean true or false
c="I love Pakistan"
print("love" in c)
if "Pakistan" in c:
    print("Yes Pakistan is present")