# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

#speed_of_light = 299792458.0 # meters per second
#billionth = 1.0 / 1000000000.0
#nanostick = speed_of_light * billionth * 100
#print nanostick

#cycles_per_second = 2700000000.0 # 2.7 Ghz Processor

# Add your own code and notes here

# given the above variables write Python code that prints out
# the distance, in meters, that light travels in one
# processor cycle

#distance = speed_of_light / cycles_per_second
#print distance


# Quiz Question...Answer is 20

#hours = 9
#hours = hours + 1
#hours = hours *2
#print hours


# Quiz Question - What is the value of seconds after running this code

#minutes = 0 + 1
#seconds = minutes * 60
#print seconds


# Quiz Question -
# Write Python code that defines the variable age
# to be your age in years, and then prints
# out the number of days you have been alive.

#age = 47
#days = age * 365
#print days


# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

#print 'Hello'
#print "Hello"

#hello = "Howdy"
#print hello

# Quiz question...Define a variable, name, and assign to it a string that is your nam.

#name = "Tracey"
#print name

# Quiz Question...Given the variable s = '<any string>'
# which of these pairs are two things with the exact same value?

#s = "about"
#print s[3], s[1 + 1 + 1]
#print s[0], (s + s)[0]
#print s[0] + s[1], s[0 + 1]
#print s[1], (s + 'ity')[1]
#print s[-1], (s + s)[-1]
#print s[2:4]

#Quiz Question...For any string s = '<any string>'
#which of these is always equivalent to s:

#s = 'string'
#print s[:]
#print s + s[0:-1+1]
#print s[0:]
#print s[:-1]
#print s[:3] + s[3:]

#Quiz Question...for any string s ='<any string>'
#which of the following always has the value 0?

#s = 'hello' #don't use the string 'string'
#print s.find(s)
#print s.find('s')
#print 's'.find('s')
#print s.find('')
#print s.find(s + '!!!') + 1

# Examples...

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

#print "Example 1: Finding substrings in a string"
#print "test".find("te")
#print "test".find("st")
#print "test"[2:]

#print "Example 2: Finding substrings in a string which is stored as a variable"
#my_string = "test"
#print my_string.find("te")
#print my_string.find("st")
#print my_string[2:]

#print "Example 3: Printing out everything after a certain substring"
#my_string = "My favorite color: blue"
#color_start_location = my_string.find("color:")
#favorite_color = my_string[color_start_location:]
#print favorite_color # oops, this line prints out 'color: ' as well...
#print favorite_color[7:] # this fixes it!

#print "Example 4: Other interesting things about string.find()..."
#print "text".find("text") # prints 0
#print "text".find("Text") # prints -1
#print "text".find("")     # prints 0
#print "text".find(" ")    # prints -1

#Second example...

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

#print "Example 1: using find to print the second occurrence of a sub-string"
#print "test".find("t")
#print "test".find("t", 1)

#print "Example 2: using a variable to store first location"
#first_location = "test".find("t") # here we store the first location of "t"
#print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

#print "Example 3: using find to get rid of exclamation marks!!"
#example = "Wow! Python is great! Don't you think?"
#first = example.find('!')
#second = example.find('!', first + 1)
#new_string = example[:first] + example[first+1:second] + example[second+1:]
#print new_string # oops, I should probably replace the !s with periods
#new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
#print new_string

#2.2 Worksession

# Write Python code that prints out the number of hours in 7 weeks.

#print 7 * 24 * 7

#Given any string s, which of the following always have the same value as s?
#(Be careful, s could be ''.)

#s = ''
#print ('a' + s)[1:]
#print s + ''
#print s[0] + s[1:]
#print s[0:]

# Given the variables s and t defined as:
#s = 'udacity'
#t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

#print s[:2] + t[3:]

# Insert the proper slicing indices for the substring variable
# so that the slice is a string that contains everything after "A NOUN".
# For example, if we wanted to store everything after "went", the returned
# string would be equal to sentence[11:].

#sentence = "A NOUN went on a walk."
#substring = sentence[6:]
#print substring

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB"
# in substring3.

#sentence = "A NOUN went on a walk. It can VERB really fast."
#substring1 = sentence[:2]
#substring2 = sentence[6:30]
#substring3 = sentence[34:]
#print sentence.find("N")
#print sentence.find(" ", 2)
#print sentence.find("V")
#print sentence.find("B")
#print substring1
#print substring2
#print substring3


# Set noun_replacement and verb_replacement to your own noun and verb strings.
# Then, concatenate the variables substring1-3, noun_replacement, and
# verb_replacement and assign the result to the variable new_sentence so that
# it's in the same order as the variable sentence.

#sentence = "A NOUN went on a walk. It can VERB really fast."
#substring1 = sentence[0:2]
#substring2 = sentence[6:30]
#substring3 = sentence[34:]

#noun_replacement = "duck" # your noun here
#verb_replacement = "waddle" # your verb here

#new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
#print new_sentence


# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America.
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

#mary = "Mary"
#katie = mary
#randa = katie
#salwa = katie
#kathleen = salwa
#gabriel = kathleen

# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
#gabriel = kathleen

# Test to see if all of these variables will print out the string "Mary"
#print gabriel
#print kathleen
#print salwa
#print katie
#print randa
#print mary


# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

#text = """Wow this is a fairly long body of text. Quite a few characters too.
#I wonder if the string.find method could help find where NOUN is located.
#That way, I could go out and VERB with my friends rather than counting characters
#all day long!"""

#noun_position = text.find('NOUN')
#verb_position = text.find('VERB')
#print noun_position
#print verb_position


# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
#text = 'all zip files are compressed'
# >>> -1

#text = "all zip files are zipped"
#first_location = text.find('zip')
#print text.find('zip', first_location +1)

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function


# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

#sentence = "A NOUN went on a walk. They can VERB really well."
#sentence = sentence.replace("NOUN","duck")
#sentence = sentence.replace("VERB","waddle")
#print sentence