# defining variables in python
a="variable" # string variable 
print(a)
b=2          # int variable 
print(b)
c=3.0        # float variable
print(c)
# In python, there is no need to define the type of the variable. Python itself assign the type to variables


# To know the type of the variable type function can be used

print(type(a))    # It will return str
print(type(b))    # It will return int 
print(type(c))    # It will return float



# ------------------------------------T Y P E   C A S T I N G ----------------------------

# --------------- in case there is need to define the type ("TYPE CASTING") can be used

integer_1=int(4.0) 
print(integer_1)  # It will return float 4.0 as int 4
print(type(integer_1)) 
integer_2 = str(integer_1) 
print(integer_2)
print(type(integer_2)) # It will return str
integer_3 = float(integer_2)
print(integer_3)  # It will return float
print(type(integer_3)) 
print()


#-------   S T R I N G   C O N C A T E N A T I O N ---------------
# TO join 2 strings + operator is used

animal1 = "Lion "
animal2="Tiger"
animal3="Giraffe"
animals_in_zoo =(animal1 + animal2+" "+animal3)
print(animals_in_zoo)
print()

#-----------------  S T R I N G   F O R M A T T I N G -------------------

# It is not possible to concate a string and a number
# for example there is variable called age containing number and a variable called name 
# If we try to concate these both variables, there will be an error 
# So to make it possible, we use format

room_number = 2005
name = "Parth"
greeting = "Hello {} your room number is {}"
print(greeting.format(name,room_number))

# In string formatting if there is the use of multiple variables, in format there can be multiple arguements
print()



# ------------------------------- L I S T S --------------------------------------


# Lists are ordered and changable data types having [] square brackets 
# Lists also allow duplicate elements   
# elements in the lists are manipulated using the index numbers

animals = ["Dog","Cat","Cow","Buffalo"]
print(animals)
print(animals[::2])

# we can use looping in the lists and can find the length of the list 
# In the list there can be multiple data types such as string, int and float

for animal in animals:
    print(animal)
print(len(animals))

# to make list we can use list constructor

thislist = list(("Preet","Ankit","Siddh","Harsh"))
print(thislist[:2])
print(thislist[-3:-1])

# Elements can be added in the list 
# 1st method we will see is from the index
# We can add single as well as multiple elements using this method

thislist[1]="Ruhani"
print(thislist)

thislist[1:4]=["Sonam","Pratik","Nishant"]
print(thislist)

# ---- INBUILT LIST Manipulation Methods  ---------------------\
    
     # ----------- ADDING ELEMENTS IN LIST -----------   
# 1 -- INSERT method
# in insert method there is need to specify the index of the element you need to insert
thislist.insert(3,"Dhruvin")
print(thislist)

# 2 -- APPEND() method
# This method is used to add the element in the end of the list

thislist.append("Mayank")
print(thislist)

# 3 -- EXTEND() method  
# This method is used to add two iterable objects 
# It is not important that a object should be only list.. It can be tuple, set and dictionary


# Adding tuple to list
friends=("John","Hardik") # Here although the object is tuple, the extend method still add to the list 
thislist.extend(friends)
print(thislist)

# Adding set to list 
newFriends={"Jenil","Alia"} # Here the set data type can be also added to the list
thislist.extend(newFriends)
print(thislist)

     # Removing items from the list
    
# 1-- REMOVE() method 
# to remove the specific item from the list, this method is used 
# you need to specify the element

thislist.remove("Hardik")
print(thislist)

# 2 -- POP () method
# This method is used when there is need to remove the item using it's index number
# If the index number is not specified it will automatically remove the last item 
thislist.pop(2)  # this will remove Pratik from the list 
print(thislist)

thislist.pop()
print(thislist)

# 3 -- CLEAR() method
# this method completely makes the list empty

thislist.clear()
print(thislist)

# 4 -- DEL() method
# This method is used to delete the list completely

del thislist
# print(thislist)

#----------------------- L I S T  comprehension -----------
# We can loop through the list 

fruits = ["apple", "orange", "cherry", "banana","kiwi"]
newFruits = []
for x in fruits:
     if "a" in x:
          newFruits.append(x)
print(newFruits)

newFruits=[x for x in fruits if x!="apple"]
print(newFruits)

newFruits = ["hello" for  x in fruits]  # It will print hello each time for each fruit  instead of fruit
print(newFruits)

