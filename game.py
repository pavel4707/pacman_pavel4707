import pygame

from settings import Game_Settings
from pac_man import PacMan
from ghost import Ghost
from pac_man_images import Images
from direction import Direction
from wall import Wall
from food import Food
class Game():
    def __init__(self):
        self.game_settings = Game_Settings()
        pygame.init()
        self.screen = pygame.display.set_mode(self.Game_Settings.WIDTH,self.Game_Settings.HEIGHT)
        self.pac_man = None
        self.food = []
        self.coordinates_eat = {}
        self.ghosts = []
        self.walls = []
        self.coordinates_walls = {}
        self.ticks = 60
    def parse_map(self):
        x,y = 0,0
        for i in self.Game_Settings.MAP:
            y += 1
            for j in i:
                x += 1
                if j == "P":
                    self.player = PacMan(x,y)
                elif j == "1":
                    self.food.append(Food(x,y,True))
                    self.coordinates_eat[(x,y)] = self.food[-1]
                elif j == "0":
                    self.food.append(Food(x,y,False))
                    self.coordinates_eat[(x, y)] = self.food[-1]
                elif j == "G":
                    self.ghosts.append(Ghost(x,y))
                else:
                    self.walls.append(Wall(x,y))
                    self.coordinates_walls[(x, y)] = self.walls[-1]
    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    key_check(event.key)


