#Area and Perimeter
# Author: Derek Wu
# Date: 2024/10/25
# Version 1

start = True

print("Perimeter and Area")
print("Kia Ora their, what are your numbers?")
print("Please enter a number that is more than 0")
print('----------------------------------------------')
while start:
    while True:
        try:
            Width = float (input('Enter a Width: '))
            while Width <= 0:
                Width = float (input(' ERROR Please Enter a Width greater than 0: '))

            Height = float (input('Enter a Height: '))
            while Height <= 0:
                Height = float (input(' ERROR Please Enter a Height greater than 0: '))
            break
        except ValueError:
            print('ENTER A NUMBER ')

    perimeter = 2* Width+ 2* Height
    Area = Width * Height

    print(f" Your  perimeter is {perimeter} units")
    print(f" Your area is {Area} units^2")

    again = input('Do we want to continue? (enter y) or press any other key to quit:  ')
    if again == 'y':
        start=True
        print("What is your next number?")
    else:
        start = False
        
    

    


