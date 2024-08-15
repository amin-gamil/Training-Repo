import pygame
from pygame.locals import *

pygame.init()

screen_size = (650, 650)
(width, height) = screen_size
screen = pygame.display.set_mode(screen_size)
pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wK', 'wB', 'wQ', 'wN', 'wP']
OBJ = {}
for i in pieces:
    OBJ[i] = pygame.transform.smoothscale(pygame.image.load(f'pieces-basic-png/{i}.png'), (width / 8, height / 8))
player = 1

# color_piece = pygame.image.load('pieces-basic-png/black-bishop.png')
# black_bishop = pygame.image.load('pieces-basic-png/black-bishop.png')
# black_bishop = pygame.transform.smoothscale(black_bishop, (width / 8, height / 8))


def grid():
    light = (177, 228, 185)
    dark = (112, 162, 163)
    screen.fill(light)
    for j in range(0, 9, 2):
        for i in range(1, 9, 2):
            rectobj = Rect(i * width / 8, j * width / 8, width / 8, width / 8)
            screen.fill(dark, rectobj)
        for k in range(0, 9, 2):
            rectobj = Rect(k * width / 8, (j + 1) * width / 8, width / 8, width / 8)
            screen.fill(dark, rectobj)


# pieces_arr = {
#     'black_rook1': [1, 1, black_rook],
#     'black_knight1': [2, 1, black_knight],
#     'black_bishop1': [3, 1, black_bishop],
#     'black_queen': [4, 1, black_queen],
#     'black_king': [5, 1, black_king],
#     'black_bishop2': [6, 1, black_bishop],
#     'black_knight2': [7, 1, black_knight],
#     'black_rook2': [8, 1, black_rook],
#     'black_pawn1': [1, 2, black_pawn],
#     'black_pawn2': [2, 2, black_pawn],
#     'black_pawn3': [3, 2, black_pawn],
#     'black_pawn4': [4, 2, black_pawn],
#     'black_pawn5': [5, 2, black_pawn],
#     'black_pawn6': [6, 2, black_pawn],
#     'black_pawn7': [7, 2, black_pawn],
#     'black_pawn8': [8, 2, black_pawn],
#     'white_rook1': [1, 8, white_rook],
#     'white_knight1': [2, 8, white_knight],
#     'white_bishop1': [3, 8, white_bishop],
#     'white_queen': [4, 8, white_queen],
#     'white_king': [5, 8, white_king],
#     'white_bishop2': [6, 8, white_bishop],
#     'white_knight2': [7, 8, white_knight],
#     'white_rook2': [8, 8, white_rook],
#     'white_pawn1': [1, 7, white_pawn],
#     'white_pawn2': [2, 7, white_pawn],
#     'white_pawn3': [3, 7, white_pawn],
#     'white_pawn4': [4, 7, white_pawn],
#     'white_pawn5': [5, 7, white_pawn],
#     'white_pawn6': [6, 7, white_pawn],
#     'white_pawn7': [7, 7, white_pawn],
#     'white_pawn8': [8, 7, white_pawn],
#
# }

board_arr = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
    ]

def moves(r2,c2,r1,c1):
    allowed=[]
    if board_arr[r1][c1]!='--':
        if board_arr[r1][c1][0]=='w' and player == 1:
            if board_arr[r1][c1][1]=='P':           ## White Pawn moves
                if board_arr[r1-1][c1]=='--':
                    allowed.append([r1-1,c1])
                if board_arr[r1-2][c1]=='--' and r1 == 6:
                    allowed.append([r1-2,c1])
    return allowed

def draw_pieces():
    for j in range(8):
        for i in range(8):
            e = board_arr[j][i]
            if e != '--':
                screen.blit(OBJ[e], (i*width/8, j*height/8))

print(board_arr)
run = True
clicks=[]
while run:
    grid()
    draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            col = int(loc[0]//(width/8))
            row = int(loc[1]//(width/8))
            clicks.append(col)
            clicks.append(row)
        if len(clicks) == 4:
            print(clicks)
            if (clicks[3],clicks[2])  in [moves(clicks[3],clicks[2],clicks[1],clicks[0])]:
                board_arr[clicks[3]][clicks[2]] = board_arr[clicks[1]][clicks[0]]
                board_arr[clicks[1]][clicks[0]] = "--"
        clicks = []

    pygame.display.update()

pygame.quit()














