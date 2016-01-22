# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.


# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

import datetime
import calendar

def isLeapYear(year):
    return calendar.isleap(year)

print isLeapYear(1991)

def daysInMonth(year,month):
    days = calendar.monthrange(year,month)
    return days[1]

print daysInMonth(2012,4)

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year,month,day +1
    elif day == daysInMonth(year, month):
        if month < 12:
            return  year, month+1,1
        elif month == 12:
            return year+1,1,1

print nextDay(2012,1,1)
print nextDay(2012,4,30)
print nextDay(2012,12,1)
print nextDay(1999,12,30)
print nextDay(2012,12,30)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    x = (year1,month1,day1)
    y = (year2,month2,day2)
    if x < y:
        return True
    else:
        return False

print dateIsBefore(2013,1,1,1999,12,31)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    a = datetime.date(year1,month1,day1)
    b = datetime.date(year2,month2,day2)
    if a < b:
        c = b-a
        return c.days
    elif a > b:
        c = a-b
        return c.days

print daysBetweenDates(2013,1,1,1999,12,31)
print daysBetweenDates(1991,3,1,1991,1,3)
print daysBetweenDates(2012,9,1,2012,9,4)
print daysBetweenDates(2012,9,4,2012,9,1)

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((2013,1,1,1999,12,31),4750),
                  ((1991,3,1,1991,1,3),57)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()