# S O R T I N G  LIST 
fruits.sort() # This will sort the list in alphabetic order
print(fruits)

# To return the list in reverse or descending order 
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)

# We can also copy the list 
impfruit = fruits.copy()
print(impfruit)
 
nwimpfruit = list(fruits)
print(nwimpfruit)

print()
#----------------------------------  T U P L E S ---------------------------------

# Tuples are collection of the ordered data
# They are immutable, that means the elements cannot be modified
# It also allows duplicate elements similar to lists
thisTuple = ("apple", "orange", "banana", "orange", "apple")
print(thisTuple)

# To know the length of the tuple we can use the len() function
print(len(thisTuple))

# Tuple allows multi data type 
tuple2 = ("boy",12,22.0,False,"Optus")
print(tuple2)

# we can also access the tuple items using the index number
print(tuple2[2])

# we can maipulate the elements in tuple by converting it to a list and then doing the normal list methods
# Similar to lists we can also loop through the elements

print()
#----------------------------------  S E T S  -----------------------------------------


# It is a data type that is used to store the unordered and unchangable elements
# it uses {} curly braces
# In sets duplicates are not allowed

thisSet = {"apple","mango","strawberry","watermelon","kiwi"}
print(thisSet)

# there can be looping in the set
for i in thisSet:
     print(thisSet)
     
# -------------------- SET METHODS --------------------------------
# 1 ADD 
     
# we can add the elements in the set
thisSet.add("orange")
print(thisSet)

# 2 UPDATE
# to add two sets we can use update method
newSet={"coconut","litchi"}
thisSet.update(newSet)
print(thisSet)

# 3 REMOVE
thisSet.remove("coconut")
print(thisSet)

#4 DISCARD
thisSet.discard("litchi")
print(thisSet)
 
#5 CLEAR
thisSet.clear
print(thisSet)
print()

# ------------------------------------- D I C T I O N A R Y ---------------------------------------------------------------

# Dictionaries are used to store the data in key:value pairs
# The elements in the dictionary are ordered, changable and do not allow duplicates

thisdict = {"company":"Audi",
            "model":"R8",
            "engine":"V 10",
            "fuelType":"Petrol"
            }
print(thisdict)

# ony single key can be printed in the dictionary by just defining the key name in the print statement
# for that you need to mention it in the square brackets []
# for example to print the model of the car, we can mention the key - model 

print(thisdict["model"])

# It can store any data type, but given that it is in key:value pair
dict2= {
     "name":["Rohan","smit","om","harsh"],
     "age":22,
     "college":"SOU"
}
print(dict2)

# we can print the value of the key by storing it in the variable 
x = thisdict["model"] # This only prints the value of the key
print(x)

# we can do the same using the inbuilt method called get
# ------   GET ()  ---------------------

y= thisdict.get("model")
print(y)

# to get all the keys of the dictionary there is a method called key

# -------------- KEYS () ---------------
y =  thisdict.keys()
print(y)

#---------------- Values ()-----------------
y= thisdict.values() # this method prints all the values of the dictionary 
print(y)

# We can change the value of the key in dictionary
thisdict["model"]="A8 L"  # It changes the model of the car from R8 to A8L
print(thisdict)

#--------------- ITEMS () ----------
# this method prints the key and value of dictionary, stored in tuple 
y= thisdict.items()    # It stores the key:value pair inside tuple, which are stored inside the list 
print(y)

#   -------------  UPDATE()  --------------
# This method updates the dictionary within the given arguement

thisdict.update({"fuelType":"Diesel"})     # This updates the the  --> fuelType from petrol to diesel
print(thisdict)


# To remove the items from dictionary there are several methods
# --------------   POP()  ----------------
# It removes the items of the specified name

thisdict.pop("fuelType")    # This will remove the key -> fuelType from the dictionary
print(thisdict)

#  --------------  POPITEM () ----------------
# This removes the last item entered in the dictionary
thisdict.popitem()
print(thisdict)

#------------- del KEYWORD   ---------
# the del keyword is used to remove the specified item
del dict2["college"]
print(dict2)

# when we do not specify the key while using the del keyword, it will the delete the entire dictionary

del dict2         # It entirely deletes the dictionary
# print(dict2)   # this will give an error because the del keyword has dleted the entire dictionary

# the another method to completely delete the dictionary is clear method
# -------- clear()  -----------------
# unlike the del keyword the clear() method will return empty dictionary when we print it 
thisdict.clear()
print(thisdict) 


