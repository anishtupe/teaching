def add(a,b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "error fuck offf"
    
    return a / b

operations = {
    "1" : ("Add",add),  
    "2" : ("Subtract",subtract),
    "3" : ("Multiply",multiply), 
    "4" : ("Divide",divide),
}

while True:
    print("\n simple calci")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    Choice = input("enter num of  yo choice")

    if Choice == "5":
        Print("calci closed")
        break

    if Choice not in operations:
        print("invalid choice")
        continue

    a = float(input('enter num1'))
    b = float(input("enter num2"))

    operation_name,operations_func = operations[Choice]

    result = operations_func(a,b)
    print(f"result of {operation_name} is {result}")


  


        



    
