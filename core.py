#wk6 class demo


def greeting(name):
    print("Hello " + name)


from tqdm import tqdm
from time import sleep


#define our function - starts with def

def calc(num_1,num_2):
    """Multiplies 2 numbers and subtracts 20"""
    result = num_1 * num_2
    result -= 20
    return result


# def iterate(amount = 40):
#     for number in tqdm(range(0,amount)):
#         sleep(.5)

