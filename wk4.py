# wk4



#while loop
# x = 0 # Setup a variable to use for the conditional

# while x <= 10: # Continue looping until x is greater than 10
#     print(x) # Print the current itterations value of x
#     x += 1 # Inrement x by 1 (add 1 to the current value of x)

# print("loop Finished") # This will execute after the loop since it's at a lower indentation level



# #for loop
# shopping_list = ["Eggs", "Ham", "Milk"]

# for item in shopping_list: # Iterate through the shopping list
#     print(item) # Print the item at the current iteration



# #break loop
# greeting = "Hello-World" # Setting up a string to iterate through

# for character in greeting: # Iterate over the string one letter at a time
#     if "-" in character: # if the current character is a hyphen
#         print("Hyphen detected, ending loop!")
#         break # End the loop
#     else:
#         print(character) # Print the current character

# print("loop has exited")



# #continue
# x = 0 # Initialize a variable to use in the condition

# while x < 10:
#     x += 1
#     if ((x % 2) == 0): # If the number is even
#         print(x)

#     else: # If the number is odd
#         continue # Go to next iteration



# #loop nesting
# shopping_lists = [["Eggs", "Milk", "Ham"], 
#                   ["Vinegar", "Mustard", "Ketchup"], 
#                   ["Burgers", "Lettuce", "Mayo"]]

# for current_list in shopping_lists: # Steps through the list of lists
#     for item in current_list: # Steps through each list
#         print(item) # Prints the item in the current shopping list


# #USING LOOPS FOR VALIDATION
# while True: # This is an infinite loop
#   number = int(input("Please type a number between 1 and 10: ")) # Take user input

#   if number < 1: # Number is too small
#     print("Number provided is less than 1")

#   elif number > 10: # Number is too large
#     print("Number provided is greater than 10")

#   else: # If the input is in a valid range
#     print("number is between 1and10")
#     break # End the loop



# #FOR LOOPS OVER A SET RANGE
# for number in range(5,11):
#     print(number)





#NEW TOPIC - FUNCTIONS


