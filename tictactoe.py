from turtle import Turtle, Screen, onscreenclick, done
from helpers import Box, Victory, Machine, Best_move
import time
import math

# set up screen
win = Screen()
win.setup(1000, 800)
win.bgcolor("black")
win.title("Tic Tac Toe")


# Initialize variables
[a, b, c, d, e, f, g, h, i] = [Box(-200, 200), Box(0, 200), Box(200, 200), Box(-200, 0), Box(0, 0), Box(200, 0), Box(-200, -200), Box(0, -200), Box(200, -200)]
list = [a, b, c, d, e, f, g, h, i]
X = ([None, None, None], [None, None, None], [None, None, None,])
machine = Machine()
best_move = Best_move()

# reset game

def reset_game():
    win.resetscreen()
    global X
    global list
    global a, b, c, d, e, f, g, h, i
    global machine

    [a, b, c, d, e, f, g, h, i] = [Box(-200, 200), Box(0, 200), Box(200, 200), Box(-200, 0), Box(0, 0), Box(200, 0), Box(-200, -200), Box(0, -200), Box(200, -200)]
    list = [a, b, c, d, e, f, g, h, i]
    X = ([None, None, None], [None, None, None], [None, None, None,])
    Box.turn = "O"
    machine = Machine()

# def minimax algorithm
def minimax(X_t, turn_t):
    X_temp = ([None, None, None], [None, None, None], [None, None, None,])
    for i in range(3):
        for j in range(3):
            X_temp[i][j] = X_t[i][j]

    turn_temp = turn_t
    depth_temp = best_move.depth
    best_move.depth += 1

    # calculate moves left
    moves = []
    counter = 0
    for i in range(3):
        for j in range(3):
            if X_temp[i][j] == None:
                counter += 1
                moves.append([i, j])

    # base condition: if game is over, return score for the game

    res = win_condition(X_temp)
    if res[1] == True:
        if res[0] == "O":
            return 1
        if res[0] == "X":
            return -1
    if res[1] == "Draw":
        return 0

    if res[1] != True or res[1] != "Draw":

        # if turn is "O"
        if turn_temp == "O":
            value = -math.inf
            for move in moves:
                a, b = move[0], move[1]
                X_temp[a][b] = turn_temp
                value = max(value, minimax(X_temp, "X"))
                X_temp[a][b] = None

                #print("O move", a, b)
                #print("Ovalue", value)
                if depth_temp == 0:
                    if value > best_move.Ovalue:
                        best_move.Ovalue = value
                        best_move.Ox = a
                        best_move.Oy = b

                    #print(X_temp)
                    #print(best_move.Ovalue)
                    #print("O best move", a, b)

        # if turn is "X"
        if turn_temp == "X":
            value = math.inf
            for move in moves:
                a, b = move[0], move[1]
                X_temp[a][b] = turn_temp
                value = min(value, minimax(X_temp, "O"))
                X_temp[a][b] = None

                #print("Xmove", a, b)
                #print("Xvalue", value)
                if depth_temp == 0:
                    if value < best_move.Xvalue:
                        best_move.Xvalue = value
                        best_move.Xx = a
                        best_move.Xy = b

                    #print(X_temp)
                    #print(best_move.Xvalue)
                    #print("X best move", a, b)

    return value

# def win_condition
def win_condition(X_t):
    X_temp = ([None, None, None], [None, None, None], [None, None, None])
    for i in range(3):
        for j in range(3):
            X_temp[i][j] = X_t[i][j]
    # win
    # top left to bottom right
    if X_temp[0][0] == X_temp[1][1] and X_temp[1][1] == X_temp[2][2]:
        if X_temp[0][0] is not None:
            return [X_temp[0][0], True]

    # top right to bottom left
    if X_temp[0][2] == X_temp[1][1] and X_temp[1][1] == X_temp[2][0]:
        if X_temp[0][2] is not None:
            return [X_temp[0][2], True]

    for row in X_temp:
        if len(set(row)) == 1:
            if row[0] is not None:
                return [row[0], True]

    row = 0
    for column in range(3):
        if X_temp[row][column] == X_temp[row+1][column] and X_temp[row+1][column] == X_temp[row+2][column]:
            if X_temp[row][column] is not None:
                return [X_temp[row][column], True]

    counter = 0
    # check for draw
    for i in X_temp:
        for j in i:
            if j == None:
                counter += 1
    if counter == 0:
        return [None, "Draw"]

    else:
        # no victory yet
        return [None, False]

# main game loop, check for win condition
while True:
    counter = 0
    for i in range(3):
        for j in range(3):
            X[i][j] = list[counter].value
            counter += 1

    # When any of the boxes are clicked, assign value to box and draw cross/circle in box
    for i in list:
        i.onclick(i.clicked)

    # When machine box is clicked, activate minimax algorithm

    def z(*args):
        minimax(X, Box.turn)
        if Box.turn == "X":
            a, b = best_move.Xx, best_move.Xy
        elif Box.turn == "O":
            a, b = best_move.Ox, best_move.Oy
        if a == 0:
            c = a + b
        if a == 1:
            c = a + b + 2
        if a == 2:
            c = a + b + 4

        list[c].clicked(1,1)
        best_move.Xx = None
        best_move.Xy = None
        best_move.Ox = None
        best_move.Oy = None
        best_move.Xvalue = math.inf
        best_move.Ovalue = -math.inf
        best_move.depth = 0

    machine.onclick(z)

    # check win condition
    res = win_condition(X)
    if res[1] == True or res[1] == "Draw":
        Victory(res[0])
        reset_game()

done()
