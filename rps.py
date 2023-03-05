# File created by: Liam Newberry

'''
All of the "if True" statements are there so I can 
minimize the sections of code for viewing

Sources: 
https://web.microsoftstream.com/user/d5627449-d3df-4aed-901f-3cae632c79ab (search Pygame)
https://www.pygame.org/wiki/GettingStarted
https://www.pygame.org/docs/ref/surface.html
https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5F2023%5FSpring%2FCode%2Fexercises%2Fper1%2Frps%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5F2023%5FSpring%2FCode%2Fexercises%2Fper1
'''

# this imports the different modules I will be using
if True: # imports
    # I will use sleep from time to delay the graphics so each set of images has time to be seen
    import time
    # this will be used to let the cpu choose its item
    from random import choice
    # this imports pygame
    import pygame as pg
    # this helps use the files provided
    import os

game_folder = os.path.dirname(__file__)

# this is the dimensions of the screen and frame rate
if True: # game dimensions
    WIDTH = 1440
    HEIGHT = 960
    FPS = 30

# these are various colors that are used for background colors and color_key()
if True: # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

# this starts pygame, the audio mixer, and labels the window of the pygame
if True: # initializing pygame
    pg.init()
    pg.mixer.init()
    pg.display.set_caption("Rock, Paper, Scissors")

# these are various shortened versions for parts of the pg module I will use
if True: # presets
    click = pg.MOUSEBUTTONUP
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

# these are all the images I will need to display throughout the project
if True: # loading images
    # this imports the image and stores it as rock_image
    rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
    # this gets the bounding box of the rock_image
    rock_image_rect = rock_image.get_rect()
    # this is the x cordinate of where the image will be displayed
    rock_image_rect.x = 50
    # this is the y cordinate of where the image will be displayed
    rock_image_rect.y = 340
    paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
    paper_image_rect = paper_image.get_rect()
    paper_image_rect.x = 622
    paper_image_rect.y = 340
    scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
    scissors_image_rect = scissors_image.get_rect()
    scissors_image_rect.x = 1050
    scissors_image_rect.y = 340
    close_image = pg.image.load(os.path.join(game_folder, "close.jpg")).convert()
    close_image_rect = close_image.get_rect()
    close_image_rect.x = 1340
    close_image_rect.y = 0
    choose_image = pg.image.load(os.path.join(game_folder, "choose.jpg")).convert()
    choose_image_rect = choose_image.get_rect()
    choose_image_rect.x = 280
    choose_image_rect.y = 150
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

# a variable that dictates when to keep pg running
running = True

