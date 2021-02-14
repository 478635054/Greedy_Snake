import pygame
import random
import sys
from pygame.locals import *

class Point():
    row = 0
    column = 0

    def __init__(self,row,column):
        self.row = row
        self.column = column

    def copy(self):
        return Point(row = self.row,column = self.column)

pygame.init()
width = 800
height = 600

ROW = 30
COLUMN = 40
direct = 'left'
head_color = (255,106,106)
snake_color = (160,32,240)
food_color = (255,165,0)
screen = pygame.display.set_mode((width,height))
head = Point(row = random.randint(3,ROW - 3),column = random.randint(3,COLUMN - 3))

snake = [
    Point(row = head.row,column = head.column + 1),
    Point(row = head.row,column = head.column + 2),
]

def getfood():
    while 1:
        position = Point(row = random.randint(0,ROW - 1),column = random.randint(0,COLUMN - 1))
        overlap = False
        if position.column == head.column and position.row == head.row:
            overlap = True
        for body in snake:
            if position.column == body.column and position.row == body.row:
                overlap = True
                break
        if overlap == False:
            break
    return position

def draw(Point,color):
    left = Point.column * width / COLUMN
    top = Point.row * height / ROW
    pygame.draw.rect(screen,color,(left,top,width / COLUMN,height / ROW))

food = getfood()

# insert the image and adapt it to the screen
backgroundimage = pygame.image.load('background.png')
newingimage = pygame.transform.scale(backgroundimage,(width,height))
screen.blit(newingimage,(0,0))
pygame.display.set_caption('Greedy Snake')

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # monitor the keyboard
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                if direct == 'right' or direct == 'left':
                    direct = 'up'
            if event.key == K_DOWN:
                if direct == 'right' or direct == 'left':
                    direct = 'down'
            if event.key == K_RIGHT:
                if direct == 'up' or direct == 'down':
                    direct = 'right'
            if event.key == K_LEFT:
                if direct == 'up' or direct =='down':
                    direct ='left'

    #offer the food
    eat = (head.row == food.row and head.column == food.column)
    if eat:
        food = Point(row = random.randint(0,ROW - 1),column = random.randint(0,COLUMN -1))
    snake.insert(0,head.copy())
    if not eat:
        snake.pop()

    # change the direction
    if direct == 'up':
        head.row -= 1
    if direct == 'down':
        head.row += 1
    if direct == 'right':
        head.column += 1
    if direct == 'left':
        head.column -= 1

    # identify the death of the snake
    death = False
    if head.row < 0 or head.column < 0 or head.row >= ROW or head.column >= COLUMN:
        death = True
    for body in snake:
        if head.row == body.row and head.column == body.column:
            death = True
            break
    if death:
        print('Game over')
        running = False

    # draw objects
    backgroundimage = pygame.image.load('background.png')
    newingimage = pygame.transform.scale(backgroundimage,(width,height))
    screen.blit(newingimage,(0,0))
    draw(head, head_color)
    draw(food, food_color)
    for body in snake:
        draw(body, snake_color)
    pygame.display.flip()
