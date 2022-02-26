from pac_man_images import Images
from direction import Direction
class PacMan():
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.direction = Direction.none
        self.speed = 15
        self.mouse_is_open = False
    def draw(self):
        if self.direction == Direction.none:
            screen.blit(Images.stay, (self.x, self.y))
        else:
            if self.direction == Direction.down:
                if self.mouse_is_open:
                    screen.blit(Images.down_open, (self.x, self.y))
                else:
                    screen.blit(Images.down_close, (self.x, self.y))
            elif self.direction == Direction.up:
                if self.mouse_is_open:
                    screen.blit(Images.up_open, (self.x, self.y))
                else:
                    screen.blit(Images.up_close, (self.x, self.y))
            elif self.direction == Direction.left:
                if self.mouse_is_open:
                    screen.blit(Images.left_open, (self.x, self.y))
                else:
                    screen.blit(Images.left_close, (self.x, self.y))
            elif self.direction == Direction.right:
                if self.mouse_is_open:
                    screen.blit(Images.right_open, (self.x, self.y))
                else:
                    screen.blit(Images.right_close, (self.x, self.y))
    def get_coordinate(self):
        return self.x,self.y
    def move(self):
        if self.direction == Direction.up:
            self.y -= self.speed
        elif self.direction == Direction.down:
            self.y += self.speed
        elif self.direction == Direction.left:
            self.x -= self.speed
        elif self.direction == Direction.right:
            self.x += self.speed
    def calculate_new_coordinates(self):
        if self.direction == Direction.up:
            return (self.x,self.y - self.speed)
        elif self.direction == Direction.down:
            return (self.x,self.y + self.speed)
        elif self.direction == Direction.left:
            return (self.x - self.speed,self.y)
        elif self.direction == Direction.right:
            return (self.x + self.speed,self.y)