# this sets up the initial screen of the program
# it makes the background black and draws all the starting images
def intialize():
    screen.fill(BLACK)
    screen.blit(rock_image,rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    screen.blit(choose_image, choose_image_rect)
    screen.blit(close_image, close_image_rect)

# this draws the selection screen for when the user chooses rock
# it then calls the next graphic function with the user_choice rock parameter
def rock_select():
    # makes the background black
    screen.fill(BLACK)
    # redraws the rock image
    screen.blit(rock_image, rock_image_rect)
    # sets the location for the red selection arond the rock image
    selected_image_rect.x = 0
    selected_image_rect.y = 240
    # this gets the green color's color id from the selection image
    green_screen = selected_image.get_at((100,100))
    # this tells the program to set the alpha value to 0 of the detected color
    selected_image.set_colorkey(green_screen)
    # draws the image
    screen.blit(selected_image, selected_image_rect)
    # calls the next graphic function with the user_choice rock parameter
    mid_game_blit('r')

# this draws the selection screen for when the user chooses paper
# it then calls the next graphic function with the user_choice paper parameter
def paper_select():
    screen.fill(BLACK)
    screen.blit(paper_image, paper_image_rect)
    selected_image_rect.x = 480
    selected_image_rect.y = 240
    green_screen = selected_image.get_at((100,100))
    selected_image.set_colorkey(green_screen)
    screen.blit(selected_image, selected_image_rect)
    mid_game_blit('p')

# this draws the selection screen for when the user chooses scissors
# it then calls the next graphic function with the user_choice scissors parameter
def scissors_select():
    screen.fill(BLACK)
    screen.blit(scissors_image, scissors_image_rect)
    s_select_image_rect.x = 1000
    s_select_image_rect.y = 220
    green_screen = s_select_image.get_at((100,100))
    s_select_image.set_colorkey(green_screen)
    screen.blit(s_select_image, s_select_image_rect)
    mid_game_blit('s')

# this just assigns a meaningless value to cpu_choice
cpu_choice = False

# this function makes the cpu randomly choose from the choices list
# it makes the cpu_choice a global variable
def cpu_rand_choice():
    choices = ["r", "p", "s"]
    global cpu_choice
    cpu_choice = choice(choices)

# this function is mainly used to display the user and cpu choices
# and then calls the final winscreen function based on the cpu and user choice parameters
def mid_game_blit(user_choice):
    # this line allows all my blit calls from the previous function to be flushed to the screen
    # the parameters just tell it to flush everything from the coordinates of the window
    pg.display.update((0,0),(WIDTH, HEIGHT))
    # delays the next graphic by a second
    time.sleep(1)
    # resets the screen to black and draws the profile images
    screen.fill(BLACK)
    screen.blit(computer_image, computer_image_rect)
    screen.blit(colon_image, colon_image_rect)
    screen.blit(user_image, user_image_rect)
    screen.blit(colon_image2, colon_image_rect2)
    # if there hasn't been a cpu selection yet it runs the function
    if cpu_choice == False:
        cpu_rand_choice()
    # if the computer chooses rock it draws it on its new coordinates
    if cpu_choice == 'r':
        rock_image_rect.x = 680
        rock_image_rect.y = 50
        screen.blit(rock_image, rock_image_rect)
    # if the computer chooses paper it draws it on its new coordinates
    elif cpu_choice == 'p':
        paper_image_rect.x = 680
        paper_image_rect.y = 50
        screen.blit(paper_image, paper_image_rect)
    # if the computer chooses scissors it draws it on its new coordinates
    elif cpu_choice == 's':
        scissors_image_rect.x = 680
        scissors_image_rect.y = 50
        screen.blit(scissors_image, scissors_image_rect)
    # if the user chose rock it draws it next to the user icon on new coordinates
    if user_choice == 'r':
        rock_image_rect.x = 680
        rock_image_rect.y = 520
        screen.blit(rock_image, rock_image_rect)
    # if the user chose paper it draws it next to the user icon on new coordinates
    elif user_choice == 'p':
        paper_image_rect.x = 680
        paper_image_rect.y = 520
        screen.blit(paper_image, paper_image_rect)
    # if the user chose scissors it draws it next to the user icon on new coordinates
    elif user_choice == 's':
        scissors_image_rect.x = 680
        scissors_image_rect.y = 520
        screen.blit(scissors_image, scissors_image_rect)
    # this runs the final win/lose/tie screen based on the cpu and user choice comparison
    endgame(cpu_choice, user_choice)
    
# this is the final graphic screen
# it first compares the user/cpu choices and then displays the winner
def endgame(cpu_choice, user_choice):
    # this line allows all my blit calls from the previous function to be flushed to the screen
    # the parameters just tell it to flush everything from the coordinates of the window
    pg.display.update((0,0),(WIDTH, HEIGHT))
    # this lets the user view the choice screen for 3 seconds
    time.sleep(3)
    # this makes the screen black
    screen.fill(BLACK)
    # this is a meaningless value for win
    win = 0
    # if the user and cpu chose the same thing it stores win with None
    if user_choice == cpu_choice:
        win = None
    # these go through all the win/lose scenarious and stores a cpu win as False in win and vice versa
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
    # if there is a tie it shows a tie screen image
    if win == None:
        # draws the tie image
        screen.blit(tie_image, tie_image_rect)
        # provide the x to close out of the window
        screen.blit(close_image, close_image_rect)
    # if there is a loss it shows a loss screen image
    elif win == False:
        screen.blit(lose_image, lose_image_rect)
        screen.blit(close_image, close_image_rect)
    # if there is a win it shows a win screen image
    elif win == True:
        screen.blit(win_image, win_image_rect)
        screen.blit(close_image, close_image_rect)

# this function calls the specific functions, creates many variables, and detects ay inputs/events in the window 
def main():
    running = True
    # none of these varaibles have been interacted with yet so they == False
    rock = False
    paper = False
    scissors = False
    initial = False
    completed = False
    # while running the pg will be displaying graphics and looking for events
    while running:
        # it is how much the game updates for frames and checks for events
        clock.tick(FPS)
        # this detects any event in the pg
        for event in pg.event.get():
            # if the initial images haven't been blitted it runs the initial image drawing function
            if initial == False:
                intialize()
                # now that the initial images have been blitted this is True
                initial = True
            # if the game detects a quit event the while loop will break
            if event.type == pg.QUIT:
                running = False
            # when the user clicks...
            if event.type == click:
                # this gets the coordinates of where the mouse clicked
                mcoords = pg.mouse.get_pos()
                # if the user clicks on the x image in the top right the while loop while break and the window will close
                if close_image_rect.collidepoint(mcoords):
                    running = False
            # if the user clicks...
            if event.type == click:
                # get the coordinates of the click
                mcoords = pg.mouse.get_pos()
                # if they clicked the rock image the value of rock is True so the function can run below
                # this only applies when none of the other images have been clicked
                if rock_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    rock = True
                # if they clicked the paper image the value of paper is True so the function can run below
                # this only applies when none of the other images have been clicked
                if paper_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    paper = True
                # if they clicked the scissors image the value of scissors is True so the function can run below
                # this only applies when none of the other images have been clicked
                if scissors_image_rect.collidepoint(mcoords) and rock == False and paper == False and scissors == False:
                    scissors = True
        # if the select function hasn't been run and rock was selected, call the rock select function
        if rock == True and completed == False:
            rock_select()
            # a select function has been run so completed is True
            completed = True
        # if the select function hasn't been run and paper was selected, call the rock select function
        if paper == True and completed == False:
            paper_select()
            # a select function has been run so completed is True
            completed = True
        # if the select function hasn't been run and scissors was selected, call the rock select function
        if scissors == True and completed == False:
            scissors_select()
            # a select function has been run so completed is True
            completed = True
        # this updates everything that has been added to the screen to the display
        pg.display.flip()

# calls the main function
main()

# this closes the pg program
pg.quit()