# Read through the code below. Even if you don't understand it, try to make
# a guess about what it does. What do you think will happen when you press
# "Test Run"? Once you have a prediction, press "Test Run" and compare what
# happens to what you predicted.

#def say_hello():
#    return "Hello!"
#print say_hello()

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing.

# Continue to the next example to see a more interesting version of say_hello.


# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time.
#
# Read through the code and try to predict what the output will be when
# you press "Test Run"

#def say_hello(name):
#    greeting = "Hello " + name + "!"
#    return greeting

#print say_hello("Miriam")
#print say_hello("Andy")


#def say_hello(name):
#    greeting = "Hello " + name + '!'
#    return greeting
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
#def add_two_numbers(number_1, number_2):
#    return number_1 + number_2

#print add_two_numbers(4, 3)
#print add_two_numbers(2, 6)
#print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the
# code below and then make ONE modification so that the function does
# what the name says it should do.

#def subtract_two_numbers(number_1, number_2):
#    return number_1 + number_2

#print subtract_two_numbers(4, 3)


# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

#def rest_of_string(s):
#    return s[1:]

#print rest_of_string('audacity')

#def inc(n):
#    return n + 1
# This does nothing, but the example points out that it adds 1 to an input number

#def sum(a, b):
#    print "Enter Sum!"
#    print "A is" , a
#    a = a + b
#    print "A is" , a

#print sum(2, 123)


#a = 1
#b = 2

#def sum(a, b):
#    a = a + b
#    return a

#print sum(a, b)

# Use of if and else

#def some_function(some_value):
#    if type(some_value) == type(1):
#        return 1
#    else:
#        return "Not an Int"

#print some_function(25)
#print some_function(25.0)

#def some_function(some_value):
#    some_list = []
#    for e in range(10):
#        some_list.append(some_value)
#    return some_list

#print some_function(25)
#print some_function(25.0)

# Recursion Example...

#def some_function(some_value, count):
#    print some_value
#    if count == 0:
#        return some_value
#    else:
#        return some_function(some_value + 1)

#print some_function(25, -1)

# Quiz Question...

# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
#    c = a + b
#    return c

#def square(n):
#    return n * n

#print square(5)

# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25


# Quiz Question...

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
#    return a + b


#def sum3(a,b,c):
#    return a + b + c

#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

# Quiz Question...

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

#def abbaize(s1, s2):
#    return s1 + s2 + s2 + s1

#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

# In addition to using single quotes (') or double quotes (")
# to create a string, you can also use TRIPLE quotes to create
# a multi-line string.

#print """I am a string
#that takes up
#multiple lines."""

#print '''I am also a string
#that makes up multiple lines!'''

#print '''
#<div class="concept">
#    <div class="concept-title">
#        Multi-line strings
#    </div>
#    <div class="concept-description">
#        Multi-line strings can be made with triple single
#        quotes or triple double quotes. But I'm not sure
#        why they are useful yet.
#    </div>
#</div>
#'''

# Look through these two solutions. They both solve the problem,
# but one of them is "better" in a way. Try to identify which is
# better and why.

################################################################
# Solution One - Uses negative indexing

#div_element = "<div>I am learning to code!</div>"

#opening_tag = div_element[:5]
#indent      = '    ' # this is just a string with 4 spaces.
#inner_text  = div_element[5:-6]
#closing_tag = div_element[-6:]

#print opening_tag
#print indent + inner_text
#print closing_tag

################################################################
# Solution Two - Does not use negative indexing

#div_element = "<div>I am learning to code!</div>"

#opening_tag = div_element[:5]
#indent      = '    ' # this is just a string with 4 spaces.
#inner_text  = div_element[5:27]
#closing_tag = div_element[27:]

#print opening_tag
#print indent + inner_text
#print closing_tag


# Work Session Question...

# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

#def udacify(s1):
#    return 'U' + s1

# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat

# Work Session Quiz

# Which ones print?

#def double1(x):
#    return 2 * x # No Print Statement

#def double2(x):
#    print 2 * x # This Prints

#def double3(x):
#    return 2 * x
#    print 2 * x # This won't print because it's after the return statement

#def double4(x):
#    print 2 * x # This Prints
#    return 2 * x

