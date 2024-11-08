# Fence Cost Calculator
# Author: Derek Wu
# Date: 2024/11/6
# Version 2

def valid_num(prompt):

    while True:
        try:
            num = float(input(prompt))
            if num > 0:
               return num
            else:
                 print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

start = True

print("Fence Cost Calculator")
print("Kia Ora their")

while start:

    print("If you choose 'FEET', please enter the dimensions in meters; we will convert them for you.")
    unit = input("Do want to use meter of feet? ").strip().lower() # Ask the user if they want to use meter or feet.
    if unit not in ['meters', 'feet']: # If the user puts an invaild unit.
        print("Invalid unit! Defaulting to meters.")
        unit = 'meters' # It changes it to the default unit (meter).
    print("Note that you have to enter a number that is greater than 0")
    print("what are your numbers?")
    print('----------------------------------------------')

    width = valid_num( "Please enter the width in meters: ")
    length = valid_num( "Please enter the length in meters:")
    cost = valid_num( " Please enter the cost $")

    perimeter = 2* width+ 2* length # solving the prerimeter for the user.
    total_cost = round(perimeter * cost, 2) # solving the Cost of the fence for the user and round the total cost to 2 decimals places.
    
    if unit == 'feet':
        perimeter *= 3.280804 # covert perimeter to feet.
        total_cost *= 3.28084 # Adjectust cost based on converion.

    gates = int(input("Enter the number of gates you have, if you don't have any gates please enter 0: "))
    gate_cost = float(input("Enter the cost of one gate: $"))

    total_gate_cost = gates * gate_cost # Solves the cost of the gate by the number of gates times the gate cost.
    total_cost += total_gate_cost # Adds the total cost with the total cost of the gate.

    print(f" Your total cost including gates: ${total_cost:.2f}") # prints the cost of the fence and the gate
    print(f" Your perimeter is {perimeter:.2f} units") # prints the perimeter.

    again = input('Do we want to continue? (press enter) or press any other key to quit:  ') # Ask the user if the want to contiune. 
    if again == '':
        start=True # If the user press enter it loops.
        print("What is your next number?")
    else:
        start = False # If the user press any other key its stops.
        print ("Thank you for using the calculator") 