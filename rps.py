from time import sleep
from random import choice
import pygame as pg
import os

game_folder = os.path.dirname(__file__)

WIDTH = 1400
HEIGHT = 800
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pg.init()
pg.mixer.init()
pg.display.set_caption("Rock, Paper, Scissors")

click = pg.MOUSEBUTTONUP
screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
clock = pg.time.Clock()

#pick_image = pg.image.load(os.path.join(game_folder, "pick.jpg")).convert()
#pick_image_rect = pick_image.get_rect()
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

running = True
def intialize():
    screen.fill(BLACK)
    screen.blit(rock_image,rock_image_rect)
    #screen.blit(pick_image, pick_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    screen.blit(choose_image, choose_image_rect)
    screen.blit(close_image, close_image_rect)
def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == click:
                mcoords = pg.mouse.get_pos()
                if close_image_rect.collidepoint(mcoords):
                    running = False
        intialize()

        pg.display.flip()

main()

pg.quit()