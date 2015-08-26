__author__ = 'chandrashekhar'

from ast import literal_eval
s1=input("enter the string which you want to convert into dictionary:")
#d=literal_eval(s1)
s2=input("enter the string which you want to convert into dictionary:")
s1.update(s2)
print s1