#Wk4



#LOOPS

"""
    =========== Exercise 1 =============
    Take the current for loop below and add
    two conditions to the loop body:
        1. If 'Eggs' are the current element, then conitnue
        2. If 'Sausages' is the current element, stop iterating.
"""
shopping_list = ["Bread", "Bannanas", "Pineapples", "Eggs", "Oranges", "Milk", "Sausages"]
for item in shopping_list: # Iterate over the items in the shopping list
    print(item)
    if "Eggs" in item:
        print ("Eggs detected - continuing")
    elif "Sausages" in item:
        print ("Sasuages detected - exit loop")
        break
         # Remove this and replace with your own loop body logic



#"""
#     =========== Exercise 2 =============
#     Take the current existing shopping list
#     and ask the user to add a number of items
#     to the list.
#     For example, if someone enters 3 then prompt
#     them for input and append it to the list 3 times.
# """
# amount_to_add = int(input("How many items do you want to add?"))
# counter = 0 # A counter to keep track of the number of items that have been added
# while counter <= amount_to_add:
#     # Do stuff
#     None # Remove this and replace with your own loop body logic 



# #FUNCTIONS # see end of recorded class - talking about this

# """
#     =========== Exercise 1 =============
#     Add a docstring to the function below.
#     The function takes a list and prints all 
#     the items in the list.
#     Bonus: Try using type declaration for the argument.
# """
# def print_list(list_to_parse):
#     """TODO: Add docstring"""
#     for item in list_to_parse:
#         print(item)
# """
#     =========== Exercise 2 =============   # Michael had a problem with this.
#     Implement the delete_item() function
#     below, all the details to do so should
#     be there for you.
#     Hint: you can use del(list[index]) to remove
#     an item from a list.
# """
# def delete_item(list_to_parse, item_index):
#     """Takes a list, removes an item at the 
#     specified index and returns the list
#     Parameters
#     ----------
#     list_to_parse:
#         The list to remove the item from
#     item_index:
#         The index to remove an item from
#     Returns
#     -------
#     The list with the item removed
#     """
#     # Do stuff here
#     pass # This just tells python to do nothing; remove it when you add your code
# shopping_list = ["eggs", "ham", "sausages"] # A test list to remove an item from
# shopping_list = delete_item(shopping_list, 1) # Should remove 'ham' from the list
# print(shopping_list)


#

