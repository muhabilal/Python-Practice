#Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
def myFun(num):
    return len(num)==8 and num.count(5)==3
num=[19, 19, 15, 5, 5, 5, 1, 2]
print(myFun(num))
