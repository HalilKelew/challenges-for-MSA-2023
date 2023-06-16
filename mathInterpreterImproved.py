def main():
    while True:
        
        while True:
            #prompt the user for the expression
            rawInput = input("Please enter the expression you want to get interpreted: (for example: 2 + 5)")

            #use .split() to get the parts of the expression. Split at the space
            refinedInput = rawInput.split(" ")

            if len(rawInput) != 3:
                print("ERROR: ENTER EXPRESSION IN X Y Z FORMAT!")
                continue
            #get values from list
            value1 = float(refinedInput[0])
            value2 = refinedInput[1]
            value3 = float(refinedInput[2])

            if value2 not in ["+","-","*","/"]:
                print("ERROR: INCORRECT OPERATOR, ONLY (+,-,*,/) ALLOWED. \n")
            break
        #determine the type of operation to carry out using if/elif/else statement
        if value2 == "+":
            print(f"{value1} plus {value3} is equals to {value1 + value3}.")
        elif value2 == "-":
            print(f"{value1} minus {value3} is equals to {value1 - value3}.")
        elif value2 == "*":
            print(f"{value1} multiplied by {value3} is equals to {value1 * value3}.")
        elif value2 == "/":
            print(f"{value1} divided by {value3} is equals to {value1 / value3}.")
        else:
            print("ERROR, PLEASE CHECK THE GUIDE AND RETRY AGAIN!")
        #run the expression and print output formatted one decimal place
        anotherCalculation = input("Would you like to evaluate another expression? (y/n): ").lower()
        if anotherCalculation != "y":
            break

