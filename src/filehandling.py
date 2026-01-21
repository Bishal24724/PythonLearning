

import os


f=open("demo.txt")
print(f.read())

#if you have on specific directory then you can use on
a=open("D:\\Test.txt")
print(a.read())

#Using the with keyword:

with open("demo.txt","r") as f:
    print(f.read())
    f.close()

    #to read only one then use f.readline()
    print(a.readline())

   # Create a New File
#To create a new file in Python, use the open() method, with one of the following parameters:

#"r" - Create - will read a file, returns an error if the file exists

#"a" - Append - will create a file if the specified file does not exists

#"w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "x")
f.write("Woops!")


#to delete file we need to import os package


os.remove("demo.txt")


#check whether exist or not

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
