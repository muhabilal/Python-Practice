#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
def myFun(nums):
    return nums.count(19)==2 and nums.count(5)>=3
nums=[19, 19, 15, 5, 3, 5, 5, 2]
print(myFun(nums))

