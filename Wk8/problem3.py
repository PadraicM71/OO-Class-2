


def ask():
    while True:
        try:
         num1 = int(input("Please enter an integer: "))
        except:
           print("Looks like you did not enter an integer!")
           continue
        else:
            print("The square is: ")
            print(num1 * num1)
            break

        finally:
            print("OK!")
          
ask()


