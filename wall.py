import pygame
class Wall():
    def __init__(self,x,y):
        self.x = y
        self.y = y
        self.sprite = pygame.image.load(r"C:\Users\Movavi_ School.DESKTOP-O1T25EP\PycharmProjects\pythonProject1\img\wall.png")
    def draw(self,screen):
        screen.blit(self.sprite,(self.x,self.y))

