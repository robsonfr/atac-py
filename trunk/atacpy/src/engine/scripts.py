'''
Created on 30/08/2011

@author: robson
'''
from engine import data_load
from graphics import Sprite

class Script(object):
    
    def __init__(self, script_name, game_obj):
        self.commands = data_load(script_name + ".yml")
        self.game_object = game_obj
        self.sprite_list = {}
        for k in dir(self.game_object):
            if isinstance(k,Sprite):
                self.sprite_list[k.__name__] = self.game_object
        
    def start(self, state_name):
        self.current = self.commands[state_name]
        
    def run(self):
        for i in self.current:
            pass
            
        