#`````````````````````````````
#
#    Developed by Ivan Seagull
#
#`````````````````````````````


#In this project I learned how to use backtacking algorithm

#   Steps to solve sudoku
#    1. Pick empty 
#    2.Try all numbers
#    3. Find one that fits
#    4. Repeat w/ the next one
#    5. If doesnt work, backtrack


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]


def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col]=i

            if solve(board):
                return True
            
            board[row][col]=0

    return False



def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True



def printingBoard(board):
    for i in range(len(board)):
        if i % 3 ==0 and i !=0:
            print("- - - - - - - - - - - - - - ")
        for j in range(len(board[i])):
            if j % 3 ==0 and j!=0:
                print(" | ", end='')

            if j== 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')
    print()


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #rol, col
    return None


printingBoard(board)
solve(board)
print('\n')
printingBoard(board)
