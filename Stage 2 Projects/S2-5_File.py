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


# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

#def weekend(day):
#    if day == 'Saturday' or day == 'Sunday':
#        return True
#    else:
#        return False

#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False

#print weekend('Sunday')
#>>> False


# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

#def print_numbers(n):
#    y = 0
#    while n > y:
#        y = y + 1
#        print y

#print_numbers(3)


#def countdown(n):
#    c = n
#    while c != 0:
#        print c
#        c = c - 1
#    print 'Blastoff!'

#countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# Alternative (and simpler) solution to the above...

#def countdown(n):
#    while n > 0:
#        print n
#        n = n -1
#    print 'Blastoff'

#countdown(10)

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#def bigger(a,b):
#    if a > b:
#        return a
#    else:
#        return b

#def biggest(a,b,c):
#    return bigger(a,bigger(b,c))


# def median(a,b,c):
#     d = min(a,b,c)
#     e = max(a,b,c)
#     med = 0
#     if a == d and b == d:
#         med = d
#     elif a == d and c == d:
#         med = d
#     elif b == d and c == d:
#         med = d
#     elif a == e and b == e:
#         med = e
#     elif a == e and c == e:
#         med = e
#     elif b == e and c == e:
#         med = e
#     elif a > d and a < e:
#         med = a
#     elif b > d and b < e:
#         med = b
#     elif c > d and c < e:
#         med = c
#     return med

# def median(a,b,c):
#     x = sorted([a,b,c])
#     return x[1]
#
# print(median(1,2,3))
# #>>> 2
#
# print(median(9,3,6))
# #>>> 6
#
# print(median(7,8,7))
# #>>> 7
#
# print(median(1,2,2))
# #>>> 7


# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".

#from random import randint

#def random_noun():
#     a = randint(0,1)
#     if a == 0:
#         return 'sofa'
#     else:
#         return 'llama'

#print random_noun()


# Write code for the function random_verb, which takes in no inputs but outputs
# one of two verbs randomly. Use the randint function to generate a number from 0-1
# and return a verb depending on whether the number is equal 0 or 1. Feel free to
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

#from random import randint

#def random_verb():
#    rand_verb = randint(0,1)
#    if rand_verb == 0:
#        return 'run'
#    else:
#        return 'kayak'

#print random_verb()


# Write code for the function word_transformer, which takes in a string word as input.
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB",
# return a random verb, else return the first character of word.

# from random import randint
#
# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return 'run'
#     else:
#         return 'kayak'
#
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return 'sofa'
#     else:
#        return 'llama'

# def word_transformer(word):
#    if word == 'VERB':
#        return random_verb()
#    if word == 'NOUN':
#        return random_noun()
#    else:
#        return word[:1]
#

# def word_transformer(word):
#     output = ''
#     if word == 'VERB':
#         output = random_verb()
#     elif word == 'NOUN':
#         output = random_noun()
#     else:
#         output = word[0]
#     return output
#
# print word_transformer('stick')
# # Should return s
#
# print word_transformer('NOUN')
# # Should return random noun
#
# print word_transformer('VERB')
# # Should return random verb
#
# print word_transformer('Ball')
# # Should return random verb
#
# print word_transformer('taco')
# # Should return random verb


# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

# from random import randint
#
# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return "run"
#     else:
#         return "kayak"
#
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return "sofa"
#     else:
#         return "llama"
#
# def word_transformer(word):
#     if word == "NOUN":
#         return random_noun()
#     elif word == "VERB":
#         return random_verb()
#     else:
#         return word[0]

    # My solution involves the string.replace method below...

# def process_madlib(mad_lib):
#     processed = mad_lib.replace('NOUN',word_transformer('NOUN'))
#     processed = processed.replace('VERB',word_transformer('VERB'))
#     return processed

    # The Udacity solution is below and it doesn't work...

# def process_madlib(mad_lib):
#     processed = ''
#     index = 0
#     box_length = 4
#     while index > len(mad_lib):
#         frame = mad_lib[index: index + box_length]
#         to_add = word_transformer(frame)
#         processed += to_add
#         if len(to_add) == 1:
#             index = += 1
#         else:
#             index += 4
#     return processed

    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len

# test_string_1 = "This is a good NOUN to use when you VERB your food"
# test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
#
# print process_madlib(test_string_1)
# print process_madlib(test_string_2)
