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



# What is programming paradigm?  ---------------->  It is the way of organizing the program
# Python support multiple paradigms which are as follows :⬇️

# procedural-oriented programming
# Funtional-oriented programming
# Object-oriented programming

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
# In object oriented programming we can solve real=life problems more effeciently than function-oriented programming
# OOP provides the following features ⬇️
# Reusability - (using Inheritance)
# Data Security - (Using Encapsulation)
# Data hiding - (using Abstraction   )

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
# There are 3 types of constructor, they are :
# !. Parameterized constructor : the above example is the type of parameterized constructor where along with self other parameters are also defined
# 2. Non-Parameterized constructor : Where only self is there inside the constructor and no other parameters are present
# 3. Default constructor 


# SELF - It is an variable that has the memory reference of the current object


# Let us consider a class that keeps track of the students details
class Student_detail:
     def __init__(self,stud_name,stud_rollno,stud_result):
          self.name = stud_name # here using self. method we are inserting the variable name inside the memory location      
          self.rollno = stud_rollno   # and we are assigning the value to the variable which will directly come from the object parameter
          self.result =stud_result
     def display(self):
          print(f"--> The name of the student is: {self.name}")
          print(f"--> The Roll no. of {self.name} is: {self.rollno}")
          print(f"--> The result of {self.name} is: {self.result}")
rohan = Student_detail("Rohan",7,"PASS")
rohan.display()

print("--------------------------------------")        
# There are few built-in class functions in python
# They are getattr, setattr, delattr and hasattr
# getattr is a function to get the attribute in the class and the syntax is getattr(object_name, attribute_name)
# setattr is a function to set or change the attribute in the class and its syntax is setattr(object_name, attribute_name, new_value)
# delattr is a function to remove the attribute in the class and its syntax is delattr(object_name, attribute_name)
# hasattr is a function that checks if the attribute is present in the class or not and if it is present it returns TRUE
# Its syntax is hasattr(object_name, attribute_name)

# let's understand these functions with an example

class Employee():
     company_name = "SoftEdge Infotech"   # This is called class variable and it will remain same for all the objects
     # We can access it using the class name.variable name 
     # here we will simply print Employee.company_name
     # If we modify this variable then the value in the objects will also be changed
     def __init__(self, emp_name,salary,age):
          self.name = emp_name
          self.salary = salary
          self.age = age
     def display (self):
          print(f"The name of the employee is {self.name}")
          print(f"The salary of {self.name} is {self.salary}")
          print(f"The age of {self.name} is {self.age}")
          
     # We cannot directly modify the class variables. Hence we use class methods to modify or work on them 
     # For defining class method the process is same as defining the normal method but we simply use a built-in decorator 
     # The purpose of using the decorator is that the interpretor can know that below this line there is class method 
     # We will use @classmethod decorator and also use (cls) for class reference where we were using self for object reference
     # Let's understand it better with an example
     @classmethod
     def get_company_name(cls):  # This is what I have mentioned above that to use the class reference we have to mention the cls variable inside the method just as we were mentioning self method
         # print(cls.company_name)   ----->  We have commented this line because it is printing the company that we have mentioned initially 
         #This is how we can access as well modify the class variable/property using the class method
          cls.company_name = "Google Inc."
          print(cls.company_name)
          # we can change the class variable's details by using this class method 
          # we can also do this in the above line itself but it will get messed up
print("----------- class method")
Employee.get_company_name() # This prints softedge infotech

     
emp1 = Employee("Rohan",87000,25)
emp1.display()      
# Let's print the class variable
print(Employee.company_name) # This will be softedge
print(emp1.company_name)  # This will be softedge
g = getattr(emp1,"salary" )   # This should print the salary 
print(g)   

# There are class methods that are in-built in python which works on class variables 
# For instance variable we use self variable to access properties, the same way we have to do for the class method
# But instead of using self we have to use cls variable 
     

setattr(emp1,"age",24)
# now lets check if the age is changed from 25 to 24 or not ?
# For this we will use __dict__ method to get the detail of the whole object. We can also use  getattr function

print(emp1.__dict__)  # The age is sucessfully changed

delattr(emp1,"age")  # this should delete the age attribute
print(emp1.__dict__) # and it has sucessfully deleted age attribute

