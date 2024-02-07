# --------------------- DATETIME ----------------
# In python the datetime module provides the classes for working with dates and time 
# the primary classes in this module is date, time, datetime, timezone, timedelta

# Date class
from datetime import date
today = date.today()                   # get today's date in format i.e yyyy-mm-dd
print(today)
print("------------------")
# Time class
from datetime import time
now_time = time(3,6)                # returns time in hh:mm:ss.ms
print(now_time)
print("------------------")

# DateTime Class
from datetime import datetime
current_datetime = datetime.now()     # gets current date & time
print(current_datetime)
print("------------------")

# timezone class
from datetime import timezone
current_timezone = datetime.now (timezone.utc)
print(current_timezone)
print("------------------")

# ------------------- MATH --------------------------
# This module provides mathematical funcrtions that cover a wide range of mathematical operations

# sqrt function that returns the square root of a number
import math
square_root = math.sqrt(169)
print(square_root)
print("------------------")

# we can also find the square of a number using the math module by using the power function
square= math.pow(21,2)
print(square)
print("------------------")

# we can also find the power of any number
power_num = math.pow(11,3)
print(power_num)
print("------------------")
# There are several other functions too. Like finding log of number, converting from degree to radian and vice-versa

#Ceil function
# If there is a decimal value then the ceil function then the number greater from the decimal value will be displayed 
# for example if the number is 3.4 and we are using the ceil function then the number --> 4 will be displayed
ceil_num = math.ceil(3.1) # It will print 4
print(ceil_num)
print("------------------")

# Floor function
# If the number is decimal then by using this function the number smaller than the decimal will be printed
# for example if the number is 18.9 then by using the floor function the number 18 will be printed 
floor_num = math.floor(18.9)
print(floor_num)
print("------------------")

# Python JSON
# json is the syntax for storing and exchanging data. It is the text, written with javascript object notation
# to work with JSON data python has built-in package called json
# To convert json to python there is method called json.loads

# Example 

# import json
# x = '{"name":"John","age":"25":"city":"Chicago"}'
# y=json.load(x)ffff
# print(y["age"])
# print("------------------")

# we can also convert python to json
import json
x={
    "name": "John",
    "age" : 25,
    "city":"Chicago"
}
y= json.dumps(x)
print(y)
print("------------------")

# we can convert any of the following data types into json strings
# dict , list , tuple , str , int , float, true, false, none
# the following python objects when converted to json they are stored as:
# dict = object, list = array, tuple =array, str = string, int = number
# float = number, true =true, false = false, none = null


# -------------------- RegEx ------------------------------
# a regex or regular expression is a sequence of character that forms a search pattern
# It can be used to check if a string contains the specified search pattern
# python has the built-in package called re, which can be used to work with Regular Expressions
# There are several metacharacters with special meaning that are used in regular expression
# '.' character matches any single character except a newline
#'[]' matches any single character within the brackets
# '^' caret symbol matches the beginning of the string
# '$' dollar - matches the end  of the string
import re
text= "An apple a day keeps the doctor away"
pattern="doctor"
x = re.search(pattern,text)
print(x)
# There's also findall() function that returns  a list containing all matches
print("------------------")

 # ------------------------- PIP ---------------------
 # pip is a package manager for Python and it's used to install packages from the Python Package Index (PyPI).
 # It is a package thhat contains all files you need for a module
 
 
 # --------------------- Try and Except --------------------
 # the try block lets you test a block of code for errors
 # The except block allows you to handle error
 # the else block lets you excecute code when there is no error
 # the finally block lets you execute the code, regardless of the result of the try and except blocks2
 # we use try and except so that program keeps on running
 # the meaning of this is that if we do not use try and except then the code after the error block will not be executed
 # but what if we need to execute it compulsorily
 # hence we use try and except
 
try:
    print(eed)  # here eed is not defined but we have given it in try block and asked python to return an exception if it is not defined
except Exception as e:  # we have used exception as e because if the error is catched by python then we will print it 
    print(e)   
  
print("---------------------")  
# Example 2:

try:
    num_1= int(input("Enter a random number: "))
    num_2 = int(input("Enter another random number : "))
    result = num_1/num_2
except ValueError: # value error is used if the input is invalid or null
    print("Invalid Input. Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result of the division of the two numbers is,",result)
finally:
    print("This block always executes")
print("---------------------")  
    
# we can do this in class and function too 
# to throw an exception there is a raise keyword that raises exception if error is occured

# ------------------ File handling ----------------------
# file handling is an important function of web application
# python has several functions for creating, reading, writing and deleting files
# the key function to work with files is open() function
# it takes two parameters------> filename, and mode
# the mode consists of r --> read, w --> write, a --> append, x -->create
# t --> text file, b --> binary file
# now we will see the syntax to handle files


# --------- Reading a File ------
f= open('textfile.txt', 'r') # opening the file in read mode. Even if we do not define r as parameter, it's completely fine as it is a default value
text=f.read() # this method is used to read the file 
f.close() # It is always a good habit of closing the file once we are done with it
print(text)


print("---------------------")  

x = open('textfile.txt', 'r')
print("This is an example of reading an line of the file ⬇️\n\n",x.readline())



print("---------------------")  

# here we have opened the file in the same directory i.e python practice
# but we can also work on files in the system outside the folder by giving the location 
#          ⬇️ here if i am working on the file outside the current directory then in the beginning I have to mention double slash
g =open('C:\\Users\kevad\OneDrive\Desktop\Further studies cost.txt','r')
text=g.read() # this method is used to read the file
# we can also read single line
# print(g.readline())
g.close() 
print(text)
 
# --------- Writitng a File ----------
# keep in mind that if we write in a file that is already present, then its content will be overwritten
# so if we have to write in the file that is already present then we have to use append method
# Now to illustrate how to write in a file we will make a new text file
f=open('textfile2.txt','w') # here we have to define w 
f.write("Hey ! this is file handling and this is the write method \nThis text is written by python code using the file writing method")
f.close()

# ------- Appending the file --------
h =  open('textfile2.txt','a')  # Here we have to define a so that interpreter comes to know that we are appending in a file
h.write("\n\nThis is the text that is appended through append method")
h.close()

# ------------ Creating a file 
try:
    j = open('myfile.txt','x') # Here we have to define x so that, we can create a new file
# but if the file is present having the same name then it will return an error
except Exception as e:
    print(e)
# Here i have used try and except as it will return error once the file is created. And so to execute the code below this block I have to use exception handling
print("---------------------")  

# ---- Readline method for reading line by line -------- 
try:
    s= open('myfile.txt','r')
    i=0
    while True:
        i+=1
        line=s.readline()
        if not line:
            break
        m1=line.split(",")[0]
        m2=line.split(",")[1]
        m3=line.split(",")[2]
        print(f"Marks of student {i} in  English is : {m1}")
        print(f"Marks of student {i} in  English is : {m2}")
        print(f"Marks of student {i}in English is : {m3}")
        print("")
except Exception as e:
    print(e)

print("---------------------")  

# writelines() method for file handling
try:
    k=open('myfile.txt','a')
    lines=["\nlst_obj1\n","lst_obj2\n","lst_obj3\n"]
    k.writelines(lines)
    k.close()
except Exception as e:
    print(e)
    