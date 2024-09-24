# Loops and indents
# Aithor: Derek Wu
# Date: 20 September 2024
#Verion: 2
# TODO:
    # Get user input (ask the user for their name)
    # Ask the user for two number
    # add the number together

# Ask the user for their name
name = input("What is your name?")
print(f"Kia ora {name}.") # f stand for format. We are formatting the print statement.

# Ask the user for two number
num_1 = int(input("what is your favourite number?"))
num_2 = int(input("What is your less favourite number?"))
 
 # Add numbers together
sum = num_1 + num_2
print(f"The numbers added together equal to {sum}")

# for loops. Repeat for a set number of times.
# for start the lopp
# next is the name of the loop
# in range tells the loop how many times to run
# the number in the () is how many times it repeats
for name_of_loop in range(5): 
    print("ha!")

# while loop. RUns until a condition is met or no longer is met
keep_going = "" # empty variable
while keep_going == "":
    print("Looping")
    print("Still looping")

    keep_going = input("Again? or press any other key to quit")