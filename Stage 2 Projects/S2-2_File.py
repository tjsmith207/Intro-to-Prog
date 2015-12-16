# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0 # meters per second
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

cycles_per_second = 2700000000.0 # 2.7 Ghz Processor

# Add your own code and notes here

# given the above variables write Python code that prints out
# the distance, in meters, that light travels in one
# processor cycle

distance = speed_of_light / cycles_per_second
print distance


# Quiz Question...Answer is 20

hours = 9
hours = hours + 1
hours = hours *2
print hours


# Quiz Question - What is the value of seconds after running this code

minutes = 0 + 1
seconds = minutes * 60
print seconds


# Quiz Question -
# Write Python code that defines the variable age
# to be your age in years, and then prints
# out the number of days you have been alive.

age = 47
days = age * 365
print days


# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Quiz question...Define a variable, name, and assign to it a string that is your nam.

name = "Tracey"
print name

# Quiz Question...Given the variable s = '<any string>'
# which of these pairs are two things with the exact same value?

s = "about"
print s[3], s[1 + 1 + 1]
print s[0], (s + s)[0]
print s[0] + s[1], s[0 + 1]
print s[1], (s + 'ity')[1]
print s[-1], (s + s)[-1]
print s[2:4]

#Quiz Question...For any string s = '<any string>'
#which of these is always equivalent to s:

s = 'string'
print s[:]
print s + s[0:-1+1]
print s[0:]
print s[:-1]
print s[:3] + s[3:]

#Quiz Question...for any string s ='<any string>'
#which of the following always has the value 0?

s = 'hello' #don't use the string 'string'
print s.find(s)
print s.find('s')
print 's'.find('s')
print s.find('')
print s.find(s + '!!!') + 1

# Examples...

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1

#Second example...

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string