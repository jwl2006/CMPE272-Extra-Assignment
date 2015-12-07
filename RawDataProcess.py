f=open('./NASA_Facilities.csv')
f2=open('./change.csv','w')
file = f.readline().strip('\n')
f2.write(file+'\n')
while 1:
    file = f.readline().strip('\n')
    if file:
        file2 = f.readline()
        file = file + " , " +  file2
        print file
        f2.write(file)
    else:
        break
f.close()
f2.close()