# We can also copy the dictionary using the copy() method
# -------- COPY() ----------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
mydict = thisdict.copy()
print(mydict)

#------------- Nested dictionary --------------------------------
# There can be dictionary inside a dictionary and so on....
# For example

myFamily ={
     "Father":{
          "name":"George",
          "Age":"51"
     },
     "Mother":{
           "name":"Julia",
           "Age":"49"
     },
     "Son":{
           "name":"John",
           "Age":"21"
     }
}

print(myFamily)

print()

Father = {
          "name":"Daniel",
          "Age":"49"
}
Mother = {
          "name":"Anna",
          "Age":"48"
}
Son={
          "name":"Dwayne",
          "Age":"19"
}
Daughter = {
          "name":"Julie",
          "Age":"15"
}

myFamily2= {
     "father":Father,
     "mother":Mother,
     "son":Son,
     "daughter":Daughter
}

print(myFamily2)

print()
# ----------------------------  CONDITIONS (  IF ELSE ......) ----------------------------
# conditions if and else are used to check certain conditions, and returns the output as true or false...
# These conditions can also be used for looping

# ----- 1 IF  statement--------------

a = 105
b = 101
if a > b:
     print(f"a ({a}) is greater than b ({b})")
print()    
# ---------- 2  ELIF statement--------------
#   It is the way to check the next condition if the previous condition is false

a = 105
b = 106
if a > b:
     print(f"a ({a}) is greater than b ({b})")   #it checks the condition if a is greater   
elif a < b:
     print(f"a ({a}) is less than b ({b})") # If the previous condition is false the interpreter checks the next condition
print()   
# ------------ ELSE --------------
# if none of the condition is true then the interpreter performs the action written in the else block of code

a = 105
b=105
if a > b:
     print(f"a ({a}) is greater than b ({b})")   #it checks the condition if a is greater   
elif a < b:
     print(f"a ({a}) is less than b ({b})") # If the previous condition is false the interpreter checks the next condition
else:
     print(f"a ({a}) is equal to  b ({b})")  # If none of the condition is true then, action in the else block is performed   
print()
     
     
# ------------ SHORT HAND STATEMENT ----------------
# the statements can be written in short forms
# there are several ways to write short hand statements

a=100
b=85
if a > b : print("A")

a=20
b=22
print("A") if a > b else print("B")
print()

#  we can also combine the if else conditions using the logical operators such as AND / OR / NOT

# -------- A N D
# This operator returns true if all the conditions are true

x=550
y=645
z=556

if x>y & x>z :   # instead of the symbol we can also use the (and) keyword as used in the below elif expression
     print(f"x ({x}) is greater than y and z")
elif y>z and y>x:
     print(f"y ({y}) is greater than x and z")
else:
     print(f"z ({z}) is greater than x and y")

print()
# ---------- O R 
# This returns true if one of the given condition is true

a=55
b=12
c=64

if a>b or a>c:
     print ("One the statement is true")

print()



# -------------------------------- L O O P S ------------------------------
# 1 ---- While loop executes the statement until the condition is true
#   once the condition becomes false it stops execution

i = 1
while i <= 6:
     print (i)
     i+=1
print()
# ------ BREAK --------------
# it is the statement that stops the execution of the loop even if the condition is true

a = 1 
while a < 7:
     print(a)
     if a == 3 :
          break
     a+=1
print()
# ----------- CONTINUE ----------------
# it is used stop the current iteration and continue with the next iteration

a =1 
while a < 7:
     a+=1
     if a == 3:
          continue
     print(a)
     # a += 1
print()
# We can also use ELSE statement along with while loop

i= 1
while i < 6:
     print(i)
     i+=1
else:
     print("\ni is no longer less than 6")

print()
     
# ---------------------------- F O R  LOOPS  ---------------------------------

# For loops are used to iterate over the sequence ( list, tuple, set or string)
fruits = ["orange","apple","watermelon","banana","mango"]
for x in fruits:
# We can also use break and continue statement in the for loops
     if x=="mango":
          break
     print(x)

print()

fruits = ["orange","apple","watermelon","banana",]
for x in fruits:
     if x == "apple":
          continue
     print(x)

print()
# we can also loop through strings

name = "Rohan"
for x in name:
     print(x)
print()


#  We can also use the --- RANGE --- function 
for i in range(6):  # it prints the number from 0 until the defined number in range but less than 1 
     print(i)       # for example here it'll print the number from 0 until 5, because it is one less than 6
