file1 = open("2013_14_Entities.txt","r")
file2 = open("entitiesoutput14.txt","a")

file_str = file1.readlines()
file2.write(file_str[0])
for i in range(1, len(file_str)):
    str0 = file_str[i].split('\t')
    str0[-1] = str0[-1].rstrip()
    new_str = str0[0:7]
    last = '"' + ','.join(str0[7:]) + '"'
    
    new_str.append(last)
    final = ','.join(new_str) + '\n'
    file2.write(final)

print("success")

file1.close()
file2.close()
