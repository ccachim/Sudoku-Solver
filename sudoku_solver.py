#imports necessarios para mypy
from typing import TypedDict
from typing import List, Set, Dict, Tuple, Optional
from xmlrpc.client import boolean

my_board =[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board:List[List[int]]):
    for i in board:
        print(i)

def find_empty_cell(board:List[List[int]])->tuple:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) # linha coluna
    return None

def check_valid(board:List[List[int]], number:int, position:tuple)->boolean:
    linha: int = position[0]
    coluna: int = position[1]
    caixa_y = linha // 3
    caixa_x = coluna // 3

    # Verificar linha
    for i in range(9):
        if board[linha][i] == number and coluna != i:
            return False

    # Verificar coluna
    for i in range(len(board)):
        if board[i][coluna] == number and linha != i:
            return False

    # Verificar caixa
    for i in range(caixa_y*3, caixa_y*3+3):
        for j in range(caixa_x*3, caixa_x*3+3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

#recursive algorithm
def solve(board:List[List[int]])->boolean:
    #base case
    position:tuple = find_empty_cell(board)
    if position == None:
        return True

    else:
        linha: int = position[0]
        coluna: int = position[1]
        for i in range(9):
            if check_valid(board, i+1, (linha, coluna)):
                board[linha][coluna] = i+1
                if solve(board):
                    return True
                else:
                    board[linha][coluna] = 0
    return False



print_board(my_board)
solve(my_board)
print("___________________________\n")
print_board(my_board)
