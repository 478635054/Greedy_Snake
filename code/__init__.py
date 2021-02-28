import pygame
import random
import sys
from pygame.locals import *
import variables
class Point():
    row = 0
    column = 0

    def __init__(self,row,column):
        self.row = row
        self.column = column

    def copy(self):
        return Point(row = self.row,column = self.column)

pygame.init()

head = Point(row = random.randint(3,variables.ROW - 3),column = random.randint(3,variables.COLUMN - 3))

snake = [
    Point(row = head.row,column = head.column + 1),
    Point(row = head.row,column = head.column + 2),
]

def getfood():
    while 1:
        position = Point(row = random.randint(0,variables.ROW - 1),column = random.randint(0,variables.COLUMN - 1))
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
    left = Point.column * variables.width / variables.COLUMN
    top = Point.row * variables.height / variables.ROW
    pygame.draw.rect(variables.screen,color,(left,top,variables.width / variables.COLUMN,variables.height / variables.ROW))

food = getfood()

# insert the image and adapt it to the screen
backgroundimage = pygame.image.load('background.png')
newingimage = pygame.transform.scale(backgroundimage,(variables.width,variables.height))
variables.screen.blit(newingimage,(0,0))
pygame.display.set_caption('Greedy Snake')

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # monitor the keyboard
        elif event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                if variables.direct == 'right' or variables.direct == 'left':
                    variables.direct = 'up'
            if event.key == K_DOWN or event.key == K_s:
                if variables.direct == 'right' or variables.direct == 'left':
                    variables.direct = 'down'
            if event.key == K_RIGHT or event.key == K_d:
                if variables.direct == 'up' or variables.direct == 'down':
                    variables.direct = 'right'
            if event.key == K_LEFT or event.key == K_a:
                if variables.direct == 'up' or variables.direct =='down':
                    variables.direct ='left'
            if event.key == K_p:
                variables.pause = True

            #pause the game
            while variables.pause == True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            variables.pause = False
                        
    #offer the food
    eat = (head.row == food.row and head.column == food.column)
    if eat:
        food = Point(row = random.randint(0,variables.ROW - 1),column = random.randint(0,variables.COLUMN -1))
    snake.insert(0,head.copy())
    if not eat:
        snake.pop()

    # change the direction
    if variables.direct == 'up':
        head.row -= 1
    if variables.direct == 'down':
        head.row += 1
    if variables.direct == 'right':
        head.column += 1
    if variables.direct == 'left':
        head.column -= 1

    # identify the death of the snake
    death = False
    if head.row < 0 or head.column < 0 or head.row >= variables.ROW or head.column >= variables.COLUMN:
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
    newingimage = pygame.transform.scale(backgroundimage,(variables.width,variables.height))
    variables.screen.blit(newingimage,(0,0))
    draw(head, variables.head_color)
    draw(food, variables.food_color)
    for body in snake:
        draw(body, variables.snake_color)
    pygame.display.flip()
