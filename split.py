email = "sri@gmail@tcs@infosys"
split_res = email.split('@')
print split_res
output_list =[]
for each in split_res:
    output_list.append(each)
    output_list.append('@')
print output_list
