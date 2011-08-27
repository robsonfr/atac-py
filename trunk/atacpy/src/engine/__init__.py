"""Pacote com modulos e classes para a construcao de jogos
Um 'engine' basico
"""
from pygame import image, mixer, surface
from pygame.locals import KEYDOWN, KEYUP, QUIT, Rect
from engine.graphics import Layer, Sprite
from pygame.transform import smoothscale
import os, sys, pygame, yaml

def data_load(filename):
    ext = filename[-3:].lower()
    
    if ext in ("png", "gif", "jpg", "jpeg"):
        return image.load(os.path.join("data", "images", filename))
    elif ext in ("wav", "ogg", "mp3"):
        return mixer.Sound(os.path.join("data", "sound", filename))
    else:
        return;

class Config(object):

    def load(self, filename):
        pass
        
    def save(self, filename):
        pass

class Estado(object):
    
    def __init__(self, game_object):
        self.go = game_object
    
    def __iter__(self):
        return self
    
    def perform(self):
        pass
    
    def next(self):
        return self

class Fim(Estado):
                
    def next(self):
        raise StopIteration        
    
class Player(Layer):
    
    def __init__(self, sprite_file, ini_pos=(0, 0)):
        self.sprite = Sprite(data_load(sprite_file))
        self.sprite.move_to(ini_pos[0], ini_pos[1])
        Layer.__init__(self, (self.sprite.x, self.sprite.y), self.sprite.size)
    
    def move_to(self, x, y):
        self.sprite.move_to(x, y)
        return self
    
    def draw(self, target):
        self.sprite.draw(target)
        
    def move_x(self, dx=1):
        if dx < 0 and self.sprite.x >= 20 + self.sprite.step_x: self.sprite.x -= self.sprite.step_x
        elif dx > 0 and self.sprite.x <= 448 - self.sprite.step_x: self.sprite.x += self.sprite.step_x             
    
class Game(object):
    """Classe generica para jogos
    """
    situacao = [0, 0, 0, 0, 0, 0]

    
    def _fullscreen(self):
        if self.fullscreen:            
            self.f_screen = pygame.display.set_mode(self.fullscreen_size, pygame.locals.FULLSCREEN, 32)
            fator = self.f_screen.get_height() / 480.0
            
            self.f_size = (int(640 * fator), int(480 * fator))
            self.scaled = surface.Surface(self.f_size, 32)
            self.px = 840 - self.f_size[0] / 2
        else:
            self.f_screen = pygame.display.set_mode(self.screen_size, 0)
 
    
    def __init__(self, e_inicial=""):
        self.estados = {}
        self.estado_inicial = e_inicial

        pygame.init()
        pygame.mixer.init()        
        self.screen_size = (640, 480)
        self.fullscreen_size = (1680, 1050)
        pygame.mouse.set_visible(False)
        self.screen = surface.Surface(self.screen_size,32)
#        modes = pygame.display.list_modes(32)
        self.fullscreen = True
        self._fullscreen()
                       
    def fsm_loop(self):
        e = self.estados[self.estado_inicial]
        prox = e
        for p in prox:
            yield p

    def end_game(self):
        pass

    def input(self, event):
        if event.type == QUIT:
            self.end_game();        
        if event.type == KEYDOWN:
            if event.key == 27: # ESCAPE
                Game.situacao[5] = 1
            if event.key == 97: # A
                Game.situacao[0] = 1
            if event.key == 100: #D
                Game.situacao[1] = 1
            if event.key == 119: #W
                Game.situacao[2] = 1
            if event.key == 115: #S
                Game.situacao[3] = 1
            if event.key == 32:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    pass
                else:
                    pass
                
            #print event.key
        if event.type == KEYUP:
            if event.key == 27: # ESCAPE
                Game.situacao[5] = -1
            if event.key == 97: # A
                Game.situacao[0] = 0
            if event.key == 100: #D
                Game.situacao[1] = 0
            if event.key == 119: #W
                Game.situacao[2] = 0
            if event.key == 115: #S
                Game.situacao[3] = 0
                
    def game_loop(self):
        maquina_estados = self.fsm_loop()
        for estado in maquina_estados:
            for e in pygame.event.get():
                self.input(e)
            if Game.situacao[5] == -1: self.end_game()
            estado.perform()
            if self.fullscreen:
                smoothscale(self.screen, self.f_size, self.scaled)
                self.f_screen.blit(self.scaled, (self.px,0))
            else:
                self.f_screen.blit(self.screen, (0,0))
            pygame.display.flip()
            pygame.time.wait(20)
        
