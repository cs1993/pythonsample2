__author__ = 'chandrashekhar'


try:
    fo = open("/home/chandrashekhar/list1", "a+")
    str=fo.read()
    print "read string is: ",str
    p=fo.tell()
    print "position of cursor in file is: ",p
    fo.write("\nAnd also it is a great language\n Is't it cs\n")
    fo.write("n yes,it is\n and you know ,I like you ")
    print fo.mode
    print fo.closed
    #fo.write("Python is a great language\n Is't it")
except IOError as e:
    print e
finally:
     fo.close()
