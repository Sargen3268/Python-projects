try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print ("Select operation:")
    print ("+")
    print ("-")
    print ("*")
    print ("/") 

    O    = input("Enter operation: ")
    match O:
        case "+":
            print (a + b)
        case "-":
            print (a - b)
        case "*":
            print (a * b)
        case "/":
            print (a / b)
        case _:
            print ("Invalid operation")
except Exception as e:
    print ("Error: ", e)
        
