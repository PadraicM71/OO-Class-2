# Wk1 and Wk2

name = "Padraic"
print(name)
name = 'Callum'
print(name)
print(type(name))

Var1 = True
Var2 = False
print (type(Var1))


# Collections:

#Lists
list1 = [1,2,3]
list2 = []
list3 = [1,"paddy",2.35]
list1.append(4)
print (type(list1))
print (list1)
print(list1[3]) # thisn will print 4

#Tupes
tup1 = ()
tup2 = (2,3,4,5)
tup3 = (2,"paddy",4.55)
print(tup3[1])




dict = {"name":"John Doe", "age": 21, "net worth": 5213.4}
#essentially a JSON file - can pretty up if like on different lines.
print (dict)
print(dict ["net worth"]) #refer to name of variable - whats inside sq brackets is a predicate


dict2 = [
        {"name":"Jack", "age": 24, "net worth": 2945},
        {"name":"paul", "age": 34, "net worth": 5645}
        ]
print (dict2[1]["name"])
print (dict2[0]["net worth"])

dict2 [1]["bankbalance"] = 115000
print (dict2[1]["bankbalance"])

# Type Casting
anyvar1 = "4" # str
# 2 + anyvar1 would throw an error
print (2 + int(anyvar1))


# Exercises

"""
    =========== Exercise 1 =============

    Using a list, create a shopping list of 5 items. Then
    print the whole list, and then each item individually.
"""

shopping_list = ["apples","garlic","spudz","milk","butter"] # Fill in with some values

print(shopping_list) # Print the whole list

print(shopping_list[2]) # Figure out how to print individual values


"""
    =========== Exercise 2 =============

    Find something that you can eat that has nutrition
    facts on the label. Fill in the dictionary below with
    the info on the label and try printing specific information.

    If you can't find anything nearby you can use this example: https://www.donhummertrucking.com/media/cms/Nutrition_Facts_388AE27A88B67.png
"""
# When ready to work on these exercises uncomment below code

nutrition_facts = {"salt":3,
                "sugar":9,
                "fat":88} # Fill in with the nutrition facts from the label

print(nutrition_facts) # Print all the nutrition facts

print(nutrition_facts["sugar"]) # Uncomment this line and pick a value to print individually

"""
    =========== Exercise 3 =============

    Python has a function built in to allow you to
    take input from the command line and store it.

    The function is called input() and it takes one
    argument, which is the string to display when
    asking the user for input.


    Here is an example:
    ```
    >> name = input('What is your name?: ')

    >> print(name)
    ```

    Using the information about type casting take an input
    from the command line (which is always a string), convert
    it to an int and then double it and print it.

    i.e. if the user provides 21 then the program should print 42
"""

# When ready to work on these exercises uncomment below code

age = input('What is your age?: ')

print(int(age) * 2) # Find a way to convert the age to an int and multiply by 2


#end
