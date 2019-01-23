#Convert log file to text or csv file

with open('/home/naveed/Dropbox/Pallet_Jack/1_19_forward.log') as file: #path of the file to be read
    lines = file.read().splitlines() #split the file into lines
    #lines = [lines[x:x+3] for x in range(0, len(lines), 3)]
    print "length:", len(lines)
    i=0
    while(1):
        dat = lines[i].split(' ') #split at space
        #189 is the chosen identifier
        if dat[2][0] == '2':
            if dat[2][1] == '8':
                if dat[2][2] == '9':
                    #print dat[2]

                    #writing into text file
                    file = open('1_19_forward.csv', 'a+') #name of the file to be written
                    file.write(str(float(dat[0][1:18])-1547668991.0000 ))
                    #print str(float(dat[0][1:18])-1547668991.0000)
                    file.write(',')
                    for j in [0,2,4,6]: #iterate over 8 bytes and write one byte at a time with delimiter
                        num = int(dat[2][6+2*j:6+2*(j+1)],16)*256 + int(dat[2][4+2*j:4+2*(j+1)],16)
                        #print int(dat[2][6:8],16)
                        #print num
                        file.write(str(num)) #convert hex data to decimal and write
                        #file.write(dat[2][4+2*j:4+2*(j+1)]) #write as hex data
                        file.write(',')
                    file.write('\n')
                    file.close()

        i = i+1
        if i == len(lines):
            break
