import pygame, sys, os, math, random;
from pygame.locals import *;
from engine.graphics import Sprite;
    
class dataloader:
    
    def load(self, filename):
        ext = filename[-3:].lower()
        
        if ext in ("png", "gif", "jpg", "jpeg"):
            return pygame.image.load(os.path.join("data", "images", filename))
        elif ext in ("wav", "ogg", "mp3"):
            return pygame.mixer.Sound(os.path.join("data", "sound", filename))
        else:
            return;        

class star:
    
#    modificadores = [0.25, 0.25, 0.05, 0.20, 0, 0.10, 0.05, 0.05, 0.05]
    
    def __reset(self):
        self.x = random.randint(0,self.max_x - 1)
        self.y = random.randint(0,self.max_y - 1)
        self.color = Color(random.randint(0,255) * 16843008)
    
    def __init__(self, (max_x, max_y)):
        self.max_x = max_x;
        self.max_y = max_y
        self.__reset()
        self.speed = random.randint(2,5)

    def draw(self, target):              
        target.set_at((self.x, self.y), self.color)

        if self.y + self.speed >= target.get_height():
            old_y = self.y
            self.__reset()
            self.y = old_y
        self.y = (self.y + self.speed) % target.get_height() 

class ourgame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()        
        self.screenSize = (640, 480)
        self.situacao = [0, 0, 0, 0, 0, 0]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.fundo = dataloader().load("fundo2.png")
        self.num_estrelas = 40
        self.som_tiro = dataloader().load("ourgame_fx1.ogg")
        pygame.mouse.set_visible(False)

    def loadBitmaps(self):
        self.background = pygame.Surface(self.screenSize)
        self.sprite = Sprite(dataloader().load("new_nave.png"))
        self.padraoTiro = Sprite(dataloader().load("random.png"))
        self.navInimiga = Sprite(dataloader().load("new_nave_inimig.png"))
        self.posTiroX = 0
        self.posTiroY = 480
        self.limTiroY = 0
        self.navInimiga.baseX = random.random() * 428 + 20 
        self.sprite.moveTo(100, 440)
        self.navInimiga.moveTo(200, 0)
        #self.background.fill((66,99,255))
        self.background.fill((0, 0, 0))
        self.stars = []
        for i in range(0, self.num_estrelas):
            self.stars.append(star(self.screenSize))

    
    def introScreen(self):
        pass
    
    def gamePlay(self):
        pass
    
    def credits(self):
        pass
    
    def input(self, event):
        if event.type == QUIT:
            sys.exit()        
        if event.type == KEYDOWN:
            if event.key == 27: # ESCAPE
                self.situacao[5] = 1
            if event.key == 97: # A
                self.situacao[0] = 1
            if event.key == 100: #D
                self.situacao[1] = 1
            if event.key == 119: #W
                self.situacao[2] = 1
            if event.key == 115: #S
                self.situacao[3] = 1
            if event.key == 32:
                print pygame.display.toggle_fullscreen()
            #print event.key
        if event.type == KEYUP:
            if event.key == 27: # ESCAPE
                self.situacao[5] = -1
            if event.key == 97: # A
                self.situacao[0] = 0
            if event.key == 100: #D
                self.situacao[1] = 0
            if event.key == 119: #W
                self.situacao[2] = 0
            if event.key == 115: #S
                self.situacao[3] = 0
            
    def updateScreen(self):
        
        if self.situacao[0] == 1 and self.sprite.x >= 20 + self.sprite.stepx:
            self.sprite.x -= self.sprite.stepx    
        elif self.situacao[1] == 1 and self.sprite.x <= 448 - self.sprite.stepx:
            self.sprite.x += self.sprite.stepx    
            
        if self.situacao[2] == 1 and self.posTiroY == 480:
            self.posTiroY -= 20
            self.som_tiro.play(loops=-1)
            self.posTiroX = self.sprite.x + 14
            self.padraoTiro.x = self.sprite.x + 14
            self.limTiroY = self.navInimiga.y - 16
            if self.limTiroY < 0:
                self.limTiroY = 0
            
    
        #
        #if self.situacao[2] == 1 and self.sprite.y >= self.sprite.stepy:
        #    self.sprite.y -= self.sprite.stepy
        #elif self.situacao[3] == 1 and self.sprite.y <= 464-self.sprite.stepy:
        #    self.sprite.y += self.sprite.stepy
            
        if self.situacao[5] == -1:
            sys.exit()

        yy = self.navInimiga.y + 1
        if yy == 480:
            yy = 0
            self.navInimiga.baseX += random.random() * 200 - 100
            if self.navInimiga.baseX < 0:
                self.navInimiga.baseX = 0
            if self.navInimiga.baseX > 448:
                self.navInimiga.baseX = 448 
        xx = self.navInimiga.baseX + math.cos(math.radians(yy * 6)) * 70
        self.navInimiga.moveTo(xx, yy)    
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.fundo, (0,0))
        for st in self.stars: st.draw(self.screen)
        
        self.sprite.draw(self.screen)
        self.navInimiga.draw(self.screen)
        
        if self.posTiroY < 480 and self.posTiroY > 0:            
            self.padraoTiro.x = self.sprite.x + 14
            self.padraoTiro.y = self.posTiroY + 40
            self.padraoTiro.drawFragment(self.screen, Rect(random.random() * 630, self.posTiroY, 4, 480 - self.posTiroY))
            self.posTiroY -= 10
            
        
        if self.posTiroY <= self.limTiroY:
            self.posTiroY = 480
            self.som_tiro.stop()
        
        pygame.display.flip()
                
                    
    def gameloop(self):
        while True:
            for e in pygame.event.get():
                self.input(e)
            self.updateScreen()
            pygame.time.wait(20)
    

if __name__ == "__main__":
    jogo = ourgame()
    jogo.loadBitmaps()
    jogo.gameloop()    
