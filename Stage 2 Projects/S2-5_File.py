# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

#def bracket(text):
#    return '[' + text + ']'

#def boldwrap(text):
#    return '<b>' + text + '</b>'

#print boldwrap('This is an important message.')



# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

#def remove(somestring, sub):
#    """Return somestring with sub removed."""
#    location = somestring.find(sub)
#    if location == -1:
#        return  somestring
#    length = len(sub)
#    part_before = somestring[:location]
#    part_after = somestring[location + length:]
#    return part_before + part_after


#
# Don't change these test cases!
#print remove('audacity', 'a')
#print remove('pythonic', 'ic')
#print remove('substring institution', 'string in')
#print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
#print remove('doomy', 'dooming')  # and this should print "doomy"
