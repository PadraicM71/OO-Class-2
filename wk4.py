# wk4


#loops
#iterations!


# while loop
x = 0 # Setup a variable to use for the conditional

while x <= 10: # Continue looping until x is greater than 10
    print(x) # Print the current iterations value of x
    x += 1 # Inrement x by 1 (add 1 to the current value of x)

print("loop Finished") # This will execute after the loop since it's at a lower indentation level



#for loop
shopping_list = ["Eggs", "Ham", "Milk"]

for z in shopping_list: # Iterate through the shopping list
    print(z) # Print the item at the current iteration



#break loop
greeting = "Hello-World" # Setting up a string to iterate through

for character in greeting: # Iterate over the string one letter at a time
    if "-" in character: # if the current character is a hyphen
        print("Hyphen detected, ending loop!")
        break # End the loop
    else:
        print(character) # Print the current character

print("loop has exited")



#continue - see below - this is a bad example to use
x = 0 # Initialize a variable to use in the condition

while x < 10:
    x += 1
    if ((x % 2) == 0): # If the number is even - also here we have another condition we have extra indent
        print(x) #this print belongs to the if condition - double indent

    else: # If the number is odd
        print(str(x) + " not an even number")
        continue # Go to next iteration - see below
    #actually from class 'continue' is not needed here for this to work - bad example - but you get the idea!




print("loop tricks and techniques")

#avoid infinate loops!
#stop with ctrl c


#loop nesting
#note here 3 lists in a list - can be used for dictionaries tupes etc
# an array within another array
shopping_lists = [["Eggs", "Milk", "Ham"], 
                  ["Vinegar", "Mustard", "Ketchup"], 
                  ["Burgers", "Lettuce", "Mayo"]]

for current_list in shopping_lists: # Steps through the list of lists
    for item in current_list: # Steps through each list
        print(item) # Prints the item in the current shopping list


# #USING LOOPS FOR VALIDATION
# #using a loop to validate input from a user
# while True: # This is an infinite loop
#   number = int(input("Please type a number between 1 and 10: ")) # Take user input

#   if number < 1: # Number is too small
#     print("Number provided is less than 1")

#   elif number > 10: # Number is too large
#     print("Number provided is greater than 10")

#   else: # If the input is in a valid range
#     print("number is between 1and10")
#     break # End the loop



#FOR LOOPS OVER A SET RANGE range() function takes two arguments
for number in range(5,11): # prints 5 to 10 - wont include 11
    print(number)
# also
for w in range(3):
    print(w)





#NEW TOPIC - FUNCTIONS


# Gameloop
# while turns < 100:             # Game goes until 100 score
#     player_move(player_one) # Player one's move
#     player_move(player_two) # Player two's move
#     turns += 1

# if player_one.score > player_two.score:
#     print("Player One Wins!")
# elif player_one.score < player_two.score:
#     print("Player Two Wins!")



# def sum(num_1, num_2):
#     """
#     Takes two variables (int's or floats), and
#     adds them together, then returns the result
#     """
#     result = num_1 + num_2
#     return result



# def greet(name="John doe", greeting="Hello there: "):
#     """Greets a person with the greeting and their name

#     Parameters
#     ----------
#     name: (str)
#         The name to greet by.
#     greeting: (str)
#         The greeting to greet by.
#     """
#     print(name, greeting)

# greet()
# greet(name = "Kieran Wood") # Prints: Hello there: Kieran Wood
# greet(greeting = "How it be: ") # Prints



