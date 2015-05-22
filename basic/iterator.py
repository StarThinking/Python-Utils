from collections import Iterable

class IterTest(object):

    def check_iter(a):
    if not isinstance(a, Iterable):
	print "not iterable"
    else:
	print "iterable"
a = [1,2,3]
check_iter(a)

#for aa in a.__iter__():
#    print aa  

l = list(a) 
print l 
