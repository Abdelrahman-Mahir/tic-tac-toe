# This's an Application for a Tic Tac Toe Game. It's part of the 100 days of Code Course.
""""
Program Parts:
1-Visual List: I used python Tutor to better visualize the nested loop
2-Winning / Losing function (Winning Condition: all 3 function are full & total is 1 or 0
"""


# Winning function
def winning_func(passed_list):
    global is_game_off
    if (passed_list[0] == passed_list[1] == passed_list[2] == "X"
            or passed_list[3] == passed_list[4] == passed_list[5] == "X"
            or passed_list[6] == passed_list[7] == passed_list[8] == "X"
            or passed_list[0] == passed_list[4] == passed_list[8] == "X"
            or passed_list[2] == passed_list[4] == passed_list[6] == "X"):
        print("\nPlayer 1 Won")
        is_game_off = True
    elif (passed_list[0] == passed_list[1] == passed_list[2] == "O"
          or passed_list[3] == passed_list[4] == passed_list[5] == "O"
          or passed_list[6] == passed_list[7] == passed_list[8] == "O"
          or passed_list[0] == passed_list[4] == passed_list[8] == "O"
          or passed_list[2] == passed_list[4] == passed_list[6] == "O"):
        print("\nPlayer 2 Won")
        is_game_off = True


# input function.
def input_check(user_input, player_num):
    """" Take the user input, and player number 1 or 2 to represent X or O respectively."""
    global new_list
    if 1 <= user_input <= 9:
        if new_list[user_input - 1] != 1 and new_list[user_input - 1] != 0:
            if player_num == 1:
                new_list[user_input - 1] = "X"
            elif player_num == 2:
                new_list[user_input - 1] = "O"
        else:

    print_loop(new_list)


# Visual Part
gaming_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# printing Loop
def print_loop(passed_list):
    counter = 0
    for i in range(3):
        for j in range(3):
            print(f"{passed_list[counter]}", end="")
            if j == 0 or j == 1:
                print(" | ", end="")
            counter += 1
        if i == 0 or i == 1:
            print("\n-----------")


# main game loop
# Welcome Message
print("Welcome to our special Tic Tac Toe. Try your best and beat your friends")
print("For our game, you just need to enter the number of the square you want to fill")
print("Here's a visual presentation")
print_loop(gaming_list)

is_game_off = False
new_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while not is_game_off:
    user1 = int(input("\nPlayer 1 is 'X'. Enter the position of the cell: "))
    input_check(user1, 1)
    winning_func(new_list)
    user2 = int(input("\nPlayer 2 is 'O'. Enter the position of the cell: "))
    input_check(user2, 2)
    winning_func(new_list)
