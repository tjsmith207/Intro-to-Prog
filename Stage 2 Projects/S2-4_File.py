# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

#print 2 < 3
#print 21 < 3
#print 7 * 3 < 21
#print 7 * 3 != 21
#print 7 * 3 == 21

# Messing around before the lesson...

#def compare(a, b):
#    if a < b:
#        return 'less than'
#    else:
#        return 'greater than'

#print compare(2, 3)
#print compare(21, 3)

# Lesson examples...

#print "Example 1: Greater-than and less-than comparisons"
#print 2 > 1
#print 1 > 2
#print 5 < 20
#print 100 < 19

#print "Example 2: Equality and non-equality comparisons"
#print 5 == 5
#print "hello" == "hello"
#print 5 == 10
#print 5 == '5' # what do you think will happen here?
#print 7 != 10
#print 7 != 7

#print "Example 3: A demo of what you are about to learn"
#if 3 < 5:
#    print "Three is definitely smaller than 5!"

#if 10 > 20:
#    print "Did you know that 10 is greater than 20!?"
#else:
#    print "20 is greater than 10"


# Quiz Number 1...

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

#def bigger(a, b):
#    if a > b:
#        return a
#    else:
#        return b

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3


# Quiz Number 2...

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

#def is_friend(s):
#    if s [0] == 'D':
#        return True
#    else:
#        return False

#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False


# Quiz Number 3...

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

#def is_friend(name):
#    if name[0] == 'D' or name[0] == 'N':
#        return True
#    else:
#        return False

#print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

#print is_friend('Moe')
#>>> False


# Quiz Number 4...

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#def biggest(n1, n2, n3):
#    if n1 >= n2 and n1 >= n3:
#        return n1
#    if n2 >= n1 and n2 >= n3:
#        return n2
#    if n3 >= n1 and n3 >= n2:
#        return n3

# Alternate way...more efficient

#def biggest(n1, n2, n3):
#    return max(n1, n2, n3)

#print biggest(1, 2, 3)
#print biggest(3, 1, 2)
#print biggest(2, 3, 1)
#print biggest(1, 3, 2)
#print biggest(3, 2, 1)
#print biggest(2, 1, 3)
#print biggest(2, 2, 1)


# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

#def count():
#    i = 0
#    while i != 10:
#        i = i + 1
#        print i

#count()

#def count():
#    i = 1
#    while i != 10: # Careful...this will never get to 10 and is an infinite loop
#        i = i + 2
#        print i

#count()


# This code demonstrates a while loop with a "counting variable"
#i = 0
#while i < 10:
#    print i
#    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?

#def remove_spaces(text):
#    text_without_spaces = '' #empty string for now
#    while text != '':
#        next_character = text[0]
#        if next_character != ' ':    #that's a single space
#            text_without_spaces = text_without_spaces + next_character
#        text = text[1:]
#    return text_without_spaces
#print remove_spaces("hello my name is andy how are you?")


# Quiz Question...

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    y = 0
    while n > y:
        y = y + 1
        print y

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3