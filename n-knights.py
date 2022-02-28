
import math


def getCombosList(totalArr, choose):
    allCombos = []
    def getCombos(totalArr, choose, acc):
        if (choose == 0):
            allCombos.append(acc)
            return
        for num in range(len(totalArr)-choose+1):
            copyAcc = acc[:]
            copyAcc.append(totalArr[num])
            getCombos(totalArr[num+1:], choose-1, copyAcc)
    getCombos(totalArr, choose, [])
    return allCombos

def createPositionArray(n):
    board = []
    for i in range(n*n):
        board.append(i)
    return board

def createBoard(positionArray, n):
    board = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        board.append(row)
    for i in positionArray:
        col = (i % n) 
        row = int(math.floor(i/n))
        board[row][col] = 1
    return board

def isValidBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                if i-2 >= 0:
                    if j-1 >= 0 and board[i-2][j-1]==1:
                        return False
                    if j+1 < len(board) and board[i-2][j+1]==1:
                        return False
                if i-1 >= 0:
                    if j-2 >= 0 and board[i-1][j-2] == 1:
                        return False
                    if j-1 >= 0 and board[i-1][j-2] == 1:
                        return False
                if i+1 < len(board):
                    if j+2 < len(board) and board[i+1][j+2] == 1:
                        return False
                    if j-2 >= 0 and board[i+1][j-2] == 1:
                        return False
                if i+2 < len(board):
                    if j+1 < len(board) and board[i+1][j+1] == 1:
                        return False
                    if j-1 >= 0 and board[i+1][j-1] == 1:
                        return False
                    

    return True


def main(n, knights):
    boardList = createPositionArray(n)
    combos = getCombosList(boardList, knights)

    validCount = 0
    for combo in combos:
        board = createBoard(combo, n)
        if isValidBoard(board):
            validCount += 1
    print(validCount)
        

main(4, 9)