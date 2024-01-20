import ps
import pfuncs
import pygame
import sys

# No cases, assume input is valid.
def main():
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))
    
    pfuncs.print_board_empty(l,w)

    obj = ps.sweeper(l,w,3)
    initW = int(input("Enter top coordinate: "))
    initL = int(input("Enter side coordinate: "))
    
    obj.generate_mines(initL,initW)
    pfuncs.print_board(obj)

    wincase = 0
    while (wincase == 0):
        initW = int(input("Enter top coordinate: "))
        initL = int(input("Enter side coordinate: "))
        if (obj.checked[initL][initW] == 1):
            print("Already checked!")
        elif (obj.mines[initL][initW] == -1):
            print("You lose!")
            pfuncs.print_board_answers(obj)
            wincase = 1
        else:
            obj.set_checked(initL,initW)
            if (obj.check_win()):
                print("You win!")
                pfuncs.print_board_answers(obj)
                wincase = 2
            else:
                pfuncs.print_board(obj)
                
# Easy: 8x8, 10 mines
# Medium: 16x16, 40 mines
# Hard: 30x16, 99 mines 
def main_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    img_1 = pygame.image.load("img/1.png").convert_alpha()
    img_2 = pygame.image.load("img/2.png").convert_alpha()
    img_3 = pygame.image.load("img/3.png").convert_alpha()
    img_4 = pygame.image.load("img/4.png").convert_alpha()
    img_5 = pygame.image.load("img/5.png").convert_alpha()
    img_6 = pygame.image.load("img/6.png").convert_alpha()
    img_7 = pygame.image.load("img/7.png").convert_alpha()
    img_8 = pygame.image.load("img/8.png").convert_alpha()
    img_bomb = pygame.image.load("img/boom.png").convert_alpha()
    img_flag = pygame.image.load("img/flag.png").convert_alpha()
    img_checked = pygame.image.load("img/checked.png").convert_alpha()
    img_unchecked = pygame.image.load("img/unchecked.png").convert_alpha()
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1: # lmb
            #         # handle_left_click(event.pos)
            #         print(event.pos[0])
            #         print(event.pos[1])
            #     elif event.button == 3:  # rmb
            #         print(event.pos[0])
            #         print(event.pos[1])          
        screen.fill((90, 90, 90))
        
        pygame.display.update()
    
if __name__ == "__main__":
    main_pygame()
