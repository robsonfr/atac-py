import random
from pygame.locals import Color, Rect
from engine.graphics import Layer, Sprite
from engine import data_load

class Star(Layer):
    
#    modificadores = [0.25, 0.25, 0.05, 0.20, 0, 0.10, 0.05, 0.05, 0.05]
    
    def __reset(self):
        self.x = random.randint(0,self.max_x - 1)
        self.y = random.randint(0,self.max_y - 1)
        self.color = Color(random.randint(0,255) * 16843008)
    
    def __init__(self, (max_x, max_y)):        
        self.max_x = max_x
        self.max_y = max_y
        self.__reset()
        Layer.__init__(self, (self.x, self.y), (1,1))
        self.speed = random.randint(2,5)

    def draw(self, target):              
        target.set_at((self.x, self.y), self.color)

        if self.y + self.speed >= target.get_height():
            old_y = self.y
            self.__reset()
            self.y = old_y
        self.y = (self.y + self.speed) % target.get_height() 

class Tiro(Layer):
    
    def __init__(self, pos = (0,480), lim_y = 480):
        self.padrao_tiro = Sprite(data_load("random.png"))
        self.x, self.y = pos
        self.lim_y = lim_y
    
    def draw(self, target):    
        self.padrao_tiro.draw_fragment(target, Rect(random.random() * 630, self.y, 4, 480 - self.y))

class Nave(Layer):
    
    def __init__(self):        
        self.sprite = Sprite(data_load("new_nave.png"))
        self.sprite.move_to(100, 440)        
        Layer.__init__(self, (self.sprite.x, self.sprite.y), self.sprite.size)
        self.tiro = Tiro()

    def move_to(self, x, y):
        self.sprite.move_to(x,y)
        return self
    
    def draw(self, target):
        self.sprite.draw(target)
        
    def move_x(self, dx=1):
        if dx < 0 and self.sprite.x >= 20 + self.sprite.step_x: self.sprite.x -= self.sprite.step_x
        elif dx > 0 and self.sprite.x <= 448 - self.sprite.step_x: self.sprite.x += self.sprite.step_x 