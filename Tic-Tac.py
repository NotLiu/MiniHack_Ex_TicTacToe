#------------------------------
#File:      Tic-Tac.py
#------------------------------


import pygame
print('py')
def place_mark():
    #checks mouse position, determining which section of the grid that mark was placed
    if pygame.mouse.get_pos()[0] < 100 and pygame.mouse.get_pos()[1]<100:
        return 1
    elif 100< pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1]<100:
        return 2
    elif 200< pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1]<100:
        return 3
    elif pygame.mouse.get_pos()[0] < 100 and 100<pygame.mouse.get_pos()[1]<200:
        return 4
    elif 100< pygame.mouse.get_pos()[0] < 200 and 100<pygame.mouse.get_pos()[1]<200:
        return 5
    elif 200< pygame.mouse.get_pos()[0] and 100<pygame.mouse.get_pos()[1]<200:
        return 6
    elif pygame.mouse.get_pos()[0] < 100 and 200<pygame.mouse.get_pos()[1]:
        return 7
    elif 100< pygame.mouse.get_pos()[0] < 200 and 200<pygame.mouse.get_pos()[1]:
        return 8
    elif 200< pygame.mouse.get_pos()[0] and 200<pygame.mouse.get_pos()[1]:
        return 9

def turn_swap(turn):
    if turn == 'O':
        pygame.mouse.set_cursor((12, 7), (5, 3), (3075, 1806, 952, 224, 952, 1806, 3075), (0, 0, 0, 0, 0, 0, 0))
    else:
        pygame.mouse.set_cursor((12, 7), (5, 3), (504, 780, 1542, 3075, 1542, 780, 504), (0, 0, 0, 0, 0, 0, 0))

def main():
    # display board
    matrix = [[None] * 3] * 3
    # [[None, None, None],[None, None, None],[None, None, None]]

    curr_turn = 'O'
    pygame.mouse.set_cursor((12,7),(5,3),(504, 780, 1542, 3075, 1542, 780, 504),(0, 0, 0, 0, 0, 0, 0))

    while quit_game != True: #run game
        if pygame.mouse.get_pressed() == (1, 0, 0):
            place_mark()    #combined with other file, take number and apply to section (remember to check if there is something already in that quadrant
            turn_swap(curr_turn)
