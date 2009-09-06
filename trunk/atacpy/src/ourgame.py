import pygame, sys, os, math, random;
from pygame.locals import *;

class gameobject:
	
	def __init__(self, source, srcCorner = (0,0), size = (32,32)):
		self.srcCorner = srcCorner
		self.size = size
		self.x = 0
		self.y = 0
		self.stepx, self.stepy = 3,0
		self.surface = source
		
	def moveTo(self, newX, newY):
		self.x, self.y = newX, newY
		
	def draw(self, target):
		target.blit(self.surface, (self.x, self.y))

class bitmapscreen:
	
	def __init__(self, imageFile, xyCoord = (0,0), effect = 0): 
		pass
	
class dataloader:
	
	def load(self, filename):
		ext = filename[-3:].lower()
		
		if ext in ("png", "gif", "jpg", "jpeg"):
			return pygame.image.load(os.path.join("data","images",filename))
		elif ext in ("wav", "ogg", "mp3"):
			return;
		else:
			return;		


class ourgame:
	
	def __init__(self):
		pygame.init();		
		self.screenSize = (800,600)
		self.situacao = [0,0,0,0,0,0]
		self.screen = pygame.display.set_mode(self.screenSize, FULLSCREEN | HWSURFACE)
		pygame.mouse.set_visible(False)
	   
	   
	def loadBitmaps(self):
		self.background = pygame.Surface(self.screenSize)
		self.sprite = gameobject(dataloader().load("new_nave.png"))
		self.navInimiga = gameobject(dataloader().load("new_nave_inimig.png"))
		self.navInimiga.baseX = random.random() * 428 + 20 
		self.sprite.moveTo(100,440)
		self.navInimiga.moveTo(200,0)
		self.background.fill((66,99,255))
	
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
		
		if self.situacao[0] == 1 and self.sprite.x >= 20+self.sprite.stepx:
			self.sprite.x -= self.sprite.stepx	
		elif self.situacao[1] == 1 and self.sprite.x <= 448-self.sprite.stepx:
			self.sprite.x += self.sprite.stepx	
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
		self.navInimiga.moveTo(xx,yy)	
		self.screen.blit(self.background, (0,0))
		self.sprite.draw(self.screen)
		self.navInimiga.draw(self.screen)
		pygame.display.flip()
				
					
	def gameloop(self):
		while True:
			for e in pygame.event.get():
				self.input(e)
			self.updateScreen()
			pygame.time.wait(20)
	
jogo = ourgame()
jogo.loadBitmaps()
jogo.gameloop()	