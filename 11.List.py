#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python
#used to store collections of data, the other 3 are Tuple, 
# Set, and Dictionary, all with different qualities and usage.

firstList=["Apple","Orange","Peach"]
print(firstList)
print(len(firstList))

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], 
#the second item has index [1] etc.
#A list can store different data types
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))
print(list1[1])

#Negative indexing means start from the end
print(list1[-1])

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To insert a list item at a specified index, use the insert() method.
thislist.insert(1,"peach")
print(thislist)

#The remove() method removes the specified item.
#The pop() method removes the specified index.
thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(thislist1)
thislist1.pop(1)
print(thislist1)
