

game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list")
    print(game_list)

display_game(game_list)

#------------------------------------------

from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list")
    print(game_list)
display_game(game_list)
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in['0','1','2']:
            clear()
            print("Sorry, but you did not choose a valid position (0,1,2)")
    return int(choice)



#-----------------------------------------------