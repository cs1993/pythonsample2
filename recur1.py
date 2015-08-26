__author__ = 'chandrashekhar'
def rec(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a+rec(a, b-1)


a=input("enter a no: ")
b=input("enter 2nd no: ")
print "product of a and b is=",rec(a,b)