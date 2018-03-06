email = "srini@gmail@tcs@infosys"
output_list = []
concatenated_str = " "
for each in email:
    if each !='@':
       concatenated_str = concatenated_str + each
    else:
       output_list.append(concatenated_str)
       output_list.append('@')
       concatenated_str = " "
print output_list
