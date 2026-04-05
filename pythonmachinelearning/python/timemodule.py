#time module in python 
#a computers epoch is the date and time from which a computer's time is calculated
#the epoch is usually set to 1 January 1970, 00:00:00 UTC   
#to find a computers epoch we can use time module (time.ctime(0))
import time 
print("epoch is", time.ctime(0))
# the argument to time.ctime() is the number of seconds since the epoch
# we can use time module to find the current time
current_time = time.ctime()
print("current time is", current_time)
# we can also pass a number of seconds to time.ctime() to find the time at that moment 
print("time at 100000 seconds since epoch is", time.ctime(100000))
#the ctime method returns a string representing the time in a human-readable format
# we can also use time module to find the current time in seconds since epoch
current_time_seconds = time.time()
print("current time in seconds since epoch is", current_time_seconds)
#local time is the time in the local timezone 
local_time = time.localtime()
print("local time is", time.asctime(local_time))
#the sleep function in the time module Delay execution for a given number of seconds. The argument may be
print("eating breakfast")
time.sleep(3)
print("done eating breakfast")




