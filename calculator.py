"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Replace this with your code

while True:
    input_str = input("Enter Equation: ")
    tokens = input_str.split(" ")
    #we need to check that this str is good and contains all needed tokens
    result = 0
    print (tokens)
    lenghts = len (tokens)
    if tokens[0] == "q":
        print("quit")
        break
    
    num1 = int(tokens[1])
    if len(tokens)== 3:
        num2 = int(tokens[2])

    if lenghts >= 2:
        #go ahed to calculate
        if tokens[0] == "pow":
            result = power(num1, num2)
        elif tokens[0] =="+":
            result = add(num1, num2)
        elif tokens[0] =="-":
            result = subtract (num1, num2)
        elif tokens[0] =="/":
            result = divide (num1, num2)
        elif tokens[0] =="*":
            result = multiply (num1, num2)
        elif tokens[0] =="square":
            result = square (num1)
        elif tokens[0] =="cube":
            result = cube (num1)
        elif tokens[0] =="mod":
            result = mod (num1, num2)
        print(result)
    
    else:
        print("Not enough numbers")

    