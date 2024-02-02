def greeting(name):
    print("Hello, " + name)
    
def calci(num_1,num_2):
    choice = input("which function you want to perform : ")
    if choice=="addition" or choice=="Addition"or choice=="ADDITION":
        return num_1+num_2
    elif choice=="subtraction"or choice =="Subtraction" or choice =="SUBTRACTION":
        if num_1>num_2:
            return num_1-num_2 
        else:
            return num_2-num_1
    elif choice=="multiplication"or choice =="Multiplication" or choice =="MULTIPLICATION":
        return num_1*num_2
    elif choice=="division"or choice =="Division" or choice =="DIVISION":
        return num_1/num_2

def KBC():
    point=0
    question_1="Q1. In which year other than 2011, did India won the world cup?\nA. 2003\nB. 2023 \nC.1983 \nD.1999"
    print(question_1)
    answer = input("Please enter a choose a correct option: ")
    if answer == "C" or answer=="c":
        print("Yeah! you got it correct.. Congratulation you won 20 points")
        point+=20
    else:
        print("OOPS! You were too close. The correct option is : C")
    print()
    question_2="Q2. In which year India got its independence? \nA. 1899\nB. 1497 \nC.1943 \nD.1947"
    print(question_2)
    answer = input("Please enter a choose a correct option: ")
    if answer == "D" or answer == "d":
         print("Yeah! you got it correct.. Congratulation you won 20 points")
         point+=20
    else:
        print("OOPS! You were too close. The correct option is : D")

        
    print("Total points earned is: ",point)