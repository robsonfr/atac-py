import pygame, sys, math, random
from pygame.locals import Rect
from engine.graphics import Sprite
from engine import data_load, Game        
from atacpy import Star

class Ourgame(Game):
    
    def __init__(self):
        Game.__init__(self)
        
        self.fundo = data_load("fundo2.png")
        self.num_estrelas = 40
        self.som_tiro = data_load("ourgame_fx1.ogg")


    def load_bitmaps(self):
        self.background = pygame.Surface(self.screenSize)
        lista_figuras = ["new_nave.png", "random.png","new_nave_inimig.png"]
        self.sprite, self.padraoTiro, self.navInimiga = [Sprite(data_load(f)) for f in lista_figuras]
        self.posTiroX = 0
        self.posTiroY = 480
        self.limTiroY = 0
        self.navInimiga.baseX = random.random() * 428 + 20 
        self.sprite.move_to(100, 440)
        self.navInimiga.move_to(200, 0)
        #self.background.fill((66,99,255))
        self.background.fill((0, 0, 0))
        self.stars = [Star(self.screenSize) for _ in xrange(self.num_estrelas)]

    
    def introScreen(self):
        pass
    
    def gamePlay(self):
        pass
    
    def credits(self):
        pass
    
    def end_game(self):
        sys.exit()
            
    def updateScreen(self):
        
        if Game.situacao[0] == 1 and self.sprite.x >= 20 + self.sprite.stepx:
            self.sprite.x -= self.sprite.stepx    
        elif Game.situacao[1] == 1 and self.sprite.x <= 448 - self.sprite.stepx:
            self.sprite.x += self.sprite.stepx    
            
        if Game.situacao[2] == 1 and self.posTiroY == 480:
            self.posTiroY -= 20
            self.som_tiro.play(loops=-1)
            self.posTiroX = self.sprite.x + 14
            self.padraoTiro.x = self.sprite.x + 14
            self.limTiroY = self.navInimiga.y - 16
            if self.limTiroY < 0:
                self.limTiroY = 0
            
    
        #
        #if Game.situacao[2] == 1 and self.sprite.y >= self.sprite.stepy:
        #    self.sprite.y -= self.sprite.stepy
        #elif Game.situacao[3] == 1 and self.sprite.y <= 464-self.sprite.stepy:
        #    self.sprite.y += self.sprite.stepy
            
        if Game.situacao[5] == -1:
            sys.exit()

        yy = self.navInimiga.y + 1
        if yy == 480:
            yy = 0
            self.navInimiga.baseX += random.random() * 200 - 100
            if self.navInimiga.baseX < 0:
                self.navInimiga.baseX = 0
            elif self.navInimiga.baseX > 448:
                self.navInimiga.baseX = 448 
        xx = self.navInimiga.baseX + math.cos(math.radians(yy * 6)) * 70
        self.navInimiga.move_to(xx, yy)    
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.fundo, (0,0))
        for st in self.stars: st.draw(self.screen)
        
        self.sprite.draw(self.screen)
        self.navInimiga.draw(self.screen)
        
        if self.posTiroY < 480 and self.posTiroY > 0:            
            self.padraoTiro.x = self.sprite.x + 14
            self.padraoTiro.y = self.posTiroY + 40
            self.padraoTiro.draw_fragment(self.screen, Rect(random.random() * 630, self.posTiroY, 4, 480 - self.posTiroY))
            self.posTiroY -= 10
            
        
        if self.posTiroY <= self.limTiroY:
            self.posTiroY = 480
            self.som_tiro.stop()
        
        pygame.display.flip()
                
                    
    def game_loop(self):
        while True:
            for e in pygame.event.get():
                self.input(e)
            self.updateScreen()
            pygame.time.wait(20)
    

if __name__ == "__main__":
    jogo = Ourgame()
    jogo.load_bitmaps()
    jogo.game_loop()    
