import pygame
from constantes import *

class Bullet:
    def __init__(self, x, y, direction):
        self.image = pygame.image.load("C:\\Users\\Denise\\Desktop\\MyGame\\Assets\\bubble2.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 10

    def update(self):
        if self.direction == DIRECTION_R:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #HOLA