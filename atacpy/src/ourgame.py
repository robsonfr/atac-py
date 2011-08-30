import pygame, sys, random
from engine.graphics import Sprite
from engine import data_load, Game        
from atacpy import Star, Nave, Intro, GamePlay

class Ourgame(Game):
    
    def __init__(self):
        Game.__init__(self,'intro')
        self.estados = {'intro' : Intro(self), 'gameplay' : GamePlay(self)}
        self.fundo = data_load("fundo2.png")
        self.num_estrelas = 40
        self.scripts = data_load("atacc.yml")


    def end_game(self):
        sys.exit()

    def load_bitmaps(self):
        self.background = pygame.Surface(self.screen_size)
        self.nave = Nave()
        self.navInimiga = Sprite(data_load("new_nave_inimig.png"))
        self.etelg = Sprite(data_load("ETELG.png"))
        self.navInimiga.baseX = random.random() * 428 + 20 
        self.navInimiga.move_to(200, 0)
        self.background.fill((0, 0, 0))
        self.stars = [Star(self.screen_size) for _ in xrange(self.num_estrelas)]
                            

if __name__ == "__main__":
    jogo = Ourgame()
    jogo.load_bitmaps()
    jogo.game_loop()    
