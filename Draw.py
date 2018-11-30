#------------------------------
#File:      Draw.py
#------------------------------


import pygame, sys
from pygame.locals import *



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



def dis():
    #reset display
    global display

    pygame.display.update()



def main():
    global display
    pygame.init()

    display = pygame.display.set_mode((702,702), 0, 32)

    pygame.draw.rect(display,(255,255,255),(0,0,702,702),0)
    display.fill((255,255,255))

    run()

main()