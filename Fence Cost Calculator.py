#Area and Perimeter
# Author: Derek Wu
# Date: 2024/11/1
# Version 1
start = True

print("Perimeter and Area")
print("Kia Ora their, what are your numbers?")
print("Please enter a number that is more than 0")
print('----------------------------------------------')
while start: 
    while True:
        try: # Error Checker
            width = float (input('Enter a Width: ')) # Ask the user for an imput number for the Width
            while width <= 0: # Checks if the imput number in greater than 0
                width = float (input(' ERROR Please Enter a Width greater than 0: ')) 

            length = float (input('Enter a Length: ')) # Ask the user for an imput number for the Length
            while length <= 0: # Checks if the imput number in greater than 0
                length = float (input(' ERROR Please Enter a Length greater than 0: ')) 
            
            cost = float(input( 'Enter the cost of a meter of Fence: $'))
            while cost <= 0: # Checks if the imput number in greater than 0
                cost = float (input(' ERROR Please Enter the cost of a meter of Fence greater than $0: ')) 

            break
        except ValueError: # Error Checker
            print('ENTER A NUMBER ')

    perimeter = 2* width+ 2* length # solving the prerimeter for the user
    total_cost = round(perimeter * cost, 2) # solving the Cost of the fence for the user and round the total cost to 2 decimals places
    
    print(f" Your perimeter is {perimeter} units") # prints the perimeter
    print(f" Your Cost: ${total_cost}") # prints the cost of the fence

    again = input('Do we want to continue? (press enter) or press any other key to quit:  ') # Ask the user if the want to contiune. 
    if again == '':
        start=True # If the user press enter it loops
        print("What is your next number?")
    else:
        start = False # If the user press any other key its stops
        print ("Thank you for using the calculator") 

        
    
       