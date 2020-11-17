# Wk 7


# print('Hello)


# try:
#     f = open('testfile','r')
#     f.write('Test write this')
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()


# try:
#     f = open("testfile", "r")
#     f.write("Test write statement")
#     f.close()
# finally:
#     print("Always execute finally code blocks")


# def askint():
#     while True:
#         try:
#          val = int(input("Please enter an integer: "))
#         except:
#            print("Looks like you did not enter an integer!")
#            continue
#         else:
#             print("Yep, thats an integer ")
#             print(val)
#             break

#         finally:
#             print("Finally, I executed!")
          

# askint()

# %%writefile simple1.py
# a = 1
# b = 2
# print(a)
# print(B)



# #%%writefile simple1.py
# """
# A very simple script.
# """

# def myfunc():
#     """
#     An extremely simple function.
#     """
#     first = 1
#     second = 2
#     print(first)
#     print(second)

# myfunc()


def cap_text(text):
    return text.capitalize()

    