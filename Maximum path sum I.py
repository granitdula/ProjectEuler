##import time
##start = time.time()
##
##def groupList(oldList):
##    nthTriNum = 0
##    prevNthTriNum = 0
##    newList = []
##    for i in range(1, len(oldList) + 1):
##        nthTriNum = int(i * (i + 1) * 0.5)
##        if nthTriNum > len(oldList):
##            break
##        tempList = oldList[prevNthTriNum:nthTriNum]
##        newList.append(tempList)
##        prevNthTriNum = nthTriNum 
##    return newList       
##    
##numberPyramid = '75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
###numberPyramid = '3 7 4 2 4 6 8 5 9 3'
##numberList = numberPyramid.split(" ")
##
##total = int(groupedList[0][0])
##index = 0
##for row in groupedList[1:]:
##    if int(row[index]) > int(row[index + 1]):
##        total += int(row[index])
##    else:
##        total += int(row[index + 1])
##        index += 1
##
##print(total)
### The code just above is what I initially thought the task was but its a bit harder
### than that
##
##
##elapsed = str(time.time() - start)
##print("Time taken to run: {0}".format(elapsed, 'seconds'))

import time
start = time.time()
 
triangle = [
 [75],
 [95, 64],
 [17, 47, 82],
 [18, 35, 87, 10],
 [20, 4, 82, 47, 65],
 [19, 1, 23, 75, 3, 34],
 [88, 2, 77, 73, 7, 63, 67],
 [99, 65, 4, 28, 6, 16, 70, 92],
 [41, 41, 26, 56, 83, 40, 80, 70, 33],
 [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
  
# Loop through each row of the triangle starting at the base.
for a in range(len(triangle) - 1, -1, -1):
    for b in range(0, a):  
        # Get the maximum value for adjacent cells in current row.
        # Update the cell which would be one step prior in the path
        # with the new total. For example, compare the first two
        # elements in row 15. Add the max of 04 and 62 to the first
        # position of row 14.This provides the max total from row 14
        # to 15 starting at the first position. Continue to work up
        # the triangle until the maximum total emerges at the
        # triangle's apex.
        triangle [a-1][b] += max(triangle [a][b], triangle [a][b+1])
  
   
print(triangle [0][0])
print ("Elapsed Time:", (time.time() - start) * 1000, "millisecs")

a=input('Press return to continue')