print()

# although the starting point of the range function is 0, but we can specify the number from where to start off
# example ⬇️

for i in range(2,8):
     print(i) # in this statement the numbers will print from 2 until 7
print()

# we can also specify the steps between the numbers, in the sense that how much numbers to skip in between two numbers

for i in range(1,8,2):  # in this statement the numbers will print from 1 to 7, but it will skip two numbers as we've mentioned the step as 2
     print(i)  # it will print numbers such as 1 3 5 7 
print()

# We can have nested loops ⬇️ here is the example of it
fruits=["apple","banana","strawberry","grapes"]
color=["red","yellow","pink","violet"]

for x in fruits:
     for y in color:
          print(x,y) # in this example one element of the outer loop i.e --> fruits will be printed until all the elements of inner loop i.e --> color is printed

print()        # for example --> apple will be printed against all the elements of the color are printed
          
          
          
#  -------------- PASS ------------
# for loops cannot be empty, because it may cause an error. So to avoid the error there is the use of the pass statement

for x in [0,1,2,3]:
    pass  # here in for loop there need a follow up condition either if...else or print statement, otherwise it'll give error
# but using the pass statement it will not show the error instead it will move ahead



# ---------------------------------------------- F U N C T I O N S ------------------------------------------


# A function is a block of code that runs/executes only when it is called
# to write a function in python it is required to mention def keyword 

def my_func():
     print(" This is a function") # it will not print the output as we have not called the function 

# To call the function we need to use the mention the function name outside the block of function

def my_func():
     print("This is an example of a function")
     
my_func()  # now here we have called the function hence it will print the output 
print()
# --------------------- Arguments -----
# information can be passed inside the function in the form of arguments 
# They are passed after the function.. inside the paranthesis
# we can pass as many as argument as we want, but they need to be seperated 

def my_employee(employee_name):
     print("------->  "+employee_name+" SoftEdge Infotech")
my_employee("Harshal")
my_employee("Ayush")
my_employee("Rohan")
my_employee("Navin")
print()

# There is the need to mention the number of arguments that we have described in the function, if we fail to mention any of the argument then it will return error
# for example ⬇️
def emp_detail( name,  age):
     print("------->  Name: "+name+" Age: "+age)
emp_detail("Harshal","22")
emp_detail("Rohan","21")
emp_detail("Ayush","20")
#emp_detail("Kunal")  # I have commented this line for further execution, because it gives error 
#This will return error because we have defined function for 2 arguments, but here we are passing only one argument
print()

# ------------------------ ARBITRARY ARGUMENT ------------------------
# If the number of arguments are unknown, then arbitrary arguments are used.They are represented by star(*args) 
def student_name(*args):
     print(" -----  The name of the youngest student is:  "+args[2]) # In this function with arbitrary argument, to print the output, it needs to specify which element to access
student_name("Takshil","Riken","Aryan","Rahul")  # It will only print one of the elements because it will be unable to print the whole tuple, and it will give error 
     
#------------------------ Arbitrary keyword arguments ------------
# It is also used when the number of arguments are unknown but here we use (**args)
# It receives the dictionary of keyword arguments in the function 
def full_name (**name):
      print(" The last name/Surname  of the person is:"+ name["lname"])

full_name(fname="Ritika",lname="Sharma")
full_name(fname="Anushka",lname="Kohli")
full_name(lname="Dhoni")
print()
# Default value argument 
# In this type of function parameter we can set the default value, in case if we return the function without the parameter, it will show it's default value

def my_func(country="India"):
     print("I am from :"+country)
my_func("United States")
my_func("United Kingdom")
my_func("Russia")
my_func() # Here although we have not passed the parameter when the function requires, it will not show error because we have defined the default value
print()

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# Let's try with the list 
def students(student):
     for x in student:
          print(x)

stud =["Harshal","Anjali","Rahul","Tina","Mohit"]
students(stud)

print()

# ------------------------- RETURN -----------------
# to return a value for a function we need to use the "return"--> keyword
# A return keyword is used to use the specific part of the function such as calculation in different part of the program. If needed it can be used outside the function
# Here are some examples of functions with a return keyword

def func_add(a,b):
     result = a+b
     print("The result of the above calculation is ",result)
     return result
func_add(5,7)
print()

# This is the next example of the function with return value having the square of the number 
def func_square(number):
     squareNum = number**2
     print("The square of the", number ," number is :",squareNum)
     return squareNum
