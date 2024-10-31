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
            Width = float (input('Enter a Width: ')) # Ask the user for an imput number for the Width
            while Width <= 0: # Checks if the imput number in greater than 0
                Width = float (input(' ERROR Please Enter a Width greater than 0: ')) 

            Length = float (input('Enter a Length: ')) # Ask the user for an imput number for the Length
            while Length <= 0: # Checks if the imput number in greater than 0
                Length = float (input(' ERROR Please Enter a Length greater than 0: ')) 
            break
        except ValueError: # Error Checker
            print('ENTER A NUMBER ')

    perimeter = 2* Width+ 2* Length # solving the prerimeter for the user
    Cost = perimeter * 10 # solving the Area for the user

    print(f" Your  perimeter is {perimeter} units") # prints the perimeter
    print(f" Your Cost: ${Cost}") # prints the Area

    again = input('Do we want to continue? (press Enter) or press any other key to quit:  ') # Ask the user if the want to contiune
    if again == '':
        start=True
        print("What is your next number?")
    else:
        start = False