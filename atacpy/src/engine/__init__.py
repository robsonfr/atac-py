"""Pacote com modulos e classes para a construcao de jogos
Um 'engine' basico
"""
from pygame import image, mixer
from pygame.locals import KEYDOWN, KEYUP, QUIT
from engine.graphics import Layer
import os, sys, pygame

def data_load(filename):
    ext = filename[-3:].lower()
    
    if ext in ("png", "gif", "jpg", "jpeg"):
        return image.load(os.path.join("data", "images", filename))
    elif ext in ("wav", "ogg", "mp3"):
        return mixer.Sound(os.path.join("data", "sound", filename))
    else:
        return;

class Fim:
    
    def perform(self):
        pass
        
    def next_state(self):
        return None

class GameElement(Layer):
    def __init__(self, sprite=None, pos=(0,0), tam=(0,0)):
        Layer.__init__(self, pos, tam)
        self.sprite = sprite
        
    
class Game:
    """Classe generica para jogos
    """
    situacao = [0, 0, 0, 0, 0, 0]
    def __init__(self):
        self.estados = [Fim()]

        pygame.init()
        pygame.mixer.init()        
        self.screenSize = (640, 480)
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(self.screenSize)
            
    def fsm_loop(self, estado_inicial = None):
        if estado_inicial is None: estado_inicial = self.estados[0]
        prox = estado_inicial
        while prox is not None:
            yield prox
            prox = prox.next_state()

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
                print pygame.display.toggle_fullscreen()
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