func_square(5)
func_square(152)
func_square(221)
func_square(19)

print()

# ----------------------- RECURSIVE FUNCTIONS --------------------
#A recursive function in Python is a function that calls itself during its execution.
# It's like a function that asks for its own help to solve a problem. 
# Recursive functions are often used to solve problems that can be broken down into smaller, similar sub-problems.


# --- Example -1 : Factorial function
def factorial(number):
     if number == 0 or number == 1:
          return 1
     else:
          return number * factorial(number-1)
     
result = factorial(5)
print("The factorial is: ",result)
print()


# Example - 2 : Countdown function
def countdown(n):
     if n == 0 :
          print("You are at zero point.... :(")
     else:
          print(n)
          countdown(n-1)
          
countdown(11)
print()
     
# Fibonacci series using Recursive function
def fibonacci_series(n, a=0, b=1):
    if n > 0:
        print(a, end=' ')
        fibonacci_series(n - 1, b, a + b)

# Example: Print the first 10 terms of the Fibonacci series
fibonacci_series(10)
print()

print("-------------------")
# ------------------------------ LAMBDA FUNCTION 


# Lambda function is a type of function that is used when there is less complexity in the code
# It is used when there is no need to have if else statement and loops in a function 
# For example when there is need have a square of a number so in that case if we define a function then the complexity of the code increases
# so we use lambda function which is anonymous ---> meaning having no name
#When we need to use lambda function we have to use lambda keyword 
# It can have multiple arguments but can consist only single expression

# SYNTAX --->  lambda argument : expression

# Example: we need to print the square of a number

squared_num=(lambda a : a**2)
number = 5
print(f"{squared_num(number)}")

print("-------------------")

# If we want to print the 3 multiple of a number

triplet =  lambda a : a*3
number = 822426
print(f"The 3 times of {number} is {triplet(number)}")
print("-------------------")

# The lambda function also acccounts for 3 other sub-functions they are  :  map(), sort() and filter()

# Finding the greater number through lambda
max_of_two = lambda a, b: a if a > b else b

result = max_of_two(10, 7)
print("The maximum of 10 and 7 is:", result)
print("-------------------")

# checking if the number is positive or negative
is_positive = lambda x: x > 0

result = is_positive(5)
print("Is 5 positive?", result)
print("-------------------")


# Reversing the string
reversed_string = lambda a:a[::-1]
result =  reversed_string("ROHAN")
print("The reverse string is :",result)

print("-------------------")

#Generating the power function 
# In this we will have a power of number with another number

power_func = lambda m,n : m**n
result = power_func(5,3)
print("The power of 3 on 5 is :", result)
print()
print("-------------------")



#------------------------------------------
#------------------------------------------
#------------------------------------------
#------------------------------------------
#   ----------------------------------------- OBJECT - ORIENTED --------------------------------------------

##  ------- ---------------------  1 CLASSES AND OBJECT  -----------------------
# Classes are like blueprint or object constructors or a template to create objects
# Classes can contain variables that is called property of a class and functions that is called method of a class

# Object are instances of a class that has the access to the properties of the class
# self represents the instance of the class, by which we can access the properties of the class

# Example of a simple class
# Let us create a class of person having values such as name and occupation
# To define class it is required to mention class keyword

class Person:
     name= "Rohan"
     occupation="Student"
     
a = Person()            # We have created an object that refers to class person
print(a.name) # This     # This will print name mentioned inside the class ----> Rohan
# If we do not want to print the same name from the class we can change it
print()
b = Person() 
b.name="Riddham"
print(b.name) # This # This will print name mentioned in the object ----> Riddham
print()

# Now we will create an instance of a class by using self method

# Let us consider the above listed class Person
 
class Person_new:
     name = "Omkar"
     age=25
     networth = "$ 10 million"
     # self if the reference to the current instance of the class and it is used to access the parameters of the class
     def info(self):           # By using the self instance we can manipulate the values of the class
          print(f"{self.name} is {self.age} years old and has networth {self.networth}")    
ambani = Person_new()

ambani.info()
print()
#  EXAMPLE-2
# Let's consider a company that has to enter the details of the employees


# ---------------------------------------> I have commented this example because it takes user input and to run the code below it requires  to enter 
#                                          the details of the employees of this class


