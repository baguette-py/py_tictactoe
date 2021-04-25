from random import randint
import os

# display tic tac toe grid
def display_grid(grid, separator = '|'):
    for i in grid:
        line = ''
        for j in range(len(i)):
            line = line + f'{i[j]}' + separator            
        print(f'{line[:-1]}')

def add_in_grid(position, grid, symbol):
    try:
        x = int(position)
    except ValueError as error:
        return True, 'position is not integer', False
    if x > 9 or x < 1:
        return True, 'position is out of range', False
    # calculate positions
    i = int((int(x) - 0.1) / 3)
    j = int(x - (i * 3) - 1) 
    if not isinstance(grid[i][j], int):
        return True, 'case already used', False
    grid[i][j] = symbol
    return False, None, check_win(grid, symbol)

def get_available_position_on_grid(grid):
    # available positions
    p = []
    for i in grid:
        for j in i:
            if isinstance(j, int):
                p[len(p):] = [j]
    return p

def ia_play(grid, symbol):
    available_position = get_available_position_on_grid(grid)
    position = available_position[randint(0, len(available_position) - 1)]
    i = int((int(position) - 0.1) / 3) # calculate positions
    j = int(position - (i * 3) - 1) 
    grid[i][j] = symbol
    return check_win(grid, symbol)

def check_win(grid, symbol):
    win_condition = str(symbol + symbol + symbol)
    check_vertical = ['', '', '']
    check_diag = ['', '']
    # check vertical & horizontal
    for i in range(len(grid)):
        check_horizontal = str(grid[i][0]) + str(grid[i][1]) + str(grid[i][2])
        if check_horizontal == win_condition: return True
        check_vertical[0] = str(check_vertical[0]) + str(grid[i][0])
        check_vertical[1] = str(check_vertical[1]) + str(grid[i][1])
        check_vertical[2] = str(check_vertical[2]) + str(grid[i][2])
        check_diag[0] = str(check_diag[0]) + str(grid[i][0 + i])
        check_diag[1] = str(check_diag[0]) + str(grid[i][2 - i])
    for vertical in check_vertical: 
        if vertical == win_condition: return True
    for diag in check_diag: 
        if diag == win_condition: return True
    return False

def display_win_message(grid, message):
    os.system('cls')
    display_grid(grid)
    print(f'{message}')

# start
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
win, stop = False, False

while not win and not stop:
    os.system('cls')
    display_grid(grid)
    position = input(':')
    if position == 'exit': # check for exit
        stop = True
    if position == '': continue
    (error, text, pwin) = add_in_grid(position, grid, 'o')
    if error:
        print(f'{text}')
    elif not error and not pwin:
        iawin = ia_play(grid, 'x')
        if iawin:
            display_win_message(grid, 'vous avez perdu!')
            stop = True
    else:
        display_win_message(grid, 'vous avez gagné')
        win = True