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