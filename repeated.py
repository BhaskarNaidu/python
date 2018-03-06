list = [1,1,2,3,1,2,3,2]
count = 0
count1 = 0
count2 = 0
for each in list:
    if each == 1:
        count = count + 1
    elif each == 2:
        count1 = count1+ 1
    elif each == 3:
        count2 = count2 + 1
print "1 is repeated {} times ".format(count)
print "2 is repeated {} times ".format(count1)
print "3 is repeated {} times ".format(count2) 
