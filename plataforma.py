import pygame
from constantes import *
from auxiliar import Auxiliar

class Plataform:
    def __init__(self, x, y, w, h, path, type=0, type_h_v=0, limit_top=None, limit_bottom=None) -> None:
        self.image = pygame.image.load("C:\\Users\\Denise\\Desktop\\MyGame\\Assets\\" + path)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collision = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.type = type
        self.move_h_v = type_h_v
        self.velocity = 1.5  # Velocidad de movimiento de la plataforma
        self.limit_top = limit_top
        self.limit_bottom = limit_bottom

    def update(self):
        if self.type == 1:
            if self.move_h_v == 0: # Tipo de plataforma que se mueve en el eje X o Y
                self.rect.x += self.velocity
                self.rect_ground_collision.x += self.velocity
                if self.rect.left < 0 or self.rect.right > ANCHO_VENTANA:
                    self.velocity = -self.velocity
            else:
                if self.limit_top is not None and self.limit_bottom is not None:
                    if self.rect.y <= self.limit_top or self.rect.y >= self.limit_bottom:
                        self.velocity = -self.velocity
                self.rect.y += self.velocity
                self.rect_ground_collision.y += self.velocity
#HOLA

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collision)