# now we will check if the age attribute is present or not using the hasattr method
print(hasattr(emp1,"age")) # it is returning false as expected because there is no age attribute anymore as we deleted it using the delattr function 
print("--------------------")
# Classes also contains built-in attributes
# They are __doc__, __dict__, __name__ and __module__
# the doc variable is used to know the documentation of the class or the purpose of the class
# dict attribute is used to get all the namespaces of the class
# name is used to know the name of the class. Sometimes it is required to use the name of the class and hence this method is used
# module attribute is used to know that from which module the class belong
# sometimes we import the class from different module and to know about the module we use this method

# Let's understand it better with an example
# let's cosider the above employee class
print(Employee.__doc__) 
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__dict__)
print("--------------------")

# We can also check whether the object belongs to a particular class or not 
# By using the isinstance method 
# The syntax of this function is isinstance(object_name,class_name)
# Based on the condition it will return boolean value either True or False
print(isinstance(emp1,Employee)) # in this case it will return True as emp1 belongs to Employee class
print("--------------------")

# Instance variables : They are the variables that are made for the instance or objects 
# It's value may differ from object to object 
# Modification in one variable of the object doesn't affect the values of the other variables for different instances
# In the above example the variables like emp_name and salary were the type of instance variable which stores the different memory address and stores different values for different objects but still it'll have the same variable name


# we can also add the variable outside the class for the object 
# In the above Employee class we haven't mentioned qualification inside the init method , but what if we want to add it in its instance i.e emp1
# We can also change the value of the variable such as name mentioned in the above example 
# by just writing --> emp1.name = "Raj" --> The name of the employee 1 will be changed without affecting the other variables
# we simply do this 
emp1.qualification = "B.Tech"
# Now to check if the above variable is added to the instance or not, we will access the object using the dict method that we have seen earlier
print(emp1.__dict__)
print("--------------------")

# ----------------------------------  Instance Methods --------------------------------
# The getter and setter methods are not the built in methods but are simply the conventions 
# Getter method : get the values of the instance variables
# Setter method : set the values of the instance variables

class Cricket_team:
     def setName(self, nm): # this is called setter method which sets the value for the variable of the instance 
          self.name = nm
     def getName(self):     # This is the getter method which fetches the setted value of the variable of the instance
          print("The name of the team is: ", self.name)    

t1 = Cricket_team()
t2 = Cricket_team()
t1.setName("CSK")    # It is an example of setter method where we are not simply using the init method and setting the variable inside the object directly and passing them as parameter
t2.setName("GT")      # Like we normally use to pass the values above when we call the class when making the object, but here we are setting the name using the setter method
t1.getName()
t2.getName()             # just as the setter method, we are using the getter method to get the value for the instance or object variable 
print("--------------------")


# In total we have 3 types of methods they are :
# 1. Instance Method - The methods that works on instance data
# 2. Class Method    - The methods that works on class data
# 3. Static Method   - The methods that works on external data (Data that doesn't belong to any object)

# static method 
# In this method there is no need to create object as it works on external data but there is need to mention the staticmethod decorator above the method so that interpreter knows that below this line there is static method
# Below is an example of static method that we've used to know the simple interest from the bank
# the interest rate of the bank remains the same/constant so in the formula we need to take it from the class Bank itself
# in the static method called simpleInterest we just have mentioned the amount and years variable and will take interest of bank from class itself

class Bank:
     name = "Kotak Mahindra"
     rate_of_interest = 12.05
     # Now for static method we need to declare the staticMethod decorator
     @staticmethod
     def simpleInterest(principal_amount,number_of_years):
          simple_interest = (principal_amount*number_of_years*Bank.rate_of_interest)/100
          print(f"The simple interest of your amount {principal_amount} for {Bank.name} is {simple_interest}")
Bank.simpleInterest(20000,2)   # As it is static method there is no need to make an object
print("------------------------")         
          


#   ----------------------------------------- 2 - INHERITANCE --------------------------------------------
# It is the method of object oriented programming that allows to us to inherit or to borrow properties and methods from parent class to child class
# Here parent class is also known as super class or base class
# And the child class is often called as sub class or derived class
# Let's understand better with an example

