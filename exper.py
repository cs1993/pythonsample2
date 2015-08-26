__author__ = 'chandrashekhar'
import largestlist

money=2000
def addmoney():
    global money
    money = 10
    money = money + 1
    #print money
    reload(largestlist)


print money
addmoney()
print money