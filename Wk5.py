# Wk 5


# name = "John Doe"
# greeting = f"Welcome, {name}!"
# print(greeting) # Prints: Welcome John Doe!

# name = "John Doe"
# greeting = f"Welcome, {name}!"
# name = "Kieran Wood"
# print(greeting) # Prints: Welcome John Doe!
# greeting = f"Welcome, {name}!" # Since it's recreated it picks up the new value of name
# print(greeting) # Prints: Welcome Kieran Wood!


# Dates

import datetime

# appolo_11_launch = datetime.date(1959, 9, 13)

# falcon_9_first_launch = datetime.date(2010, 6, 4)

# print(falcon_9_first_launch > appolo_11_launch) # prints: True
# print(falcon_9_first_launch.month)

# import datetime

# appolo_11_launch = datetime.date(1959, 9, 13)

# appolo_11_launch.year # prints: 1959

# appolo_11_launch.month # Prints: 9

# appolo_11_launch.day # Prints: 13

# import datetime

# current_datetime = datetime.date.today() # Returns datetime object of todays date

# print(current_datetime)


# class Animal:
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
    
#   def print_info(self):
#     """Prints information about animal instance"""
#     print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")

# leopard_gecko = Animal("Eublepharis macularius", ["Afghanistan","Pakistan","India", "Iran"],"Common Leopard Gecko")

# """Prints (not returns)
# Common Name: Common Leopard Gecko
# Species: Eublepharis macularius
# Regions: ['Afghanistan','Pakistan','India', 'Iran']
# """
# leopard_gecko.print_info()

# leopard_gecko = Animal("Eublepharis macularius",["Afghanistan","Pakistan","India", "Iran"],"Common Leopard Gecko")

# print(leopard_gecko.common_name)





# class CookieBaker:
#   def __init__(self, number_of_cookies):
#     """ Example class that is used to show off the __init__ method.
#     The __init__ method calls prints 'Cookie Baked' as many times as there are number_of_cookies.

#     Attributes
#     ----------
#     number_of_cookies(int): How many cookies to bake
#     """
#     print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
#     self.number_of_cookies = number_of_cookies
#     for cookie in range(number_of_cookies):
#       print("Cookie Baked!")



# CookieBaker(5)









import datetime
class user:
  def __init__(self, name, age, sign_up_date, birthday, premium_member):
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    self.name = name
    self.age = age
    self.sign_up_date = sign_up_date
    self.birthday = birthday
    self.premium_member = premium_member


    

