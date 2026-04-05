import pandas as pd
import numpy as np 
from datetime import *

myyear=2005
mymonth=9
myday=5  
myhour=12
mymin=20
mysec=15
'''datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.'''
mydata= datetime(myyear,mymonth,myday,myhour,mymin,mysec)
print(mydata)
myser = pd.Series(['Nov 3, 2000', '2000-01-01', None])
print(myser) #this doesnt read the above list as a timedata 
#to read the above list as a timedata we use the pd.to_datetime() function
t1 = pd.to_datetime(myser, errors='coerce')
print(t1)
