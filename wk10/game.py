

# game_list = [0,1,2]

# def display_game(game_list):
#     print("Here is the current list")
#     print(game_list)

# display_game(game_list)


#-----------------------------------------------

from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def display_game(game_list):
    print("Here is the current list")
    print(game_list)
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in['0','1','2']:
            clear()
            print("Sorry, but you did not choose a valid position (0,1,2): ")
    return int(choice)
def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement
    return game_list
def gameon_choice():
    choice = "wrong"
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','N']:
            clear()
            print("Sorry, I didn't understand. Please make sure to choose Y or N. ")
    if choice == "Y":
        return True
    else:
        return False
game_on = True
game_list = [0,1,2]
while game_on:
    clear()
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    clear()
    display_game(game_list)
    game_on = gameon_choice()


#-----------------------------------------------