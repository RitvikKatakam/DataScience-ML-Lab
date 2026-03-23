"""In Python, File I/O (Input/Output) means reading data from a file and writing data to a file.
inbuild functions to work with file
open(), read(), write(), and close()
syntax=:
file = open("filename","mode")
common file modes
 r= read a file
 w= write a new file or update the existing file
 a= append data to file
 x= create a new file
 b= binary mode
 d= text mode(default mode)"""
#v1. Reading from a File
file= open("data.txt","r")
content = file.read()
print(content)
file.close()

# 2.Writing into the file
file= open("data.txt","w")
file.write('hello , This is python file i/o write example')
file.close()

# 3.Appending data to file
file= open("data.txt","a")
file.write('\nThis is an appended line.')
file.close()

# 4.Using with statement (This automatically closes the file when the scope of the code is over)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)