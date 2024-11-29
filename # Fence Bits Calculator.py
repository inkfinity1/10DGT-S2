# Fence Bits Calculator
# Author: Derek Wu
# Date: 2024/11/13
# Version 1

from pydoc import text

def valid_num(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                return num
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

def valid_pixel(question):
    while True:
        try:
            response = int(input(question))
            if response > 0:
                return response
            else: 
                print("Please enter a valid whole number above 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

print("Bit Calculator\nKia ora there\n This calculator with calualate the integer, text and image")

while True:
    selection = valid_num("\nSelect what type of data you would like to calculate.\n\nPress 1 for ineger\nPress 2 for text\nPress 3 for image\n")
    
    if selection == 1:
        # Covert numbers to binary and bits.
        user_num = int(float(valid_num("Please enter your number:\n")))
        binary_representation = bin(user_num)[2:]
        bits = (len(binary_representation))
        print(f"The number {user_num} in binary form is {binary_representation}. {bits} bits are required to represent {user_num}")
        pass
           
    elif selection == 2:
        # Convert text to binary and bits
        text_bit = len(input("\nWrite in the text that you want to calculate the number of bits that it uses.\nThe calculation will only be accurate if you use ascii charictors\n"))* 8
        print(f"\nThe number of bits that are in the text are {text_bit}")
        keep_going = input("\nIf you would like to do another calculation press <enter>. If not press any other key.")
        pass
        
    elif selection == 3:
        # Convert imager into binary and bits
                pixel_height = int(valid_pixel("Please enter the height of your image in pixels\n"))
                pixel_width = int(valid_pixel("Please enter the width of your image in pixels.\n"))
                bits = (pixel_height * pixel_width) * 24
                kilobytes = bits/8000
                print(f"Your image is represented with {bits} bits/ {kilobytes} kilobytes") 
                pass
    
    if input('Continue? Press Enter to continue or any other key to quit: '):
        print("Thank you for using the calculator!")
        break
