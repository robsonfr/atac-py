"""Pacote com modulos e classes para a construcao de jogos
Um 'engine' basico
"""
from pygame import image, mixer
import os

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
   
class Game:
    """Classe generica para jogos
    """
           
    def __init__(self):
        self.estados = [Fim()]
                
            
    def fsm_loop(self, estado_inicial = None):
        if estado_inicial is None: estado_inicial = self.estados[0]
        prox = estado_inicial
        while prox is not None:
            yield prox
            prox = prox.next_state()
