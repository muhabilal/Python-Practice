def myfun():
    print("hello pakistan")
myfun()


#The terms parameter and argument can be used for the same thing: information that are passed into a function.

#From a function's perspective:

#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the value that is sent to the function when it is called.

def cal(a,b):
    print("The sum {a1} and {b1} is: ".format(a1=a,b1=b),a+b)

cal(2,4)