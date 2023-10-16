# This's an Application for a Tic Tac Toe Game. It's part of the 100 days of Code Course.
""""
Program Parts:
1-Visual List: I used python Tutor to better visualize the nested loop
2-Winning / Losing function (Winning Condition: all 3 function are full & total is 1 or 0
"""


# Winning function
def winning_func(passed_list):
    """Check the game's lines, columns, diagonals if they're X or O for winning condition"""
    global is_game_off
    if (passed_list[0] == passed_list[1] == passed_list[2] == "X"
            or passed_list[3] == passed_list[4] == passed_list[5] == "X"
            or passed_list[6] == passed_list[7] == passed_list[8] == "X"
            or passed_list[0] == passed_list[4] == passed_list[8] == "X"
            or passed_list[2] == passed_list[4] == passed_list[6] == "X"
            or passed_list[0] == passed_list[3] == passed_list[6] == "X"
            or passed_list[1] == passed_list[4] == passed_list[7] == "X"
            or passed_list[2] == passed_list[6] == passed_list[8] == "X"
    ):
        print("\nPlayer 1 Won")
        is_game_off = True
    elif (passed_list[0] == passed_list[1] == passed_list[2] == "O"
          or passed_list[3] == passed_list[4] == passed_list[5] == "O"
          or passed_list[6] == passed_list[7] == passed_list[8] == "O"
          or passed_list[0] == passed_list[4] == passed_list[8] == "O"
          or passed_list[2] == passed_list[4] == passed_list[6] == "O"
          or passed_list[0] == passed_list[3] == passed_list[6] == "O"
          or passed_list[1] == passed_list[4] == passed_list[7] == "O"
          or passed_list[2] == passed_list[6] == passed_list[8] == "O"
    ):
        print("\nPlayer 2 Won")
        is_game_off = True


# input function.
def input_check(user_input, player_num):
    """" Take the user input, and player number 1 or 2 to represent X or O respectively."""
    global new_list
    input_incorrect = True
    while input_incorrect:
        if 1 <= user_input <= 9:
            if new_list[user_input - 1] != "X" and new_list[user_input - 1] != "O":
                input_incorrect = False
                if player_num == 1:
                    new_list[user_input - 1] = "X"
                    print_loop(new_list)
                elif player_num == 2:
                    new_list[user_input - 1] = "O"
                    print_loop(new_list)
            else:
                num = int(input(f"That square is already occupied. Player {player_num}, Enter a new number: "))
                input_check(num, player_num)
                input_incorrect = False
        else:
            num = int(input(f"Please enter a valid number between 1 and 9. Player {player_num}, try again"))
            input_check(num, player_num)
            input_incorrect = False


# Checking if all spaces are empty:
def check_spaces(passed_list):
    """"A function that checks if all the spots in the list/grid are full or not. Return false for grid with
    available space, and True for full grid"""
    list_checker = False
    for x in passed_list:
        if x == " ":
            list_checker = True
    return list_checker


# printing Loop
def print_loop(passed_list):
    """"Prints the passed list as a 3x3 matrix with dividers between cells and rows"""
    counter = 0
    for i in range(3):
        for j in range(3):
            print(f"{passed_list[counter]}", end="")
            if j == 0 or j == 1:
                print(" | ", end="")
            counter += 1
        if i == 0 or i == 1:
            print("\n-----------")


# Welcome Message
print("Welcome to our special Tic Tac Toe. Try your best and beat your friends")
print("For our game, you just need to enter the number of the square you want to fill")
print("Here's a visual presentation")
demo_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print_loop(demo_list)

# Main game loop
is_game_off = False
#This list is to keep the players input and to be printed
new_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while not is_game_off:
    if check_spaces(new_list):
        user1 = int(input("\nPlayer 1 is 'X'. Enter the position of the cell: "))
        input_check(user1, 1)
        winning_func(new_list)
        if not is_game_off:
            if check_spaces(new_list):
                user2 = int(input("\nPlayer 2 is 'O'. Enter the position of the cell: "))
                input_check(user2, 2)
                winning_func(new_list)
    else:
        print("\nGame is Draw")
        is_game_off = True
