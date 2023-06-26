import pygame
from constantes import *


class Prize:
    def __init__(self,x,y,width,height,quantity,path) -> None:
        self.image = pygame.image.load(PATH_IMAGE+path)
        self.image = pygame.transform.scale(self.image,(width,height))        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.quantity = quantity




    def draw(self, screen):
            if DEBUG:
                pygame.draw.rect(screen, BLUE, self.rect) 
            screen.blit(self.image, self.rect)