f=open('filetest1.txt', 'a')
f.write('\nkichu shekh re khankir pola eta notun line.')
f.close()
# This code appends a new line to the existing file filetest1.txt
f= open('filetest1.txt', 'r')
text=f.read()
print(text)
#read n readline in file handling , reading each line in python 
#line = f.readline()
#this reads the lines of the file one by one 
 #seek and tell in file handling 
 #seek function is used to change the cursor position in the file from the current to the desired position
#f.seek(0)  , Move the cursor to the beginning of the file
#f.seek(5)  , Move the cursor to the 5th position in the file
#read(4) , Read the next 4 characters from the current cursor position
#tell function is used to find the current position of the cursor in the file
f=open('filetest1.txt', 'r')
print(f.tell())  # Prints the current position of the cursor
f.seek(0)  # Move the cursor to the beginning of the file
print(f.tell())  # Prints the current position of the cursor again
f.close()

