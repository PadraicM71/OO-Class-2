# Wk3



print (5+3)
sum_value = 5+8
sum_2 = 6 + sum_value
print (sum_value)
print (sum_2)


my_list = [1,2,3,4] # Initialize my_list

my_list_2 = [5,6,7,8] # Initialize my_list_2

my_list = my_list + my_list_2 # Take the current value of my_list and add my_list_2 to it

print(my_list) # Prints: [1, 2, 3, 4, 5, 6, 7, 8]


name = "Hello " # Set name variable to an string 'hello ' space here also for joining to world

name = name + "World!" # Take the current name value and add 'world' to it

print(name) # Prints: Hello World!



# my_list3 = [] # Initialize an empty list
# name = "John" # Initialize name variable to John
# my_list3 = my_list3 + name # Adding the current my_list variable to the string name
# print(my_list3) # Prints: ['j','o','h','n']
# #this will not work on new vervion of python - worked on earlier versions??
# #dont worry about this too much


print(5-3)
subvalue=5-8
print (subvalue -6)




mul=5*6
print(mul*8)
mul1 = mul * 100
print (mul1)


mul2 = [1,2,3,4] # Initialize my_list

mul2 = mul2 * 3 # Take my_list and multiply it by 3

print(mul2) # Prints: [1,2,3,4,1,2,3,4,1,2,3,4]




# floating point division
print (5/2)
value=5/4
print(value)
print (value/3)
value2 = value /8
print (value2)



#intiger division
print(5 // 3) # Prints: 1 - if answer is a float then it takes floor of division - rounds down - even if over 0.5
print (5//8)
divvalue = 10//6
print (divvalue/5)
print (divvalue//5)


print ("Shortcuts")
# Shortcuts

variable_1 = 5 # Initialize the variable to 5
# variable_1 = variable_1 + 5 # Take the current value of the variable and add 5
variable_1 += 5 #shortcut - same as above - works with /= aswell etc
print(variable_1)

variable_1 = 5 # Initialize the variable to 5
#variable_1 = variable_1 - 5 # Take the current value of the variable and subtract 5
variable_1 -= 5
print(variable_1)

variable_1 = 5 # Initialize the variable to 5
#variable_1 = variable_1 / 2 # Take the current value of the variable and floating point divide by 2
variable_1 /= 5
print(variable_1)
print (20 / 5) # sideline - floating point division will always get .0 even if answer is whole number

variable_1 = 5 # Initialize the variable to 5
#variable_1 = variable_1 // 2 # Take the current value of the variable and intege
variable_1 //= 2
print (variable_1)

q = 9
q *= 3
print (q)



# Modulus
print("modulus")
print (5//3)
print(5 % 3) # Prints: 2 - Modulus - prints the remainder - eg if you wanted to see if a number is divisible
# can use variables too etc
print(10%2)
x = 0
y = x % 6
print (y) # because 0/anything = 0




print("logical operators")

print(5 > 3) # Prints: True; since 5 is greater than 3

result = 5 > 3 # You can store the result in a variable

print(result) # Prints: True

print(3 > 5) # Prints: False; since 3 is NOT greater than 5

print(5 > 5) # Prints: False; since 5 is NOT greater than 5 (they are equal)

print(5>=5)


print(5 >= 3) # Prints: True; since 5 is greater than 3

result = 5 >= 3 # You can store the result in a variable

print(result) # Prints: True

print(3 >= 5) # Prints: False; since 3 is NOT greater than 5

print(5 >= 5) # Prints: True; since 5 is equal to 5


print("not")
print (not 5<3) #flips result
print(not 5 < 3) # Prints: True; since the statement 5 < 3 evaluates to False
result = not 5 < 3 # You can store the result in a variable
print(result) # Prints: True
print(not 3 < 5) # Prints: False; Since the statement 3 < 5 evaluates to True

print ("and")
print(5 > 3 and 8 > 6) # Prints: True; since both statements evaluate to True
print(5 < 3 and 8 > 6) # Prints: False; since the first statement evaluates to F

print("or")
print(5 < 3 or 8 > 6) # Prints: True; since both statements evaluate to True
print(5 > 3 or 8 > 6) # Prints: True; since the second statement evaluates to T

print ("in")
# name = input("Enter name: ") # Take someones name from the command line
# print("john" in name) # Prints: True if john is name given, or False otherwise
print(4 in [1,2,3]) # Prints: False since no 4 is present in the list
print(4 in [1,2,3,4]) # Prints: True since 4 is present in the list


print ("CONDITIONALS")

# if
print("if")
x = 1 # Setting up the x variable
if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
print(x) # Since this is on a lower indentation level, this code will run regardless
if x <= 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
print(x) # Since this is on a lower indentation level, this code will run regard
z=5
if z > 6:
    print("ok")
print("ok2")


# else
print("else")
x = 2 # Setting up the x variable

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
else:
    x -= 1 # This will run if x is not less than 3

print(x) # Since this is on a lower indentation level, this code will run regardless

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
else:
    x -= 1 # This will run if x is not less than 3

print(x) # Since this is on a lower indentation level, this code will run regard



# user_value = int(input("Enter a number between 0 and 5: "))

# if user_value == 0:
#     print("Zero")
# elif user_value == 1:
#     print("One")
# elif user_value == 2:
#     print("Two")
# elif user_value == 3:
#     print("Three")
# elif user_value == 4:
#     print("Four")
# elif user_value == 5:
#     print("Five")
# else: # If value is not between 0 and 5
#     print("Value provided is not between 0 and 5!")

    
    