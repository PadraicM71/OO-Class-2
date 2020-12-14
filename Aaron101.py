# AAron's Stuff





#test


print ("hello Aaron") 

number = int(input("Please type a number Aaron: "))
x = 2
while True:
  num1 = (number%x)
 # print (num1)

  if x == number:
    print("Number is prime Aaron")
    break

  elif num1 == 0:
    print("Number is composite Aaron")
    print("It is dividible by " + str(x))
    break

  else:
    x += 1
