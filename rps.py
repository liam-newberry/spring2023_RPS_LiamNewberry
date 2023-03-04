# File created by: Liam Newberry

if True: # imports
    from time import sleep
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
    colon_image = pg.image.load(os.path.join(game_folder, "colon.jpg")).convert()
    colon_image_rect = colon_image.get_rect()
    colon_image_rect.x = 510
    colon_image_rect.y = 70
    selected_image = pg.image.load(os.path.join(game_folder, "selected.jpg")).convert()
    selected_image_rect = selected_image.get_rect()
    s_select_image = pg.image.load(os.path.join(game_folder, "s_select.jpg")).convert()
    s_select_image_rect = s_select_image.get_rect()

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

def paper_select():
    screen.fill(BLACK)
    screen.blit(paper_image, paper_image_rect)
    selected_image_rect.x = 480
    selected_image_rect.y = 360
    green_screen = selected_image.get_at((100,100))
    selected_image.set_colorkey(green_screen)
    screen.blit(selected_image, selected_image_rect)

def scissors_select():
    screen.fill(BLACK)
    screen.blit(scissors_image, scissors_image_rect)
    s_select_image_rect.x = 1000
    s_select_image_rect.y = 360
    green_screen = s_select_image.get_at((100,100))
    s_select_image.set_colorkey(green_screen)
    screen.blit(s_select_image, s_select_image_rect)

def cpu_rand_choice():
    choices = ["r", "p", "s"]
    return choice(choices)

def mid_game_blit(option):
    sleep(1)
    screen.fill(BLACK)
    screen.blit(computer_image, computer_image_rect)
    screen.blit(colon_image, colon_image_rect)

def main():
    running = True

    rock = False
    paper = False
    scissors = False
    initial = False
    cpu_choice = None

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
        if rock == True:
            rock_select()
        if paper == True:
            paper_select()
        if scissors == True:
            scissors_select()
        if paper == True or rock == True or scissors == True:
            cpu_choice = cpu_rand_choice()
            rock = False
            paper = False
            scissors = False
        if cpu_choice != None:
            mid_game_blit(rock)
        pg.display.flip()

main()

pg.quit()