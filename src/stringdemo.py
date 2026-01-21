#Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")
print('Hello')

#You can use three double quotes or single quotes for multilines string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


print(a)


#slicing 

#you can return a range of character of string by using slice string

b = "Hello, World!"  
print(b[2:5])  #Get the characters from position 2 to position 5 (not included):

print(b[:5])  #Get the characters from the start to position 5 (not included):


#Slice To the End

print(b[2:])  #Get the characters from position 2, and all the way to the end:

print(b[-5:-2])


#modify string
a="teSt "

print(a.upper())

print(a.lower())

print(a.strip())  #remove white space

