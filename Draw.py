#------------------------------
#File:      Tic-Tac.py
#------------------------------


import pygame, sys
from pygame.locals import *

def place_mark(turn, grid):
    #checks mouse position, determining which section of the grid that mark was placed
    if pygame.mouse.get_pos()[0] < 234 and pygame.mouse.get_pos()[1]<234 and grid[0] == 0:
        grid[0] = turn
        return grid
    elif 234< pygame.mouse.get_pos()[0] < 468 and pygame.mouse.get_pos()[1]<234 and grid[1] == 0:
        grid[1] = turn
        return grid
    elif 468< pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1]<234 and grid[2] == 0:
        grid[2] = turn
        return grid
    elif pygame.mouse.get_pos()[0] < 234 and 234<pygame.mouse.get_pos()[1]<468 and grid[3] == 0:
        grid[3] = turn
        return grid
    elif 234< pygame.mouse.get_pos()[0] < 468 and 234<pygame.mouse.get_pos()[1]<468 and grid[4] == 0:
        grid[4] = turn
        return grid
    elif 468< pygame.mouse.get_pos()[0] and 234<pygame.mouse.get_pos()[1]<468 and grid[5] == 0:
        grid[5] = turn
        return grid
    elif pygame.mouse.get_pos()[0] < 234 and 468<pygame.mouse.get_pos()[1] and grid[6] == 0:
        grid[6] = turn
        return grid
    elif 234< pygame.mouse.get_pos()[0] < 468 and 468<pygame.mouse.get_pos()[1] and grid[7] == 0:
        grid[7] = turn
        return grid
    elif 468< pygame.mouse.get_pos()[0] and 468<pygame.mouse.get_pos()[1] and grid[8] == 0:
        grid[8] = turn
        return grid
    return grid

def get_position():
    #get section clicked
    if pygame.mouse.get_pos()[0] <= 234 and pygame.mouse.get_pos()[1]<=234:
        return 1
    elif 234< pygame.mouse.get_pos()[0] <= 468 and pygame.mouse.get_pos()[1]<=234:
        return 2
    elif 468<= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1]<=234:
        return 3
    elif pygame.mouse.get_pos()[0] <= 234 and 234<=pygame.mouse.get_pos()[1]<468:
        return 4
    elif 234< pygame.mouse.get_pos()[0] <= 468 and 234<=pygame.mouse.get_pos()[1]<468:
        return 5
    elif 468<= pygame.mouse.get_pos()[0] and 234<=pygame.mouse.get_pos()[1]<468:
        return 6
    elif pygame.mouse.get_pos()[0] <= 234 and 468<=pygame.mouse.get_pos()[1]:
        return 7
    elif 234< pygame.mouse.get_pos()[0] <= 468 and 468<=pygame.mouse.get_pos()[1]:
        return 8
    elif 468<= pygame.mouse.get_pos()[0] and 468<=pygame.mouse.get_pos()[1]:
        return 9

def draw_mark(mark):
    if mark == 1:
        return (77 + 234 * (mark - 1), 87)
    elif mark == 2:
        return (77 + 234 * (mark - 1), 87)
    elif mark == 3:
        return (77 + 234 * (mark - 1), 87)
    elif mark == 4:
        return (77 + 234 * (mark - 4), 321)
    elif mark == 5:
        return (77 + 234 * (mark - 4), 321)
    elif mark == 6:
        return (77 + 234 * (mark - 4), 321)
    elif mark == 7:
        return (77 + 234 * (mark - 7), 555)
    elif mark == 8:
        return (77 + 234 * (mark - 7), 555)
    elif mark == 9:
        return (77 + 234 * (mark - 7), 555)


'''
def turn_swap(turn):
    global img
    global c
    if turn == 'O':
        img = "Letter-X.png"
        c = pygame.image.load(img).convert_alpha()
        return 'X'
    if turn == 'X':
        img = "Circle.png"
        c = pygame.image.load(img).convert_alpha()
        return 'O'
'''
def run():
    global curr_turn
    global c
    global img
    global matrix

    display.fill((255, 255, 255))
    pygame.display.update()
    while True: #run game
        img = 'Brush.png'
        c = pygame.image.load(img).convert_alpha()
        x, y = pygame.mouse.get_pos()
        x -= c.get_width() / 2
        y -= c.get_height() / 2
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pygame.mouse.set_cursor((16, 7), (10, 3), (4064, 49155, 14392, 28686, 28686, 14392, 49155, 4064, 28686, 14392, 14392, 28686, 49155, 49155),(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

            if event.type == MOUSEBUTTONUP:
                pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
            if event.type == KEYDOWN:
                display.fill((255, 255, 255))
        display.blit(c, (x, y))
        dis()
        pygame.display.update()
        #if pygame.mouse.get_pressed() == (1, 0, 0):
        #    place_mark()    #combined with other file, take number and apply to section (remember to check if there is something already in that quadrant
        #    turn_swap(curr_turn)


def dis():
    #reset display
    global display
    global c
    global img
    global matrix



def main():
    # display board

    global display
    global curr_turn
    global matrix

    pygame.init()

    display = pygame.display.set_mode((702,702), 0, 32)

    pygame.draw.rect(display,(255,255,255),(0,0,702,702),0)
    display.fill((255,255,255))


    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    run()

    #pygame.mouse.set_cursor((48, 12), (30, 7), (32766,0,0, 1048575,0,0, 66977792,0,0, 34634616275448,0,0, 277076930199615,0,0, 272678883688479,0,0, 272678883688479,0,0, 272678883688479,0,0, 277076930199615,0,0, 34634616275448,0,0, 66977792,0,0, 1048575,0,0, 32766,0,0,0,0,0,0,0,0,0,0,0,0,0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ))
    #pygame.mouse.set_cursor((16, 7), (10, 3), (4064, 49155, 14392, 28686, 28686, 14392, 49155, 4064, 28686, 14392, 14392, 28686, 49155, 49155), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    #4064, 49155, 14392, 28686, 28686, 14392, 49155, 4064, 28686, 14392, 14392, 28686, 49155, 49155


main()