# Wk 5

# Week 5 exercises - discussions are from last 30min of wk5 


# name = "John Doe"
# print(f"hello, {name}")
# greeting = f"Welcome,{name}!"
# print(greeting) # Prints: Welcome John Doe! Injects the variable

# name = "John Doe" # very important - get this - they are created on call -
# greeting = f"Welcome, {name}!" # only update when they are created an not when variable is updated
# name = "Kieran Wood"
# print(greeting) # Prints: Welcome John Doe!
# greeting = f"Welcome, {name}!" # Since it's recreated it picks up the new value of name
# print(greeting) # Prints: Welcome Kieran Wood!


# Dates
# by default we dont have any methods or functions for dates
# there is a date type for the variable - but dont have a constructor for them(lecture Mikhail)
# so we import:
import datetime #The module works off of classes that you can use to create objects,
#to create a simple date object you just need to provide 3 attributes – 
# a year (int), a month (int), and day (int)
# lots of modules in Python itself - this one is included with Python distrubition already
f = datetime.date.today()
print (f)
# appolo_11_launch = datetime.date(1959, 9, 13)
# falcon_9_first_launch = datetime.date(2010, 6, 4)
# print(falcon_9_first_launch > appolo_11_launch) # prints: True
# print(falcon_9_first_launch.month)

# import datetime # lots of other features to this will do later

# appolo_11_launch = datetime.date(1959, 9, 13)
# print(appolo_11_launch.year) # prints: 1959
# appolo_11_launch.month # Prints: 9
# appolo_11_launch.day # Prints: 13

# import datetime # without the import it wont know what we want to acheive
# #because cannot reach that class
# current_datetime = datetime.date.today() # Returns datetime object of todays date
# print(current_datetime)






# CLASSES

# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# class Animal:  #reserved word class - here has 3 attritubes
#   def __init__(self, species_name, regions, common_name):
#     """A class to represent a generic animal

#     Attributes
#     ----------
#     species_name : (str) 
#         The technical species name of the animal
#     regions : (list[str]) 
#         A list of regions the animal is endemic to
#     common_name : (str) 
#         The colloquial name of the animal
#     """
#     self.species_name = species_name
#     self.regions = regions
#     self.common_name = common_name


# leopard_gecko = Animal("Eublepharis macularius",
#     ["Afghanistan","Pakistan","India", "Iran"],
#     "Common Leopard Gecko")
# #We have now INSTANTIATED the leopard_gecko INSTANCE
# #here the leopard_geko instance is passed to the class and becomes the 'self' in the class

# print(leopard_gecko.common_name)




#now add functions inside the classes - called Methods
#'self' instance that is been passed - the one created by the constructor -me
#class name capital letter - we define our class 'Classname'
#next we define an init Method
#before instance exists it needs to be initiated constructor - Michail
#
#self - for all instance attributes (variables specific to each instance and not the overall
# class) we are adding a 'self' in front with a dot.
# this is because when we create an 'instance', all of the variables are 'localised' to
# that 'instance'.
#The word self is used to represent the instance of a class and by using the self keyword
# we acess the Attributes and Methods of a class in Python.
class Animal:  #reserved word class - here has 3 attritubes - this is class definition
  counter = 0 # Initialize counter to 0 - becomes global for this specific Class
  # This ^^ is a class variable since it is outside of __init__ and has no self. in front
  def __init__(self, species_name, regions, common_name):
    """A class to represent a generic animal

    Attributes
    ----------
    species_name : (str) 
        The technical species name of the animal
    regions : (list[str]) 
        A list of regions the animal is endemic to
    common_name : (str) 
        The colloquial name of the animal
    """
    self.species_name = species_name
    self.regions = regions
    self.common_name = common_name
    Animal.counter += 1 # Accessing and incrementing the class counter by 1 on each instantiation of an Animal
                        # belongs to Animal Class so no self!
  def print_info(self):
    """Prints information about animal instance"""
    print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")
#here defining a new Method - and again passing self,
#passing that instance that we create -leopard_geko
#\n (comes from unix terminology - stands for a new line)


