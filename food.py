import pygame
class Food():
    def __init__(self,x,y,bonus):
        self.x,self.y = x,y
        self.bonus = bonus
        self.value = 10 if self.bonus else self.value = 1
        self.sprite = pygame.image.load(r"C:\Users\Movavi_ School.DESKTOP-O1T25EP\PycharmProjects\pythonProject1\img\bonus_food.png") if self.bonus else self.sprite = pygame.image.load(r"C:\Users\Movavi_ School.DESKTOP-O1T25EP\PycharmProjects\pythonProject1\img\food.png")
    def draw(selfself,screen):
        screen.blit(self.sprite,(self.x,self.y))
    def get_coordinate(self):
        return self.x, self.y