import pygame
class Player(Entity):
    def __init__(self,lifes):
        self.lifes = lifes
        self.direction = None
        self.playerpos = (x,y)
        self.picture = None
        can.move = True
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        self.direction = "DOWN"
                        self.picture = pygame.image.load(pacman_down.png)
                    elif event.key == K_UP:
                        self.direction = "UP"
                        self.picture = pygame.image.load(pacman_up.png)
                    elif event.key == K_LEFT:
                        self.direction = "LEFT"
                        self.picture = pygame.image.load(pacman_left.png)
                    elif event.key == K_RIGHT:
                        self.direction = "RIGHT"
                        self.picture = pygame.image.load(pacman_right.png)
            Player.move()
    def move(self):
        if can.move == True:
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
            if (self.pos.x,self.pos.y - 5) in dict_walls.keys():
                can.move = False
        elif self.direction == "DOWN":
            if (self.pos.x,self.pos.y + 5) in dict_walls.keys():
                can.move = False
        elif self.direction == "LEFT":
            if (self.pos.x - 5,self.pos.y) in dict_walls.keys():
                can.move = False
        elif self.direction == "RIGHT":
            if (self.pos.x + 5,self.pos.y) in dict_walls.keys():
                can.move = False
        else:
            can.move = True
# pac-man при нажатии на клавишу один раз двигается до ближайшего препятствия
