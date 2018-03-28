import time
start = time.time()

def isLeapYear(year):
    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0 and year % 100 == 0):
        return True
    else:
        return False

monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30,
             12:31}
weekNum = 2 # Monday on Jan 01 1900 so Tuesday on Jan 01 1901 since
            # 365 % 7 = 1 so 1 day more than Monday.
numOfSundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if isLeapYear(year):
            if month == 2:
                weekNum = (weekNum + 29) % 7 
            else:
                weekNum = (weekNum + monthDays[month]) % 7
            if weekNum == 0:
                numOfSundays += 1
        else:
            weekNum = (weekNum + monthDays[month]) % 7
            if weekNum == 0:
                numOfSundays += 1
            
print(numOfSundays)
elapsed = str(time.time() - start)
print("Time taken: {0}".format(elapsed, "seconds"))
    
    
