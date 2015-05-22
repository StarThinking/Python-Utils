def flatten(nested):
    try:
        for sublist in nested:
	    for element in flatten(sublist):
		yield element
    except TypeError:
	yield nested

nested = [[1,2],3]
print list(flatten(nested))

