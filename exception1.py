__author__ = 'chandrashekhar'
class Networkerror(RuntimeError):

    error_msg = None
    def __init__(self,msg):
        self.a = msg
        print self.a


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print e