# What is the need of inheritance ?  ( Important interview question
# Answer is that inheritance is for the code-reusability
# When you have relations among other classes

class Employe:
     bonus = 5500
     def display(self):
          print(f"The bonus of the employee is : {Employe.bonus}")
class Manager(Employe): # by this way we have given a parent class inside the child class 
     bonus= 11000
     def show(self):
         print(f"The bonus of the manager is : {Manager.bonus}")
e1=Employe()
m1=Manager()
e1.display()   # this will show the bonus of the method in the parent class
# e1.show()   # this was to illustrate that the child class can access parent class's properties and methods but the vice-verso is not possible 
m1.show()       # Here it is accessing the method mentioned inside the child class
m1.display()     # Child class can also access the methods and properties of parent class 
print("------------------------")         


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


# By using the super() class we can access the properties of the parent class
# It returns an temporary object that contains a reference to the parent class
# It makes inheritance more manageable and extensible 
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

# --------- TYPES OF INHERITANCE ---------
# 1. Single Inheritance - It means that there is one parent and one child class
# 2. Multi-level Inheritance - Here Parent and child class are further inherited to form a new class. This forms the multi-level inheritance
# 3. Hierarchical Inheritance - In this type of inheritance there is one parent class and mutliple child classes 
# 4. Multiple Inheritance  - In this type of inheritance there are multiple parent classes and from these parent classes one child class if formed, It is one of the important type of inheritanc
# 5. Hybrid Inheritance - It contains various different types of inheritance
# 6. Cyclic Inheritance

# ----- MRO ( Method Resoulution order ) ------------- 
# MRO represents how the properties ( attributes, methods) are searched in inheritance
# Python first search in child class and then goes to parent class. So priority is to the child class

# Example of multi-level inheritance
class Grand_father :
     def __init__(self):
          print("Grandfather constructor called")
          self.name = "RK"
class Father(Grand_father):
     def __init__(self):
          super().__init__()
          print("Father constructor called")
          self.occupation = "Bussinessman"
class Son (Father):
     def __init__(self):
          super().__init__()
          print("Son constructor called")
          self.city="New York"
# Here the son constructor is called as its preference is higher 
# If there was no son constructor, in that case father constructor would've called. Also if father constructore was not there then grand father constructor would've been called
# the above case is only true when we are not using the super method 
# Once we define the super keyword to access the property of parent class it will call the constructor of the parent as well as grand parent class
# As it is multi level inheritance we have created an object of child class and by using inheritance we will access the properties not only of child class but also of parent and grand parent class

obj_1 = Son()
# The object that we've made here is of the child class, but as it multi level inheritance we can access the properties of the parent and grand parent class using this object itself
print(obj_1.city)  # It is the property of the child class itself This will print New york
print(obj_1.occupation) # It is the property of the parent class and will print Bussinessman
print(obj_1.name) # It is the property of grand parent class and will print RK



print("--------------------------")


# Hierarchical inheritance example
# consider a class called person that has properties like name and age
# we will create another class called student that inherits person class and will inherit its property such as name and age and will have and additional property called marks
# Same will be the case with another class called employee and it will also have an additional property called salary

class Person:
     def __init__(self,name,age):
          self.name= name
          self.age= age
     def display(self):
          print(f"The name and age of the person is {self.name} and {self.age}")
          
class Employee(Person):
     def __init__(self,name,age,salary):
          super().__init__(name,age)
          self.salary =  salary
     def displayE (self):
          print(f"The name, age and salary of the employee is {self.name},{self.age} and {self.salary}")
class Student(Person):
     def __init__(self,name,age,marks):
          super().__init__(name,age)
          self.marks = marks
     def displayS (self):
          print(f"The name, age and marks of the student is {self.name},{self.age} and {self.marks}")
          
s1 = Student("Harsh",21,93)
e1 = Employee("Rahul",28,300000)
p1 = Person("Jayraj",24)

s1.displayS()
e1.displayE()
p1.display()

print("--------------------------")


# Multiple inheritance example
# Let us  consider that there are 3 classes that are district, state and country
# And each class will have its office
class Country:
     def __init__(self):
          print("Country constructor is called")
          self.office="Delhi"   # This is the office of the country class
