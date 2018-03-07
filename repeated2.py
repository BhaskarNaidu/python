list = [1,2,1,2,3,3,1,2]
for each in list:
    processed_list = []
for each in list:
    if each not in processed_list:
        print "{} is repeated {} times ".format(each, list.count(each))
        processed_list.append(each)
