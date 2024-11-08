# Fence Cost Calculator
# Author: Derek Wu
# Date: 2024/11/8
# Version 3

def valid_num(prompt):

    while True:
        try: # The try block attempts to convert the user input to a float.
            num = float(input(prompt))
            if num > 0: 
               return num 
            else: # If the input is invalid or less than or equal to zero, an error message is printed, and the user is prompted again.
                 print("Please enter a positive number") 
        except ValueError:
            print("Please enter a valid number")

print("Fence Cost Calculator\nKia ora there")

while True:
    print("If you choose 'FEET', please enter the dimensions in meters; we will convert them for you.")
    unit = input("Do want to use meter of feet?\n ").strip().lower() # Ask the user if they want to use meter or feet.
    if unit not in ['meters', 'feet']: # If the user puts an invaild unit.
        print("Invalid unit! Defaulting to meters.")
        unit = 'meters' # It changes it to the default unit (meter).
    print("Note that you have to enter a number that is greater than 0\nWhat are your numbers?\n---------------------------------------------- ")

    width = valid_num( "Please enter the width in meters:\n ") # User input width
    length = valid_num( "Please enter the length in meters:\n ") # User input length
    cost = valid_num( "Please enter the cost per meter\n$: ") # User input cost

    perimeter = 2 * width + 2 * length # solving the prerimeter for the user.
    if unit == 'feet': 
        perimeter *= 3.28084 # convert perimeter to feet 

    while True: 
        try:
            gates = int(input("Number of gates (enter 0 if none):\n ")) # integer 
            if gates >= 0: # The number is more than(or equal to) 0
                break
            else:
                print("Please enter a non-negative integer")
        except ValueError:
            print("Invalid input. Please enter a whole number")

    while True:
        try:
            gate_cost = float(input("Cost of one gate\n$: ")) # float
            if gate_cost >= 0: # The number is more than(or equal to) 0
                break
            else:
                print("Please enter a non-negative number")
        except ValueError:
            print("Invalid input. Please enter a valid number")

    total_cost = round(perimeter * cost, 2)  # solving the Cost of the fence for the user and round the total cost to 2 decimals places.

    total_gate_cost = gates * gate_cost # Solves the cost of the gate by the number of gates times the gate cost.
    total_cost += total_gate_cost # Adds the total cost with the total cost of the gate.

    print(f" Your total cost including gates: ${total_cost:.2f}") # prints the cost of the fence and the gate
    print(f" Your perimeter is {perimeter:.2f} units") # prints the perimeter.

    if input('Continue? Press Enter to continue or any other key to quit: '): # If enter is press its loops the code.
        print("Thank you for using the calculator!") 
        break