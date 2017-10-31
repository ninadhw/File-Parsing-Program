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
        date=(row[0])
        cur1=(row[20])
        cur2=(row[34])
        cur3=(row[48])
        cur4=(row[62])
        cur5=(row[76])
      
        if (row[26]!='0' or row[40]!='0' or row[54]!='0' or row[68]!='0' or row[82]!='0') and i!=0 and flag==1:
            print('first error detected. Details as follows:')
            print('alarm codes',row[26],row[40],row[54],row[68],row[82],'for the time and date',row[0])
            flag=-1
        
        newFile.write(date)
        newFile.write(',')
        newFile.write(cur1)
        newFile.write(',')
        newFile.write(cur2)
        newFile.write(',')
        newFile.write(cur3)
        newFile.write(',')
        newFile.write(cur4)
        newFile.write(',')
        newFile.write(cur5)
        newFile.write('\n')
        i=i+1

print('total number of data items found in file:',i)
newFile.close()
print('done....')
input('press any key to exit')
