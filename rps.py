# File created by: Liam Newberry

if True: # imports
    import time
    from random import choice
    import pygame as pg
    import os

game_folder = os.path.dirname(__file__)

if True: # game dimensions
    WIDTH = 1440
    HEIGHT = 960
    FPS = 30

if True: # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

if True: # initializing pygame
    pg.init()
    pg.mixer.init()
    pg.display.set_caption("Rock, Paper, Scissors")

click = pg.MOUSEBUTTONUP
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

if True: # loading images
    rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
    rock_image_rect = rock_image.get_rect()
    rock_image_rect.x = 50
    rock_image_rect.y = 480
    paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
    paper_image_rect = paper_image.get_rect()
    paper_image_rect.x = 622
    paper_image_rect.y = 480
    scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
    scissors_image_rect = scissors_image.get_rect()
    scissors_image_rect.x = 1050
    scissors_image_rect.y = 480
    close_image = pg.image.load(os.path.join(game_folder, "close.jpg")).convert()
    close_image_rect = close_image.get_rect()
    close_image_rect.x = 1340
    close_image_rect.y = 0
    choose_image = pg.image.load(os.path.join(game_folder, "choose.jpg")).convert()
    choose_image_rect = choose_image.get_rect()
    choose_image_rect.x = 280
    choose_image_rect.y = 340
    computer_image = pg.image.load(os.path.join(game_folder, "computer.jpg")).convert()
    computer_image_rect = computer_image.get_rect()
    computer_image_rect.x = 50
    computer_image_rect.y = 50
    user_image = pg.image.load(os.path.join(game_folder, "user.jpg")).convert()
    user_image_rect = user_image.get_rect()
    user_image_rect.x = 50
    user_image_rect.y = 480
    colon_image = pg.image.load(os.path.join(game_folder, "colon.jpg")).convert()
    colon_image_rect = colon_image.get_rect()
    colon_image_rect.x = 510
    colon_image_rect.y = 70
    colon_image2 = pg.image.load(os.path.join(game_folder, "colon2.jpg")).convert()
    colon_image_rect2 = colon_image2.get_rect()
    colon_image_rect2.x = 510
    colon_image_rect2.y = 600
    selected_image = pg.image.load(os.path.join(game_folder, "selected.jpg")).convert()
    selected_image_rect = selected_image.get_rect()
    s_select_image = pg.image.load(os.path.join(game_folder, "s_select.jpg")).convert()
    s_select_image_rect = s_select_image.get_rect()
    win_image = pg.image.load(os.path.join(game_folder, "win.jpg")).convert()
    win_image_rect = win_image.get_rect()
    lose_image = pg.image.load(os.path.join(game_folder, "lose.jpg")).convert()
    lose_image_rect = lose_image.get_rect()
    tie_image = pg.image.load(os.path.join(game_folder, "tie.jpg")).convert()
    tie_image_rect = tie_image.get_rect()

running = True

def intialize():
    screen.fill(BLACK)
    screen.blit(rock_image,rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    screen.blit(choose_image, choose_image_rect)
    screen.blit(close_image, close_image_rect)

def rock_select():
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    selected_image_rect.x = 0
    selected_image_rect.y = 360
    green_screen = selected_image.get_at((100,100))
    selected_image.set_colorkey(green_screen)
    screen.blit(selected_image, selected_image_rect)
    mid_game_blit('r')

def paper_select():
    screen.fill(BLACK)
    screen.blit(paper_image, paper_image_rect)
    selected_image_rect.x = 480
    selected_image_rect.y = 360
    green_screen = selected_image.get_at((100,100))
    selected_image.set_colorkey(green_screen)
    screen.blit(selected_image, selected_image_rect)
    mid_game_blit('p')

def scissors_select():
    screen.fill(BLACK)
    screen.blit(scissors_image, scissors_image_rect)
    s_select_image_rect.x = 1000
    s_select_image_rect.y = 360
    green_screen = s_select_image.get_at((100,100))
    s_select_image.set_colorkey(green_screen)
    screen.blit(s_select_image, s_select_image_rect)
    mid_game_blit('s')

cpu_choice = False

def cpu_rand_choice():
    choices = ["r", "p", "s"]
    global cpu_choice
    cpu_choice = choice(choices)

def mid_game_blit(user_choice):
    pg.display.update((0,0),(WIDTH, HEIGHT))
    time.sleep(1)
    screen.fill(BLACK)
    screen.blit(computer_image, computer_image_rect)
    screen.blit(colon_image, colon_image_rect)
    screen.blit(user_image, user_image_rect)
    screen.blit(colon_image2, colon_image_rect2)
    if cpu_choice == False:
        cpu_rand_choice()
    if cpu_choice == 'r':
        rock_image_rect.x = 680
        rock_image_rect.y = 50
        screen.blit(rock_image, rock_image_rect)
    elif cpu_choice == 'p':
        paper_image_rect.x = 680
        paper_image_rect.y = 50
        screen.blit(paper_image, paper_image_rect)
    elif cpu_choice == 's':
        scissors_image_rect.x = 680
        scissors_image_rect.y = 50
        screen.blit(scissors_image, scissors_image_rect)
    if user_choice == 'r':
        rock_image_rect.x = 680
        rock_image_rect.y = 520
        screen.blit(rock_image, rock_image_rect)
    elif user_choice == 'p':
        paper_image_rect.x = 680
        paper_image_rect.y = 520
        screen.blit(paper_image, paper_image_rect)
    elif user_choice == 's':
        scissors_image_rect.x = 680
        scissors_image_rect.y = 520
        screen.blit(scissors_image, scissors_image_rect)
    endgame(cpu_choice, user_choice)
    
def endgame(cpu_choice, user_choice):
    pg.display.update((0,0),(WIDTH, HEIGHT))
    time.sleep(3)
    screen.fill(BLACK)
    win = 0
    if user_choice == cpu_choice:
        win = None
    elif user_choice == 'r' and cpu_choice == 'p':
        win = False
    elif user_choice == 'p' and cpu_choice == 's':
        win = False
    elif user_choice == 's' and cpu_choice == 'r':
        win = False
    elif user_choice == 'r' and cpu_choice == 's':
        win = True
    elif user_choice == 'p' and cpu_choice == 'r':
        win = True
    elif user_choice == 's' and cpu_choice == 'p':
        win = True
    if win == None:
        print('tie')
        screen.blit(tie_image, tie_image_rect)
        screen.blit(close_image, close_image_rect)
    elif win == False:
        print('lose')
        screen.blit(lose_image, lose_image_rect)
        screen.blit(close_image, close_image_rect)
    elif win == True:
        print('win')
        screen.blit(win_image, win_image_rect)
        screen.blit(close_image, close_image_rect)
def main():
    running = True

    rock = False
    paper = False
    scissors = False
    initial = False
    completed = False

    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if initial == False:
                intialize()
                initial = True
            if event.type == pg.QUIT:
                running = False
            if event.type == click:
                mcoords = pg.mouse.get_pos()
                if close_image_rect.collidepoint(mcoords):
                    running = False
            if event.type == click:
                mcoords = pg.mouse.get_pos()
                if rock_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    rock = True
                if paper_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    paper = True
                if scissors_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    scissors = True
        if rock == True and completed == False:
            rock_select()
            completed = True
        if paper == True and completed == False:
            paper_select()
            completed = True
        if scissors == True and completed == False:
            scissors_select()
            completed = True
        pg.display.flip()

main()

pg.quit()