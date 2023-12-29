#-------------------------------- P A T T E R N S -------------------------------------------

# 1️⃣ Right-Angled triangle using star **
# '''
# *
# **
# ***
# ****
# *****
# '''

size = 5 # It is the size or number of rows in the pattern
for i in range (1,size+1):
     print('*'*i)
     
print("----------------------------------------")
# Now we will perform same triange but with number
#''' 
# 1
# 22
# 333
# 4444
# 55555
# '''

size=5
for i in range (1,size+1):
     print(f'{i}'*i)
 
print("----------------------------------------")
     
#1
#12
#123
#1234
#12345

size=5
for i in range(1,size+1):
     for j in range(1,i+1):
          print(j , end="")
     print()

print("----------------------------------------")

#1
#21
#321
#4321
#54321

size=5
for i in range(1,size+1):
     for j in range(i,0,-1):
          print(j , end="")
     print()

print("----------------------------------------")

# --- 2️⃣ Inverted Right-Angled Triangle
#54321
#4321
#321
#21
#1

size=5
for i in range(size,0,-1):
     for j in range(i,0,-1):
          print(j,end="")
     print()

print("----------------------------------------")

#12345
#1234
#123
#12
#1

size=5
for i in range(size,0,-1):
     for j in range(1,i+1):
          print(j,end="")
     print()
     
print("----------------------------------------")
#    1
#   12
#  123
# 1234
#12345

size =5

for i in range(1,size+1):
     #The below loop is the print spaces 
     for j in range(size,i,-1):
          print(' ',end="")
      #The below loop is used to print numbers
     for k in range(1,i+1):
               print(k,end="")
     print() # Using this print statement we define to move to the next column
     
print("----------------------------------------")

#12345
# 1234
#  123
#   12
#    1

size=5
for i in range(size,0,-1):
     for space in range(size-i):
          print(' ',end="")
     for number in range(1,i+1):
          print(number,end="")
     print()

print("----------------------------------------")

#54321
# 5432
#  543
#   54 
#    5

# size=5
# for i in range(size,0,-1) :
#      for space in range(size,i,-1):
#           print(' ',end="")
#      for number in range(i,0,-1):
#           print(number,end="")
#      print()

size = 5

for i in range(size, 0, -1):
    # Print spaces
    for j in range(size, i, -1):
        print(' ', end='')

    # Print numbers
    for k in range(size, size-i, -1):
        print(k, end='')

    # Move to the next line after printing each row
    print()


print("----------------------------------------")
    
#5
#45
#345
#2345
#12345

size=5
for i in range(size,0,-1):
     for j in range(i,size+1):
          print(j,end="")
     print()
     
print("----------------------------------------")
     
#1
#2 3 
#4 5 6
#7 8 9 10
#11 12 13 14 15

# In this pattern we have to create a variable called 'counter'
size=5
counter=1
for i in range(1,size+1):
     for j in range(i):
          print(counter,end=" ")
          counter+=1
     print()

print()
print("----------------------------------------")

# 3️⃣ Diamond of numbers
#    1
#   121
#  12321
# 1234321
#123454321
# 1234321
#  12321
#   121
#    1

size=5
#This loop is for the upper part of the pattern
for i in range(1,size+1):
     for space in range(size,i,-1): # It is for spaces 
          print(" ",end=" ")
     for number in range(1,i+1): # It is the numbers that forms the pattern on left side consisting numbers in increasing order
          print(number,end=" ")
     for numb2 in range(i-1,0,-1):# This is for right side where the numbers are decreasing
          print(numb2,end=" ")
     print()
for j in range (size-1,0,-1):
     for space2 in range(size,j,-1):
          print(" ",end=" ")
     for numb3 in range(1,j+1):
          print(numb3,end=" ")
     for numb4 in range(j-1,0,-1):
          print(numb4,end=" ")
     print()