class State:
     def __init__(self):
          print("State constructor is called")
          # super().__init__()
          self.office = "Ahmedabad"
class District(State,Country): # Here when we are inheriting multiple classes, then the init method of the class on the left will be called
     # because the priority of the classes on the left is higher
     def __init__(self):
          super().__init__()   # Now as we have used super method the constructor of the parent of the left side is called 
          # but to call the constructor of the parent class on the left side we have to use the super method in the class on the left side (in this case state class)
          print("District constructor is called")
          super().__init__()
          self.office = "Sabarmati"

o1= District()
print(o1.__dict__)
print("--------------------------")

#------------------------------ Constructor-Overriding --------------------------------
# In inheritance when in the child class there is no constructor (__init__) then it automatically calls the constructor of the parent class (if described
# But what if the child class also has the constructor ???...
# Then the preference of the constructor of the child class will be higher than the parent class
# This is called constructor over-riding



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

# print() 
print("--------------------------")

 # ---------------- Encapsulation ------------------------------
 # The wrapping up of data and methods working on data together in a single unit (i.e.class) is callled encapsulation
 # The main purpose of encapsulation is to stop the access of the data and properties by the use of objects outside the class
 # By using encapsulation the properties can only be accessed with the help of the class methods
 # For example in the class without encapsulation when we create an object of its respective class, then we can access the properties of the class directly using the object
 # This could be done in this way ---> object_name.property
 # This could land the code in trouble sometimes
 # so to avoid it we use encapsulation 
 
 # Example of the code without encapsulation
 
class Finance:    # this is the finance class and has the data called revenue that is sensitive
     def __init__(self):
          self.revenue = 10000
          self.number_of_sales = 114
f1 = Finance()
print(f1.__dict__) # To know the content of the finance class we are printing the dict of the object
class HR:
     def __init__(self):
          self.number_of_employee = 16
          f1.revenue=50000  # Here we are not only accessing the sensitive data of the class but also modifying the value it
          # This type of data cannot be directly accessed by the object of the class
          # Now we will print the dict of the HR class to confirm that the data is changed
h1 = HR()
print(f1.__dict__)          # This will show that the data of the fincance class i.e revenue is getting modified

print("--------------------------")

# so in the above example we changed the sensitive data of the class from outside the class
# consider the website of the bank could be accessed in an unauthorized way, This may be problematic
# Hence to prevent this from happening, encapsulation is used


# Generally in encapsulation, we restrict the data access outside the class
# Encapsulation can be achieved by declaring the data members and methods of the class as private
# So we use access modifier : they are public, private and protected
# We don't use the protected method much in python so here we will only know more about public and private

# Public member - Accessible anywhere by using the object reference
# Private member -  Accessible within the class only via methods
# Protected member - Accessible within class and it's subclasses (Basically it is used in inheritance, but not often)

# So in order to make the revenue variable private, we just add two underscore infront of the variable __
# now let's check it again

class Finance:
     def __init__ (self):
          self.__revenue= 100000   # This is private member as it has two underscores
          self._number_of_employee = 120   # This is protected member as it has only one underscore
     def display(self):
          print(f"The revenue generated is {self.__revenue}, with the help of {self._number_of_employee} employees")
f1 = Finance()

print(f1.__dict__)

class HR:
     def __init__(self):
          self.number_of_center=55
          f1.__revenue=110 # by using this method the private data variable cannot be modified but instead a new private data variable is created for the HR class
          #print(f1.__dict__)# This line is commented because it generates an error because the revenue is private member and cannot be accessed by object
h1 = HR()
print(f1.__dict__)
print(h1.__dict__)
# print(__revenue) # It will give an error as private members cannot be accessed outside the class but they can be accessed it there is a method defined in class
f1.display() # so now by using the class method we can see the private members
print("--------------------------")

# The private data is stored as _classname__variablename and this process is called name-mangling
# Although python provides some security by hiding the private members, it does not completely hide them
# If someone knows that private variable are stored after having name mangling, then they can access those variables
# below I'll illustrate that we can access private variable 

# print(f1.__revenue) # This will require 
print(f1._Finance__revenue) # By using it will print the private variable too. Because I know name-mangling I can access the  
print("--------------------------")

