import csv

print('Thanks for using this applet!\n~Ninad')
print('This applet will read through the data from the MSAT Gateway \nand create a separate file with current values with the name "ParsedFile.csv" \nand give details if any alarms are raised and at what time')
filename=input('enter file name:')
with open(filename) as csvfile:
    header=csv.reader(csvfile, delimiter=',')
    print(header)
    i=0;
    print('file reading done..')
    newFile = open('ParsedFile.csv','a')
    print('file parsing in progress...')
    i=0
    flag=1

    for row in header:
        write_data=row[0]+','+row[20]+','+row[34]+','+row[48]+','+row[62]+','+row[76]+'\n'
      
        if (row[26]!='0' or row[40]!='0' or row[54]!='0' or row[68]!='0' or row[82]!='0') and i!=0 and flag==1:
            print('first error detected. Details as follows:')
            print('alarm codes',row[26],row[40],row[54],row[68],row[82],'for the time and date',row[0])
            flag=-1
        elif i!=0 and flag==1:
            print('no alarm raised in this file!')
            flag=-1
            
        newFile.write(write_data)
        i=i+1

print('total number of data items found in file:',i)
newFile.close()
print('done....')
input('press any key to exit')
