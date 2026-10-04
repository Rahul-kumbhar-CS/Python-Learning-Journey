#WAP to demonstrate string operations
a="Hello"
b="World"
c=a+" "+b   #concatenation of string
print(c)
print(len(a), len(b), len(c))                          # length of string
str="This is rahul kumbhar \nI am Learning python"     #\n is used for new line
print(str)
print(str[8],str[9],str[10],str[11],str[12])    # indexing of string
print(str[0:13])       # slicing of string
print(str[0:13:2])     # slicing of string with step

#String functions
print(str.endswith("on"))           # check if string ends with specified substring
print(str.capitalize())             # capitalize first character of string
print(str.find('rahul'))               # find index of specified substring
print(str.replace("rahul","RAHUL"))    # replace specified substring with another
s=str.upper()              # convert string to uppercase
print(s)       
print(s.count("I"))        # count number of occurrences of specified substring
