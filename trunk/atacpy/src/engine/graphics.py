'''
Todas as classes relacionadas com graficos ficam aqui
Created on 31/12/2009

@author: Robson
'''

class Layer:
    """Uma camada (layer) de "algo" grafico a ser desenhado
       Todos tem em comum um comportamento chamado draw
       e outro chamado test_collision
    """ 
    def __init__(self, pos = (0,0), tam = (0,0)):
        self.x, self.y = pos
        self.size = tam
        
    def dx(self):
        return self.x + self.size[0]    

    def dy(self):
        return self.y + self.size[1]

    def draw(self, target):
        pass
    
    def test_collision(self, layer):
        """Testa a colisao com outro Layer...
        """
        return ((layer.x <= self.x <= layer.dx()) or (self.x <= layer.x <= self.dx())) and ((layer.y <= self.y <= layer.dy()) or (self.y <= layer.y <= self.dy())) 
        
        
class Sprite(Layer):
    """Um sprite eh um objeto que se move dentro de um layer, mas
       nada impede que ele tambem seja um Layer ;)
    """
    def __init__(self, source, srcCorner=(0, 0), size=(32, 32)):
        self.srcCorner = srcCorner
        self.size = size
        self.x, self.y = 0, 0
        self.stepx, self.stepy = 3, 0
        self.surface = source
        
    def move_to(self, newX, newY):
        self.x, self.y = newX, newY
        
    def draw(self, target):
        target.blit(self.surface, (self.x, self.y))

    def draw_fragment(self, target, area):
        target.blit(self.surface, (self.x, self.y), area)
        
class Bitmap(Layer):
    
    def __init__(self, imageFile, xyCoord=(0, 0), effect=0): 
        pass

