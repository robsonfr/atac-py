import pygame, sys, random
from engine.graphics import Sprite
from engine import data_load, Game        
from atacpy import Star, Nave, GamePlay

class Ourgame(Game):
    
    def __init__(self):
        Game.__init__(self)
        self.estados = [GamePlay(self)]
        self.fundo = data_load("fundo2.png")
        self.num_estrelas = 40
        self.som_tiro = data_load("ourgame_fx1.ogg")


    def end_game(self):
        sys.exit()

    def load_bitmaps(self):
        self.background = pygame.Surface(self.screenSize)
        self.nave = Nave()
        self.navInimiga = Sprite(data_load("new_nave_inimig.png"))
        self.navInimiga.baseX = random.random() * 428 + 20 
        self.navInimiga.move_to(200, 0)
        self.background.fill((0, 0, 0))
        self.stars = [Star(self.screenSize) for _ in xrange(self.num_estrelas)]
                            

if __name__ == "__main__":
    jogo = Ourgame()
    jogo.load_bitmaps()
    jogo.game_loop()    
