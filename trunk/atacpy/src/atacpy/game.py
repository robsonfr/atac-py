'''
Created on 15/01/2012

@author: robson
'''
import random
from pygame.locals import Color, Rect
from engine.graphics import Layer, Sprite
from engine import data_load, Player, Estado, Game
import math

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
        self.som_tiro = data_load("ourgame_fx1.ogg")
        self.disparando = False
       
    def draw(self, target, x):        
        self.padrao_tiro.x = x
        self.padrao_tiro.y = self.y + 40
        self.padrao_tiro.draw_fragment(target, Rect(random.random() * 630, self.y, 4, 480 - self.y))
        self.y -= 20
        if self.y <= self.lim_y:
            self.y = 480
            self.disparando = False
            self.som_tiro.stop()

    def shoot(self, x, l_y=20):
        self.disparando = True
        self.y = 460
        self.x = x
        self.padrao_tiro.x = x
        self.lim_y = l_y
        self.som_tiro.play(loops=-1)
        

class Nave(Player):
    
    def __init__(self):        
        self.sprite = Sprite(data_load("new_nave.png"))
        self.sprite.move_to(100, 440)        
        Layer.__init__(self, (self.sprite.x, self.sprite.y), self.sprite.size)
        self.tiro = Tiro()

    def shoot(self):
        if not self.tiro.disparando:
            self.tiro.shoot(x=self.sprite.x + 14, l_y=20)
            
    def draw(self, target):
        Player.draw(self, target)
        if self.tiro.disparando: self.tiro.draw(target, self.sprite.x + 14)

class Intro(Estado):
    
    def __init__(self, game_object):
        Estado.__init__(self, game_object)
        self.etelg = Sprite(data_load("ETELG.png"))
        self._30anos = Sprite(data_load("30anos.png"))
        self._47anos = Sprite(data_load("47anos.png"))
        self.speed = 30
        self.counter = self.speed
        self.index = 0
        self.indices = {  }
        
    def next(self):
        return self.go.estados['gameplay']

class GamePlay(Estado):                
        
    def __call__(self):
    
        if Game.situacao[0] == 1:
            self.go.nave.move_x(-1)        
        elif Game.situacao[1] == 1:
            self.go.nave.move_x(1)
        
        if Game.situacao[2] == 1 and self.go.nave.tiro.y == 480:
            self.go.nave.shoot()
                    
        yy = self.go.navInimiga.y + 1
        if yy == 480:
            yy = 0
            self.go.navInimiga.baseX += random.random() * 200 - 100
            if self.go.navInimiga.baseX < 0:
                self.go.navInimiga.baseX = 0
            elif self.go.navInimiga.baseX > 448:
                self.go.navInimiga.baseX = 448 
        xx = self.go.navInimiga.baseX + math.cos(math.radians(yy * 6)) * 70
        self.go.navInimiga.move_to(xx, yy)    
        self.go.screen.blit(self.go.background, (0, 0))
        self.go.screen.blit(self.go.fundo, (0,0))
        for st in self.go.stars: st.draw(self.go.screen)
        
        self.go.nave.draw(self.go.screen)
        self.go.navInimiga.draw(self.go.screen)                
