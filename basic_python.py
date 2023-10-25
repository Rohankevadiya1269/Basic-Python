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