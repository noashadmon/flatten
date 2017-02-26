def flatten(l):
    #checks to see if the list is iterable
    if hasattr(l, "__iter__"):
        return [element for sublist in l for element in flatten(sublist)] #recursive call to flatten each sublist
    else:
        return [l]

print "Input is: flatten([0, 2, [[2, 3], 8, 100, None, [[None]]], -2])"
print flatten([0, 2, [[2, 3], 8, 100, None, [[None]]], -2])

print "Input is: flatten([[[[[[[6]]]]]]])"
print flatten([[[[[[[6]]]]]]])

print "Input is: flatten([[[[[7],3]],[10,2]]])"
print flatten([[[[[7],3]],[10,2]]])

print "Intput is: flatten([1,2,3,4])"
print flatten([1,2,3,4])

print "Input is: flatten(5)"
print flatten(5)

print "Input is: flatten(qqq)"
print flatten(qqq)
