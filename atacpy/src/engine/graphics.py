'''
Todas as classes relacionadas com graficos ficam aqui
Created on 31/12/2009

@author: Robson
'''

class Layer:
    """Uma camada (layer) de "algo" grafico a ser desenhado
       Todos tem em comum um comportamento chamado draw
    """ 
    def __init__(self):
        pass

class Sprite:
    """Um sprite eh um objeto que se move dentro de um layer
    """
    def __init__(self, source, srcCorner=(0, 0), size=(32, 32)):
        self.srcCorner = srcCorner
        self.size = size
        self.x, self.y = 0, 0
        self.stepx, self.stepy = 3, 0
        self.surface = source
        
    def moveTo(self, newX, newY):
        self.x, self.y = newX, newY
        
    def draw(self, target):
        target.blit(self.surface, (self.x, self.y))

    def drawFragment(self, target, area):
        target.blit(self.surface, (self.x, self.y), area)

class BitmapLayer:
    
    def __init__(self, imageFile, xyCoord=(0, 0), effect=0): 
        pass