print(Animal.counter) #should print 0


leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")
"""Prints (not returns)
Common Name: Common Leopard Gecko
Species: Eublepharis macularius
Regions: ['Afghanistan','Pakistan','India', 'Iran']
"""


leopard_gecko.print_info()     #because its a function it has the brackets there
#this will call the print_info() method
#we just used the print_info Method inside the Class that we created

arctic_fox = Animal("Vulpes lagopus",
    ["The Arctic"],
    "Arctic fox")
#Self;
#Instance versus Class attributes.
#Instance
#so if use Animal Class
#now have 2 different animal instances and variables dont overlap

#This is the same with instance methods.
#The variables it pulls are specific to the instance and not the class.

leopard_gecko.print_info()
"""Prints (not returns)
'Common Name: Common Leopard Gecko
Species: Eublepharis macularius
Regions: ["Afghanistan","Pakistan","India", "Iran"]'
"""

arctic_fox.print_info()
"""Prints (not returns)
'Common Name: Arctic fox
Species: Vulpes lagopus
Regions: ["The Arctic"]'
"""

#Class attributes on the other hand are attributes that are common among all instances of a class.
#you wanted to keep a counter that goes up by 1 for every time a new animal is added.
#Since this information, is not specific to an instance, but rather to every instance of a
#given class you would want it to be accessible to every instance.
#see counter above - Now there is a counter variable that can be used to find out how many animals have been instantiated

print(Animal.counter) # Prints 2; since the Leopard Gecko, and Arctic fox have been instantiated

# Both below calls print 2; Class variables are also accessible in any instance
print(arctic_fox.counter)
print(leopard_gecko.counter)
#As you can see because the variable belongs to the class and not the instance, it is available to
#both the class as a variable, or any instances of the Animal class.




#Class Methods
#Methods are functions that are accessible through class instances, for example let's say
#you want to create a function to print all of the attributes of a class you could define the
#function in the class and then use the self operator to print the information.
#print_info() method used earlier is a class method.
#Setting up class methods is the same as setting up a regular function, you just need to indent it to 
#the same line as the class and always pass self as an argument.
#Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
#Dunder here means “Double Under (Underscores)”.
#These are commonly used for operator overloading – we will cover this later in the semester.
#Few examples for magic methods are: init, add, len, repr etc. - later semister
#__init__ METHOD
#The __init__ is a reserved method in python acts as a constructor (sort of) in Python.
#This method is called when an object is created from a class and it allows the class to initialise the attributes of the class.
#This means that it 'constructs' the instance.
#In our analogy of a cookie cutter from earlier, the __init__ method would be the actual cutting of the cookie.
#The method is run every time you instantiate an instance. For example when you run the leopard_gecko example from before:
#leopard_gecko = Animal("Eublepharis macularius",
 #   ["Afghanistan","Pakistan","India", "Iran"],
  #  "Common Leopard Gecko")
#The variable is making an implicit call to __init__, this would roughly be equivalent to:
#leopard_gecko = Animal.__init__("Eublepharis macularius",     -but we dont need to state __init__ as magic method - shortcut
#    ["Afghanistan","Pakistan","India", "Iran"],
 #   "Common Leopard Gecko")







#As you can see, you can do some basic logic in the __init__ method, such as for loops.

class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls prints 'Cookie Baked' as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      print("Cookie Baked!")

def bake_cookie(self):
    """Print's 'Cookie Baked!'."""
    print("Cookie Baked!")

CookieBaker(5)


#You can also call methods, just make sure to include self. when calling them since you are inside the instance.
#see diference here
# class CookieBaker:
#   def __init__(self, number_of_cookies):
#     """ Example class that is used to show off the __init__ method.
#     The __init__ method calls the bake_cookie() method as many times as there are number_of_cookies.

#     Attributes
#     ----------
#     number_of_cookies(int): How many cookies to bake
#     """
#     print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
#     self.number_of_cookies = number_of_cookies
#     for cookie in range(number_of_cookies):
#       self.bake_cookie()      #to call below method

