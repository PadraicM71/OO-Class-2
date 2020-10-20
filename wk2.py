# Wk2






list1 = [1,2,3]
list1.append(4)
print (type(list1))
print(list1[3])



dict = {"name":"John Doe", "age": 21, "net worth": 5213.4}
#essentially a JSON file - can pretty up if like on different lines.
print (dict)
print(dict ["net worth"]) #refer to name of variable - whats inside sq brackets is a predicate



dict2 = [
        {"name":"Jack", "age": 24, "net worth": 2345},
        {"name":"paul", "age": 34, "net worth": 5645}
        ]
print (dict2[1]["name"])




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


