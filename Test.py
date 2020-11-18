# #Test File


# class MyClass:
#     x=5

# p1 = MyClass()
# print (p1.x)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class People:
#     count = 0
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
#         People.count += 1
#     def myfunc(self):
#         print("hello there " + "\nyour name is " + "\n" + self.name)



# print (People.count)

# k1 = People("qwerrty", 36)
# print (People.count)
# k2 = People("joe", 45)
# print (People.count)
# k3 = People("john", 56)

# print (People.count)

# print(k1.name)
# k1.myfunc()

#----------------------------------------------------------
#-------------Prime Numbers Project------------------------

number = int(input("Please type a number Callum: "))
x = 2
while True:
  num1 = (number%x)
 # print (num1) used to debug initally

  if x == number:
    print("Number is prime Callum")
    break

  elif num1 == 0:
    print("Number is composite Callum")
    print("It is dividible by " + str(x))
    break

  else:
    x += 1

 #---------------------------------------------------------

