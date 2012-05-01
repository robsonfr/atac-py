'''
Todas as classes relacionadas com graficos ficam aqui
Created on 31/12/2009

@author: Robson
'''

from pygame.locals import Rect

class Layer(object):
    """Uma camada (layer) de "algo" grafico a ser desenhado
       Todos tem em comum um comportamento chamado draw
       e outro chamado test_collision
    """ 
    def __init__(self, pos = (0,0), tam = (0,0)):
        self.x, self.y = pos
        self.size = tam
    
    @property    
    def dx(self):
        return self.x + self.size[0]    

    @property
    def dy(self):
        return self.y + self.size[1]

    def draw(self, target):
        pass
    
    def test_collision(self, layer):
        """Testa a colisao com outro Layer...
        """
        cx = (layer.x <= self.x <= layer.dx) or (self.x <= layer.x <= self.dx)
        cy = (layer.y <= self.y <= layer.dy) or (self.y <= layer.y <= self.dy)
        return cx and cy 
        
        
class Sprite(Layer):
    """Um sprite eh um objeto que se move dentro de um layer, mas
       nada impede que ele tambem seja um Layer ;)
    """
    def __init__(self, source, srcCorner=(0, 0), size=(32, 32)):
        self.srcCorner = srcCorner      
        self.step_x, self.step_y = 3, 0
        self.surface = source
        Layer.__init__(self, tam=size)
        
    def move_to(self, newX, newY):
        self.x, self.y = newX, newY
        
    def draw(self, target):
        target.blit(self.surface, (self.x, self.y))

    def draw_fragment(self, target, area):
        target.blit(self.surface, (self.x, self.y), area)


class AnimatedSprite(Sprite):
    """Um sprite animado eh um sprite que segue uma regra de animacao
    """
    def __init__(self, source, srcCorner=(0,0), size=(32,32), num_of_frames=1, frames_per_second = 60, hor_step=32, ver_step=0): 
        Sprite.__init__(self, srcCorner, size)
        self.h_s = hor_step
        self.v_s = ver_step
        self.fps = 1000.0 / frames_per_second
        self.frames = num_of_frames
        self.curr_frame = 0
        
    def get_curr_frame(self):
        s, self.curr_frame = self.curr_frame, self.curr_frame + 1
        if self.curr_frame == self.frames: self.curr_frame = 0
        return s 
    
    def _calc_area(self):
        f = self.get_curr_frame()
        s = self.srcCorner
        h = self.h_s
        v = self.v_s
        if self.hor_step <> 0:
            return Rect(s[0] + h * f, s[1], self.size[0], self.size[1])
        else:    
            return Rect(s[0], s[1] + v * f, self.size[0], self.size[1])
            
        
    def draw(self, target):
        Sprite.draw_fragment(self, target, self._calc_area())
        
    area = property(_calc_area)
    
class Bitmap(Layer):
    
    def __init__(self, imageFile, xyCoord=(0, 0), effect=0): 
        pass


class Font(Sprite):

    def __init__(self,source):
        pass