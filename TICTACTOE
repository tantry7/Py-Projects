#created on 19|4|19 lol 
#author - narayanatantry


# print the board
def play_board(board):
    print("\n"*10)
    print(     board[7] +    "   |  " + board[8] + "  |  " + board[9])
    print("----"  + "|" + "-----"  + "|" + "-----" )
    print(     board[4] +    "   |  " + board[5] + "  |  " + board[6])
    print("----"  + "|" + "-----"  + "|" + "-----" )
    print(     board[1]  +    "   |  " + board[2] + "  |  " + board[3])
    print("----"  + "|" + "-----"  + "|" + "-----" )

boardy = [" "]*10


# now we need to take the user input and place it on the board aka boardy
def player_input():
    marker = " "
    while marker !="x" and marker !="o":
        marker = str(input("player1, choose X or O: "))
    if marker == "x":
        return ("X","O")
    else:
        return ("O","X")


def marker_place(board, marker, postion):
    board[postion] = marker


# check if there is a winner
def check_win(board,marker):
    # acroos wins
        if (board[1] == board[2] == board[3] == marker) or \
                (board[4] == board[5] == board[6] == marker) or \
                (board[7] == board[8] == board[9] == marker) or \
                (board[3] == board[6] == board[9] == marker) or \
                (board[2] == board[5] == board[8] == marker) or \
                (board[1] == board[4] == board[7] == marker) or \
                (board[1] == board[5] == board[9] == marker) or \
                (board[3] == board[5] == board[7] == marker):
            return True
        else:
            return False


import random
def starter():
    go = random.randint(0,1)
    if go == 0:
        return "player 1"
    else:
        return "player 2"


def space_check(board, postion):
    return board[postion] == " "


def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True




def ask_input(board):
    postion = 0
    while postion not in range(1,10) or not space_check(board,postion):
        postion = int(input("choose position (1-9): "))
    return postion



def replay():
    result = str(input("play again? (yes - no): "))
    return result == "yes"
    





def lets_play():
    global boardy
    player1,player2 = player_input()
    while True:
        play_ = str(input("Ready to play? Enter yes or no: "))
        if play_ == "yes":
            play_ = True
        else:
            play_ = False
        turns = starter()
        print(f" {turns} will go first")
        while play_:
            if turns == "player 1":
                play_board(boardy)
                position = ask_input(boardy)
                marker_place(boardy, player1, position)
                if check_win(boardy, player1):
                    play_board(boardy)
                    print("player1 has won")
                    play_ = False
                else:
                    if full_board(boardy):
                        play_board(boardy)
                        print("Tie Game !")
                        play_ = False
                    else:
                        turns = "player 2"

            else:
                play_board(boardy)
                position = ask_input(boardy)
                marker_place(boardy, player2, position)
                if check_win(boardy, player2):
                    play_board(boardy)
                    print("player2 has won")
                    play_ = False
                else:
                    if full_board(boardy):
                        play_board(boardy)
                        print("Tie Game !")
                        play_ = False
                    else:
                        turns = "player 1"
        if not replay():
            break
print(lets_play())

# problems: 1.Replay
            2.player's names

