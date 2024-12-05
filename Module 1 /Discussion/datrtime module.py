'''
The datetime module provides a number of class types to deal with dates, times, and time intervals with a more object-oriented interface. Please list the main object class types and explain their usage.
'''

text = '''

Python DateTime module
Python Datetime module supplies classes to work with date and time. These classes provide several functions to deal with dates, times, and time intervals. Date and DateTime are an object in Python, so when you manipulate them, you are manipulating objects and not strings or timestamps. 

The DateTime module is categorized into 6 main classes:

1. datetime.date class: Represents a date (year, month, and day) without any time component. Its attributes are year, month, and day. 

e.g: 
 
from datetime import date
d = date(2024, 11, 12)
print(d) # Output: 2024-11-12

2. datetime.time: Represents a time of day (hours, minutes, seconds, and microseconds) without any date component. Its attributes are hour, minute, second, microsecond, and tzinfo. 

e.g:
from datetime import time
t = time(14, 30, 15)
print(t)  # Output: 14:30:15

3. datetime.datetime : It is a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.

e.g:
from datetime import datetime
dt = datetime(2024, 11, 23, 14, 30, 15)
print(dt)  # Output: 2024-11-23 14:30:15

4. datetime.timedelta : A duration expressing the difference between two dates or time, or datetime instances to microsecond resolution.  Its attributes are days, seconds, microseconds.

e.g:
from datetime import timedelta
delta = timedelta(days=5, hours=3)
print(delta)  # Output: 5 days, 3:00:00

5. datetime.tzinfo: (abstract base class)
- It provides time zone information objects. 
- Used as a base class for implementing timezone information
- Common Subclass: datetime.timezone (a concrete implementation).

from datetime import timezone, timedelta
tz = timezone(timedelta(hours=5, minutes=30))  # UTC+5:30
print(tz)  # Output: UTC+05:30

6. datetime.timezone : A class that implements the tzinfo abstract base class as a fixed offset from the UTC. Basically a subclass of tzinfo that represents a fixed offset from UTC.

e.g

from datetime import timezone, timedelta
tz = timezone(timedelta(hours=5, minutes=30))
dt = datetime(2024, 11, 23, 14, 30, tzinfo=tz)
print(dt)  # Output: 2024-11-23 14:30:00+05:30

'''

print(text)

print("\nSummary Table\n")
print("Class\t\t\tPurpose\t\t\t\t\t\tExample")
print("date\t\t\tRepresents a date without time\t\t\tdate(2024, 11, 23)")
print("time\t\t\tRepresents a time without date\t\t\ttime(14, 30, 15)")
print("datetime\t\tCombines date and time\t\t\t\tdatetime(2024, 11, 23, 14, 30)")
print("timedelta\t\tRepresents a duration.\t\t\t\ttimedelta(days=5, hours=3)")
print("tzinfo\t\t\tBase class for timezone information\t\tUsed for custom timezone handling.")
print("timezone\t\tFixed offset from UTC\t\t\t\ttimezone(timedelta(hours=5))")
