# 4.1
# We are playing bingo, given a list of numbers called and boards, determine what board will be have the first bingo

import numpy as np
calledNumbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

board1 = [
    [22, 13, 17, 11,  0],
    [8,  2, 23,  4, 24],
    [21,  9, 14, 16,  7],
    [6, 10,  3, 18,  5],
    [1, 12, 20, 15, 19],
]

board2 = [
    [3, 15,  0,  2, 22],
    [9, 18, 13, 17,  5],
    [19,  8,  7, 25, 23],
    [20, 11, 10, 24,  4],
    [14, 21, 16, 12,  6],
]

board3 = [
    [14, 21, 17, 24,  4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7]
]

boards = [board1, board2, board3]

boardHorizontal = [
    [14, 21, 17, 24,  4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    ["x", "x", "x", "x", "x"]
]

boardVertical = [
    ["x", 21, 17, 24,  4],
    ["x", 16, 15, 9, 19],
    ["x", 8, 23, 26, 20],
    ["x", 11, 13, 6, 5],
    ["x", 12, 25, 43, 1]
]

boardRight = [
    ["x", 21, 17, 24,  4],
    [16, "x", 15, 9, 19],
    [1, 8, "x", 26, 20],
    [2, 11, 13, "x", 5],
    [9, 12, 25, 43, "x"]
]

boardLeft = [
    [19, 37, 17, 24, "x"],
    [16, 34, 15, "x", 19],
    [1, 8, "x", 26, 20],
    [2, "x", 13, 14, 5],
    ["x", 12, 25, 43, 16]
]

#for number in calledNumbers[0]:

def checkBingo(board):
    boardTranspose = np.array(board).T.tolist()
    yell = ""
    for x in board:
        if x == ["x", "x", "x", "x", "x"]:
            yell = "Bingo"
    for y in boardTranspose:
        if y == ["x", "x", "x", "x", "x"]:
            yell = "Bingo"
    # if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x" and board[3][3] == "x" and board[4][4] == "x":
    #     yell = "Bingo"
    # if board[4][0] == "x" and board[3][1] == "x" and board[2][2] == "x" and board[1][3] == "x" and board[0][4] == "x":
    #     yell = "Bingo"
    return yell

def callNumber(number, board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == number:
                board[x][y] = "x"
    return board

def numberGenerator(finalNum, board):
    sum = 0 
    for x in range(len(board)):
        for y in range(len(board[x])):
            if isinstance(board[x][y], int):
                sum += board[x][y]
    print(sum * finalNum)


def solution1a():
    while True:
        for number in calledNumbers:
            for board in boards:
                if checkBingo(callNumber(number, board)) == "Bingo":
                    numberGenerator(number, board)
                    return False       
def solution1b():
    boards = []
    calledNumbers = []
    bigList = []
    with open("4.txt") as f:
        for line in f:
            bigList.append(line.strip())

    for el in bigList[0].split(","):
        try:
            calledNumbers.append(int(el))
        except ValueError:
            pass
    #for x in calledNumbers:
        #print(x)
    del bigList[0]

    filteredList = []
    for x in bigList:
        if x != "":
            filteredList.append(x)
    board = []

    for x, i in enumerate(filteredList):
        x = x + 1
        
        daList = i.split(" ")
        daList = list(filter(lambda x: x != "", daList))
        daList = list(map(int, daList))

        if x % 5 == 0:
            board.append(daList)
            boards.append(board)
            board = []
        else:
            board.append(daList)
    
    while True:
        for number in calledNumbers:
            for board in boards:
                if checkBingo(callNumber(number, board)) == "Bingo":
                    numberGenerator(number, board)
                    return False   
    
#solution1a()
#solution1b()

def solution2a():
    winnersList = []
    winnerNumbers = []
    x = 0
    while x < len(calledNumbers[:]):
        i = 0
        while i < len(boards):
            callNumber(calledNumbers[x], boards[i])
            if checkBingo(boards[i]) == "Bingo":
                winnersList.append(boards[i])
                winnerNumbers.append(calledNumbers[x])
                del boards[i]
            else:
                i += 1
        x += 1
    numberGenerator(winnerNumbers[-1], winnersList[-1])
    
# solution2a()

def solution2b():
    boards = []
    calledNumbers = []
    bigList = []
    with open("4.txt") as f:
        for line in f:
            bigList.append(line.strip())

    for el in bigList[0].split(","):
        try:
            calledNumbers.append(int(el))
        except ValueError:
            pass
    #for x in calledNumbers:
        #print(x)
    del bigList[0]

    filteredList = []
    for x in bigList:
        if x != "":
            filteredList.append(x)
    board = []

    for x, i in enumerate(filteredList):
        x = x + 1
        
        daList = i.split(" ")
        daList = list(filter(lambda x: x != "", daList))
        daList = list(map(int, daList))

        if x % 5 == 0:
            board.append(daList)
            boards.append(board)
            board = []
        else:
            board.append(daList)
    
    winnersList = []
    winnerNumbers = []
    x = 0
    while x < len(calledNumbers[:]):
        i = 0
        while i < len(boards):
            callNumber(calledNumbers[x], boards[i])
            if checkBingo(boards[i]) == "Bingo":
                winnersList.append(boards[i])
                winnerNumbers.append(calledNumbers[x])
                del boards[i]
            else:
                i += 1
        x += 1
    numberGenerator(winnerNumbers[-1], winnersList[-1])

solution2b()