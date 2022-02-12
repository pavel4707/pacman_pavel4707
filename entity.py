import pygame
import sys
from pygame.color import THECOLORS
class Player(Entity):
    def __init__(self,lifes):
        self.lifes = lifes
        self.direction = None
        self.playerpos = (x,y)
        self.score = 0
        can_move = True
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        self.direction = "DOWN"
                    elif event.key == K_UP:
                        self.direction = 'UP"
                    elif event.key == K_LEFT:
                        self.direction = "LEFT"
                    elif event.key == K_RIGHT:
                        self.direction = "RIGHT"
            Player.move()
    def move(self):
        if can_move == True:
            if self.direction == "DOWN":
                self.playerpos.y += 5
            elif self.direction == "UP":
                self.playerpos.y -= 5
            elif self.direction == "LEFT":
                self.playerpos.x -= 5
            elif self.direction == "RIGHT":
                self.playerpos.x += 5
            if self.playerpos in dict_food.keys():# тот самый словарь у Андрея 
                self.score += 10
    def can_move(self):
        if self.direction == "UP":
        elif self.direction == "DOWN":
        elif self.direction == :
        elif self.direction ==:
        if self.playerpos + 5 in dict_walls.keys():
            can_move = False
        else:
            can_move = True
# pac-man при нажатии на клавишу один раз двигается до ближайшего препятствия