# --------------------------------- POLYMORPHISM ----------------------------
# Polymorphism is an ability of python to take many forms
#  Python has several built-in polymorphism objects
# such as + operator which works on both integer and string
# next is len() function which can count the number of elements in list, no of keys in dictionary as well as it can count the number of words in string
#Then there is reversed()function which can print the words in reversed order of a string as well as it can print the elements in reverse order of a list. it is illustrated in the example below

a = "INFOSYS"
for i in  reversed(a):
     print(i)# It will print SYSOFNI
print("--------------------------")

li = ["Ram","Laskshman","Janki"]
for j in reversed(li):
     print(j)# It will print janki, lakshman, ram
# Here we saw the example of polymorphism where the same function has more than one form 
print("--------------------------")

 
 # We can also change the functionality of the built-in function by using over-riding
 # We cannot directly use the len() function to know the length of the object
 # for that we have to define the len method in our class
 
 # let's understand by example
 
class Shopping:
      def __init__(self,basket1,basket2,basket3):
           self.clothes = basket1       # clothes will go in basket 1
           self.electronics = basket2   # electronic items will go inside the basket 2
           self.others= basket3         # other items will go inside the basket3
           
user1= Shopping(["Hoodie","6 Pocket Cargo","T-shirt","Denim Jacket","3 pair of jeans"],["Laptop","Mobile","Fridge"],["Bagpack","Tiffin"])
# print(len(user1)) # this will return error as we cannot directly measure the length of the object 
# The above line returns error so I have commented that line

# So we can create the custom len method

class Shopingg:
          def __init__(self,basket1,basket2,basket3):
               self.clothes = basket1       # clothes will go in basket 1
               self.electronics = basket2   # electronic items will go inside the basket 2
               self.others= basket3         # other items will go inside the basket3
          def __len__(self): # this is the magic method which can return the len of the object
               return len(self.clothes)+len(self.electronics)+len(self.others)  # here we are returning the len because if we print the values it will  give error sometime
          # As print returns none and the len() function requires integer to return a number
          # And hence we are having the return 
          
user2 = Shopingg(["Hoodie","6 Pocket Cargo","T-shirt","Denim Jacket","3 pair of jeans"],["Laptop","Mobile","Fridge"],["Bagpack","Tiffin"])
print(len(user2))
print("--------------------------")

class BMW:
     def fuel_type(self):
          print("Diesel")
     def top_speed(self):
          print("213 km/hr")
class Ferrari:
     def fuel_type(self):
          print("Petrol Octane 90")
     def top_speed(self):
          print("311 km/hr")
          
def car_select(obj):
     obj.fuel_type()
     obj.top_speed()
bmw=BMW()
ferrari=Ferrari()
# here we have shown polymorphism by illustrating the same methods having different functionality
# In this example we have used the same function called fuel type and top speed
# but being same they print different values
car_select(bmw)
print("--------------------------")
car_select(ferrari)
print("--------------------------")

# ------------------------ Operator - Overloading  ----------------------
# The meaning of operator-overloading is that same operator behaves differently depending on values
# for example + operator works in a different way
# 1 - for adding two integers

a=55
b=14
print(a+b) # here + operator works for addition of 2 numbers and output will be 69
print("--------------------------")

# 2 - for string concatenation

greeting = "Hello"
name = "Raj"
print(greeting +" "+ name)

print("--------------------------")

# --------------------------- Modules ---------------------------------
# A module is like code library
# It contains set of functions you want to include in the application
# here we have created a file called mymodule.py and there I have created a function called greeting where it prints greeting.
# to use the module we have to import the name of the module and then we have called greeting

import module_res.mymodule as mymodule
mymodule.greeting("Rohan")
# In the below example i have created a simple calculator in another file and I am importing it 
# result = mymodule.calci(15,11)
# print(result)

# mymodule.KBC()  

# these I have commented kbc because it asks for input at run-time and it disturbs the code below it 
# We can also import module by the name we want to import. This is called module re-naming or aliasis
# for example below I have impor ted 
# 
# 
# import mymodule as mm
# mm.KBC()
print("--------------------------")

# We can import only specific part of the module such as function, class or variable 
from module_res import mymodule
mymodule.greeting("124dd")

from module_res import mymod_2
mymod_2.greet("RRK")
 