"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.
"""
thistuple = ("apple", "banana", "cherry",1,2)
print(thistuple)


#if u want to change the touple values first store touple values in a list
test=[12,"hello","world","pakistan"]
x=list(test)
print(type(x))
x[1]=14
test=tuple(x)
print(test)

for res in test:
    print(res)
