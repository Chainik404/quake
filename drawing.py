import pygame 
from settings import *
from ray_casting import ray_casting

class Drawing:
    def __init__(self):
        self.sc = sc
        
    def background(self, sc):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))