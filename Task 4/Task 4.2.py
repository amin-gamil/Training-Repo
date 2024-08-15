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


def moves(r2, c2, r1, c1):
    allowed = []
    if board_arr[r1][c1] != '--':
        # The square is not empty
        if board_arr[r1][c1][0] == 'w' and player == 1:  #White piece in white's turn
            if board_arr[r1][c1][1] == 'P':  ## White Pawn moves

                if board_arr[r1 - 1][c1] == '--':
                    allowed.append([r1 - 1, c1])
                    if board_arr[r1 - 2][c1] == '--' and r1 == 6:
                        allowed.append([r1 - 2, c1])
                if board_arr[r1 - 1][c1 - 1][0] == 'b':
                    allowed.append([r1 - 1, c1 - 1])
                if c1 + 1 <= 7:
                    if board_arr[r1 - 1][c1 + 1][0] == 'b':
                        allowed.append([r1 - 1, c1 + 1])
        if board_arr[r1][c1][0] == 'b' and player == -1:
            if board_arr[r1][c1][1] == 'P':  ## Black Pawn moves
                if r1 + 1 <= 7:  # Prevents 'out of range' errors
                    if board_arr[r1 + 1][c1] == '--':
                        allowed.append([r1 + 1, c1])
                        if r1 == 1 and board_arr[r1 + 2][c1] == '--':
                            allowed.append([r1 + 2, c1])

                    if board_arr[r1 + 1][c1 - 1][0] == 'w':
                        allowed.append([r1 + 1, c1 - 1])
                    if c1 + 1 <= 7:
                        if board_arr[r1 + 1][c1 + 1][0] == 'w':
                            allowed.append([r1 + 1, c1 + 1])
        if board_arr[r1][c1][1] == 'R' or board_arr[r1][c1][1] == 'Q':  #Rook's moves which also applies to Queen
            ally = board_arr[r1][c1][0]
            if (player == 1 and ally == 'w') or (player == -1 and ally == 'b'):
                ally = board_arr[r1][c1][0]
                enemy = 'w' if ally == 'b' else 'b'
                for i in range(1, 8):  ## Moving up the board
                    if board_arr[r1 - i][c1] == '--':
                        allowed.append([r1 - i, c1])
                    elif board_arr[r1 - i][c1][0] == ally:
                        break
                    elif board_arr[r1 - i][c1][0] == enemy:
                        allowed.append([r1 - i, c1])
                        break
                for i in range(1, 8):  ## Moving down the board
                    if r1 + i <= 7:
                        if board_arr[r1 + i][c1] == '--':
                            allowed.append([r1 + i, c1])
                        elif board_arr[r1 + i][c1][0] == ally:
                            break
                        elif board_arr[r1 + i][c1][0] == enemy:
                            allowed.append([r1 + i, c1])
                            break
                for i in range(1, 8):  ## Moving left
                    if c1 - i >= 0:
                        if board_arr[r1][c1 - i] == '--':
                            allowed.append([r1, c1 - i])
                        elif board_arr[r1][c1 - i][0] == ally:
                            break
                        elif board_arr[r1][c1 - i][0] == enemy:
                            allowed.append([r1, c1 - i])
                            break
                for i in range(1, 8):  ## Moving Right
                    if c1 + i < 8:
                        if board_arr[r1][c1 + i] == '--':
                            allowed.append([r1, c1 + i])
                        elif board_arr[r1][c1 + i][0] == ally:
                            break
                        elif board_arr[r1][c1 + i][0] == enemy:
                            allowed.append([r1, c1 + i])
                            break

        if board_arr[r1][c1][1] == 'B' or board_arr[r1][c1][1] == 'Q':  #Bishop's moves which also applies to Queen
            ally = board_arr[r1][c1][0]
            if (player == 1 and ally == 'w') or (player == -1 and ally == 'b'):
                ally = board_arr[r1][c1][0]
                enemy = 'w' if ally == 'b' else 'b'
                for i in range(1, 8):  ## Moving up-left the board
                    if board_arr[r1 - i][c1 - i] == '--':
                        allowed.append([r1 - i, c1 - i])
                    elif board_arr[r1 - i][c1 - i][0] == ally:
                        break
                    elif board_arr[r1 - i][c1 - i][0] == enemy:
                        allowed.append([r1 - i, c1 - i])
                        break
                for i in range(1, 8):  ## Moving down-left the board
                    if r1 + i <= 7:
                        if board_arr[r1 + i][c1 - i] == '--':
                            allowed.append([r1 + i, c1 - i])
                        elif board_arr[r1 + i][c1 - i][0] == ally:
                            break
                        elif board_arr[r1 + i][c1 - i][0] == enemy:
                            allowed.append([r1 + i, c1 - i])
                            break
                for i in range(1, 8):  ## Moving up-right
                    if c1 + i < 8:
                        if board_arr[r1 - i][c1 + i] == '--':
                            allowed.append([r1 - i, c1 + i])
                        elif board_arr[r1 - i][c1 + i][0] == ally:
                            break
                        elif board_arr[r1 - 1][c1 + i][0] == enemy:
                            allowed.append([r1 - i, c1 + i])
                            break
                for i in range(1, 8):  ## Moving down-right
                    if r1 + i < 8 and c1 + i < 8:
                        if board_arr[r1 + i][c1 + i] == '--':
                            allowed.append([r1 + i, c1 + i])
                        elif board_arr[r1 + i][c1 + i][0] == ally:
                            break
                        elif board_arr[r1 + i][c1 + i][0] == enemy:
                            allowed.append([r1 + i, c1 + i])
                            break
        if board_arr[r1][c1][1] == 'N':  #Knight's moves
            ally = board_arr[r1][c1][0]
            enemy = 'w' if ally == 'b' else 'b'
            if (player == 1 and ally == 'w') or (player == -1 and ally == 'b'):
                moves_list = [[r1 + 2, c1 + 1], [r1 + 2, c1 - 1], [r1 - 2, c1 + 1], [r1 - 2, c1 - 1],
                              [r1 + 1, c1 + 2], [r1 + 1, c1 - 2], [r1 - 1, c1 + 2], [r1 - 1, c1 - 2]]
                for i in moves_list:
                    if i[0] < 8 and i[1] < 8:
                        if board_arr[i[0]][i[1]][0] == enemy or board_arr[i[0]][i[1]] == '--':
                            allowed.append(i)
        if board_arr[r1][c1][1] == 'K':  #King's moves
            ally = board_arr[r1][c1][0]
            enemy = 'w' if ally == 'b' else 'b'
            if (player == 1 and ally == 'w') or (player == -1 and ally == 'b'):
                moves_list = [[r1 - 1, c1], [r1 - 1, c1 + 1], [r1 - 1, c1 - 1], [r1, c1 + 1],
                              [r1, c1 - 1], [r1 + 1, c1], [r1 + 1, c1 + 1], [r1 - 1, c1 - 1]]
                for i in moves_list:
                    if i[0] < 8 and i[1] < 8:
                        if board_arr[i[0]][i[1]][0] == enemy or board_arr[i[0]][i[1]] == '--':
                            allowed.append(i)

    return allowed


def draw_pieces():
    for j in range(8):
        for i in range(8):
            e = board_arr[j][i]
            if e != '--':
                screen.blit(OBJ[e], (i * width / 8, j * height / 8))


# print(board_arr)
run = True
clicks = []
while run:
    grid()
    draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            col = int(loc[0] // (width / 8))
            row = int(loc[1] // (width / 8))
            clicks.append(col)
            clicks.append(row)
        if len(clicks) == 4:
            # print(clicks)
            allowed = moves(clicks[3], clicks[2], clicks[1], clicks[0])
            # print(allowed)
            # print(clicks[2], clicks[3])
            if [clicks[3], clicks[2]] in allowed:
                board_arr[clicks[3]][clicks[2]] = board_arr[clicks[1]][clicks[0]]
                board_arr[clicks[1]][clicks[0]] = "--"
                player *= -1
            clicks = []

    pygame.display.update()

pygame.quit()
