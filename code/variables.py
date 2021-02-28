import pygame

width = 800
height = 600
ROW = 30
COLUMN = 40
direct = 'left'
pause = False
head_color = (255,106,106)
snake_color = (160,32,240)
food_color = (255,165,0)
screen = pygame.display.set_mode((width,height))

def variable():
    global width
    global height
    global ROW
    global COLUMN
    global direct
    global head_color
    global snake_color
    global food_color
    global screen
    global pause
    width = 800
    height = 600
    ROW = 30
    COLUMN = 40
    direct = 'left'
    ead_color = (255,106,106)
    snake_color = (160,32,240)
    food_color = (255,165,0)
    screen = pygame.display.set_mode((width,height))