# class Employee:                       # here we've defined a class named employee that will keep track of the employee information
#      def emp_info(self):                # A class cannot be empty so we have created a method to insert the employee information. The method is a function here
#           self.name=input("Enter employee name ")
#           self.salary=float(input("Enter employee salary "))
#           self.id=int(input("Enter employee id "))
#      def display(self):                      # This method is defined to display the output of the details of employee
#           print(f"-->  The name of the employee is: {self.name}")
#           print(f"-->  The id of {self.name} is: {self.id}")
#           print(f"-->  The salary of {self.name} is: {self.salary}")
# # now here we will create an object that will have access of the properties of class
# a=Employee()
# a.emp_info()
# a.display()
# print()
# b=Employee()
# b.emp_info()
# b.display()

# print()

# __init__ method also known as  --->  "CONSTRUCTOR"
# It is the method of the class that is called when an object is created
# It initializes the attributes of class

# Let us consider a class that keeps track of the students details
class Student_detail:
     def __init__(self,stud_name,stud_rollno,stud_result):
          self.name = stud_name
          self.rollno = stud_rollno  
          self.result =stud_result
     def display(self):
          print(f"--> The name of the student is: {self.name}")
          print(f"--> The Roll no. of {self.name} is: {self.rollno}")
          print(f"--> The result of {self.name} is: {self.result}")
rohan = Student_detail("Rohan",7,"PASS")
rohan.display()
          
          

#   ----------------------------------------- 2 - INHERITANCE --------------------------------------------
# It is the method of object oriented programming that allows to us to inherit or to borrow properties and methods from parent class to child class
# Here parent class is also known as super class or base class
# And the child class is often called as sub class or derived class
# Let's understand better with an example

class Mother:
     def __init__(self,skin_tone,eye_color,hair_color,allergies):
          self.skin_tone = skin_tone
          self.eye_color = eye_color
          self.hair_color =hair_color
          self.allergies = allergies
     def display(self):
          print(self.skin_tone)
          print(self.eye_color)
          print(self.hair_color)
          print(self.allergies)

# Here we have defined a class called mother that is a parent class and we have displayed the qualities of mother 
# Now we will inherit some properties of parent class in child class
print()
class Daughter(Mother):               #Here to define that daughter is inheriting from mother class we have to write the parent class inside bracket after child class
     def __init__(self,skin_tone,eye_color,hair_color,allergies,height, weight): # Here we have defined some qualities as mentioned in parent class and added 2 properties i.e height and weight
          super().__init__(skin_tone,eye_color,hair_color,allergies)
          self.height = height
          self.weight = weight
     def display(self):
          super().display()
          print(self.height)
          print(self.weight)

suzzane=Daughter("fair","brown","blonde","no allergy",5.6,66)
suzzane.display()
# print(type(suzzane.eye_color))
print("----------------------------------")

# ----------------------------    ITERATORS   ----------------
# Iterators are objects that are used to iterate over an iterable object 
# It contains method such as iter() and next method 
# iter() method is an method to iterate over an interable object 
# next() method is used to get on the next iterable or element
# Unlike loops iterators are used to iterate over any iterable item such as list, string, file or even a generator
# It is used to solve more complex looping pattern than a for loop. We can also skip some elements, reverse the order and even combine multipe iteraotors
# There is also a methos called StopIteration which stops the iteration operation

# For iteration we can also use for loop, however it also uses built-in iterator methods which we cannot see

# example of iteration

employees = ["Rohan","Kenil","Raj","Vraj"]        # it is called iterable. On which iteration can occur
print(dir(employees))
print()
itr_obj = iter(employees)                         # Here we have used the built-in iteration method using keyword iter, which we have assigned to variable so we can access it
print(dir(itr_obj))
print(type(itr_obj))                              # To cross check it we have used type function and it should return the type as list iterator
# so to print each and every element we have to use next method
print(next(itr_obj))   # It will return rohan 
print(next(itr_obj))   # It will return Kenil
print(next(itr_obj))   # It will return raj
print(next(itr_obj))  # It will return vraj
# If we use one more print statement as above it will raise an exception as it can iterate as much as the elements are

# We can know whether the object is iterator or iterable 
# on checking the dir(object) of the object if we get only __iter__ then it is :  iterable
# And if it is returning __iter__ as well as _next__ then it is :  iterator
# this is also called magic method
print(" --------- Magic method")
# We can also use this magic method for iteration

admins = ["RK","Patel","Iyer","KD"]
iter_obj  = admins.__iter__()

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
 