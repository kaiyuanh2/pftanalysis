file1 = open("2012_13_ResearchFile.txt","r")
file2 = open("researchoutput13.txt","a")

file_str = file1.readline()
file2.write(file_str)
file_str = file1.readline()
while(file_str):
    str0 = file_str.split(',')
    for i in range(0, len(str0)):
        str0[i] = str0[i].strip()
        str0[i] = str0[i][1:-1].strip()
    final = (','.join(str0)) + "\n"
    file2.write(final)
    file_str = file1.readline()

print("success")
file1.close()
file2.close()

