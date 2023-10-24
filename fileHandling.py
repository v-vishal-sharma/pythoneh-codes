#!/bin/python3

months = open('months.txt')

print(months) #gives info about the file
print(months.mode) #prints the mode of file, i.e, r, w, rw ...

#READING A FILE

print(months.readable()) #returns a bool statement
print(months.writable())
print('\n')
print(months.read()) #reads the whole file as it is
months.seek(0)
print('\n')
print(months.readline()) #reads just one line, consecutively writing this line will move the pointer to next line
months.seek(0)
print('\n')
print(months.readlines()) #reads whole file and returns everyline as a list item

months.seek(0) #resets the pointer to the starting position of file.
#adding two months.readlines() will return two lists, one is with data and other is empty b'coz our pointer has already read through the file and now it does not have anything left to read.

for month in months:
	print(month.strip())#strip is for removing new line or any leading or trailing white spaces.


#WRITING A FILE

#writing a file name with w or a mode will create the file if not already created

f = open('days.txt','a') # a is append mode and will append to the file, w mode is write mode and will overwrite the file
f.write('Monday')
f.write('\nTuesday')


months.close()
