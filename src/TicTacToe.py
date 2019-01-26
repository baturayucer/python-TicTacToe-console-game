#python TicTacToe game

dod = ' '
move = 0
maxMoveNumber = 9
winFlag = False
turnFlag = 1
move = 0
clear = "\n" * 100

matrix = [['| |' for a in range(3)] for b in range(3)]
print("Game is starting...")
print("    1   2   3  ")


for k in range(3):

    for l in range(3):
        if l==0:
            print(f"{k+1} ", matrix[k][l], end=" ")
        else:
            print(matrix[k][l], end=" ")
    print(" ")
print(" ")


def restart():

    global dod
    global move
    global maxMoveNumber
    global winFlag
    global turnFlag
    global matrix
    dod = ' '
    move = 0
    maxMoveNumber = 9
    winFlag = False
    turnFlag = 1
    move = 0

    print(clear)

    matrix = [['| |' for a in range(3)] for b in range(3)]
    print("Game is starting...")
    print("    1   2   3  ")

    for k in range(3):

        for l in range(3):
            if l == 0:
                print(f"{k + 1} ", matrix[k][l], end=" ")
            else:
                print(matrix[k][l], end=" ")
        print(" ")
    print(" ")


def change(turn):
    if turn == 1:
        return 2
    elif turn == 2:
        return 1


def inputCheck():
    global move
    global turnFlag
    global dod
    try:
        if matrix[int(dod[0]) - 1][int(dod[1]) - 1] == '| |':
            if turnFlag == 1:
                matrix[int(dod[0]) - 1][int(dod[1]) - 1] = '|X|'
                turnFlag = change(turnFlag)
                move = move + 1
            else:
                matrix[int(dod[0]) - 1][int(dod[1]) - 1] = '|O|'
                turnFlag = change(turnFlag)
                move = move + 1
        else:
            print('This move has been played already!')
        print("    1   2   3  ")
        for k in range(3):
            print(" ")
            for l in range(3):
                if l == 0:
                    print(f"{k + 1} ", matrix[k][l], end=" ")
                else:
                    print(matrix[k][l], end=" ")
        print(" ")
        print(" ")
        print(f"Move:{move}")

    except Exception:
        print("Invalid input")

def wincheck():
    global winFlag
    global matrix
    global turnFlag
    for counter in range(3):
        if matrix[counter] == ['|X|', '|X|', '|X|'] or matrix[counter] == ['|O|', '|O|', '|O|']:
            print(f"game over. Player{change(turnFlag)} wins")
            winFlag = True
            break
        elif (matrix[0][counter] == matrix[1][counter] == matrix[2][counter]) and matrix[0][counter] != '| |':
            print(f"game over. Player{change(turnFlag)} wins")
            winFlag = True
            break
    if (matrix[0][0] == matrix[1][1] == matrix[2][2]) and matrix[0][0] != '| |':
        print(f"game over. Player{change(turnFlag)} wins")
        winFlag = True

    elif (matrix[0][2] == matrix[1][1] == matrix[2][0]) and matrix[0][2] != '| |':
        print(f"game over. Player{change(turnFlag)} wins")
        winFlag = True


# game
def getreplaychoice():
    res = input(f'Would you like to play again?(y,n)')
    if res == 'y':
        return 'yes'
    elif res == 'n':
        return 'no'
    else:
        print("invalid input")
        getreplaychoice()


while move < maxMoveNumber:

    if winFlag == True:
        ans = getreplaychoice()
        if ans == 'yes':
            restart()
        else:
            break

    dod = input(f'Coordination for Player:{turnFlag}(x,y)')
    dod = dod.split(',')
    print(" ")

    inputCheck()

    wincheck()
