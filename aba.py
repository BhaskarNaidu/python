name = "sriababaxyz"
search_str = "aba"
counter = 0
y = 0
for each in name:
    res = name[y:y+3]
    y = y+1
    if res == search_str:
       counter = counter + 1
print "{} is repeated {} times".format(search_str, counter) 
