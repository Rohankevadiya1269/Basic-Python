num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operation = input("Which operation to perform? add / subtract / multiply / divide ")
try:
    if operation == "add":
        print(num1+num2)
    elif operation == "subtract":
        print(num1-num2)
    elif operation == "multiply":
        print(num1*num2)
    elif operation == "divide":
        print(num1/num2)
    else:
        print("Enter the valid operation to perform")
except Exception as e:
    print(f"Error: Invalid operation {e}")
    