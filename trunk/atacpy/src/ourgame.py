import pygame, sys, os, math, random, numpy, engine;
from pygame.locals import *;
from engine.graphics import bitmapscreen, sprite;
	
class dataloader:
	
	def load(self, filename):
		ext = filename[-3:].lower()
		
		if ext in ("png", "gif", "jpg", "jpeg"):
			return pygame.image.load(os.path.join("data", "images", filename))
		elif ext in ("wav", "ogg", "mp3"):
			return;
		else:
			return;		


class ourgame:
	
	def __init__(self):
		pygame.init();		
		self.screenSize = (640, 480)
		self.situacao = [0, 0, 0, 0, 0, 0]
		self.screen = pygame.display.set_mode(self.screenSize, HWSURFACE)
		pygame.mouse.set_visible(False)
	   
	   
	def loadBitmaps(self):
		self.background = pygame.Surface(self.screenSize)
		self.sprite = sprite(dataloader().load("new_nave.png"))
		self.padraoTiro = sprite(dataloader().load("random.png"))
		self.navInimiga = sprite(dataloader().load("new_nave_inimig.png"))
		self.posTiroX = 0
		self.posTiroY = 480
		self.limTiroY = 0
		self.navInimiga.baseX = random.random() * 428 + 20 
		self.sprite.moveTo(100, 440)
		self.navInimiga.moveTo(200, 0)
		#self.background.fill((66,99,255))
		self.background.fill((0, 0, 0))
	
	def introScreen():
		pass
	
	def gamePlay():
		pass
	
	def credits():
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
			self.posTiroX = self.sprite.x + 14
			self.padraoTiro.x = self.sprite.x + 14
			self.limTiroY = self.navInimiga.y - 16
			if self.limTiroY < 0:
				self.limTiroY = 0
			
	
		#
		#if self.situacao[2] == 1 and self.sprite.y >= self.sprite.stepy:
		#	self.sprite.y -= self.sprite.stepy
		#elif self.situacao[3] == 1 and self.sprite.y <= 464-self.sprite.stepy:
		#	self.sprite.y += self.sprite.stepy
			
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
		self.sprite.draw(self.screen)
		self.navInimiga.draw(self.screen)
		
		if self.posTiroY < 480 and self.posTiroY > 0:			
			self.padraoTiro.x = self.sprite.x + 14
			self.padraoTiro.y = self.posTiroY + 40
			self.padraoTiro.drawFragment(self.screen, Rect(random.random() * 630, self.posTiroY, 4, 480 - self.posTiroY))
			self.posTiroY -= 10
			
		
		if self.posTiroY <= self.limTiroY:
			self.posTiroY = 480
		
		pygame.display.flip()
				
					
	def gameloop(self):
		while True:
			for e in pygame.event.get():
				self.input(e)
			self.updateScreen()
			pygame.time.wait(20)
	

if __name__ == "__main__":
	print engine.__doc__
	jogo = ourgame()
	jogo.loadBitmaps()
	jogo.gameloop()	
