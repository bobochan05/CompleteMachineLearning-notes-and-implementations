#how to read wirte and append to a file in python
#the modes are 'r' for reading, 'w' for writing (overwriting), 'a' for appending
#open a file for reading
#f = open('file name', 'mode')
f= open('python1.py', 'r')
text=f.read()
print(text)
#open a file for writing
#f = open('python1.py', 'w')
#f.write('print("Hello World")')
#f.close()
#open a file for appending
f = open('python1.py', 'a')
f.write('\nprint("my bitchass is writing a file")')
f.close()
# This code appends a new line to the existing file python1.py
f= open('python1.py', 'r')
text=f.read()
print(text)







