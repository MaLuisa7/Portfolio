#dt Demo

import time
epochseconds = time.time()
print(epochseconds)

t = time.ctime(epochseconds)
print(t)

#finiding the current date and time
import datetime
dt = datetime.datetime.today()
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current time: {},{},{}'.format(dt.hour, dt.minute, dt.second))

#Combining date and time
from datetime import *
d = date(2018,7,21)
t = time(12,45)
dt = datetime.combine(d,t)
print(dt)

#sorting dates
from datetime import *

ldates = []
d1 = date(2016,8,12)
d2 = date(2016,7,12)
d3 = date(2018,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for d in ldates:
    print(d)


#sleep
from datetime import *
import time

ldates = []
d1 = date(2016,8,12)
d2 = date(2016,7,12)
d3 = date(2018,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(3)
for d in ldates:
    print(d)

#Knowing the execution time of a program

from datetime import *
import time

starTime = time.perf_counter()

ldates = []
d1 = date(2016,8,12)
d2 = date(2016,7,12)
d3 = date(2018,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(3)
for d in ldates:
    print(d)

endTime = time.perf_counter()

print('Execution time',  endTime- starTime )