#   def bake_cookie(self):
#     """Print's 'Cookie Baked!'."""
#     print("Cookie Baked!")
#method for printing out cookies is living in a seperate Method that we defined.



"""
Keep in mind that like other variables python will let you override class variables without question.
So they can be modified from the class at will.
For example:

print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

Animal.counter = 35 # Overriding the variable from the class

print(Animal.counter) # Prints 35; since the attribute has been overridden
print(leopard_gecko.counter) # Prints 35; since the attribute has been overridden


Me - this is interesting below!
But if you try to modify a class variable from an instance, then it will create an instance variable 
that is now local to the instance while leaving the class variable in tact:

print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

Animal.counter = 35 # Overriding the variable from the class

print(Animal.counter) # Prints 35; since the attribute has been overridden

leopard_gecko.counter = 26 # creating an instance variable from the class attribute

print(Animal.counter) # Prints 35; since the class attribute WONT be modified by changing the gecko instance counter
print(leopard_gecko.counter) # Prints 26; since the instance attribute has been created

"""






#Dataclasses in Python
# If you are just storing variables there is also a useful module inside the Python standard library called dataclasses this
# library makes creating useful classes that just store data much faster.

# import datetime
# class user:
#   def __init__(self, name, age, sign_up_date, birthday, premium_member):
#     """A class to represent a generic animal

#     Attributes
#     ----------
#     name(str): The technical species name of the animal
#     age(str): A list of regions the animal is endemic to
#     sign_up_date(datetime.datetime): A datetime object of the day the user signed up
#     birthday(datetime.datetime): A datetime object of the users birthday
#     premium_member(bool): Whether the user is on premium or free subscription
#     """
#     self.name = name
#     self.age = age
#     self.sign_up_date = sign_up_date
#     self.birthday = birthday
#     self.premium_member = premium_member



"""
Now thats a lot of self.attribute_name's, dataclasses will automate the __init__ method (and __repr__ method).
"""
#instead of above we can import dataclass from dataclasses - inbuilt in Python
import datetime
from dataclasses import dataclass

@dataclass
class user:
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    name:str
    age:str
    sign_up_date:datetime.datetime
    birthday:datetime.datetime
    premium_member:bool
    
#shortcut - save time

user1 = user("john",69,datetime.date(1961, 4, 12),datetime.date(1961, 4, 12), True)
print(user1.name)




# SEE GLOSSARY IN NOTES - copied below
"""
Class: A template to create Instance(s)/Object(s) from.
Classes exist to bundle data (attributes) and functions (methods) into abstractions that are meaningful.
A good analogy is to think of a cookie cutter as a class, that is a template used 
to cut (instantiate) cookies (Instance(s)/Object(s))
For example you could have an Animal class that can be used to create Instance(s)/Object(s) to 
bundle data and functions about animals, or a user class that can be used to create Instance(s)/Object(s) to 
bundle data and functions about each user of an app.


Instance/Object: An object representing something, created from a class (used as a template).
A good analogy is to think of a cookie cutter as a class, that is a template used to cut (instantiate) 
cookies (Instance(s)/Object(s)).
For example if you had an Animal class, you could use it to instantiate a leopard gecko instance that has 
all the data (attributes) and 
functions (methods) necessary to represent a leopard gecko.
In Python people use Instance and Object interchangeably, and the same is true for many 
other object-oriented languages.


Instantiate: The act of creating (initialising) an Instance/Object from a class.
A good analogy is to think of a cookie cutter as a class, that is a template used to 
cut (instantiate) cookies (Instance(s)/Object(s))
Attribute: A variable that is specific to a class or Instance/Object.

Method: A function that is specific to a class or Instance/Object.

Constructor: What typically gets called on instantiation of an Instance/Object.
This is a concept used broadly in object-oriented languages, but in python this roughly 
corresponds to the __init__ method.
"""



#before proceed define each element in a class - know the lingo - __init__ what is this? etc



# Week 5 exercises - discussions are from last 30min of wk5 
