import random
from pygame.locals import Color
from engine.graphics import Layer

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

