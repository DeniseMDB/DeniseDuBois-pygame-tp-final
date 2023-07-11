import pygame
from constantes import *
from auxiliar import Auxiliar

class Plataform:
    def __init__(self, x, y, w, h, path,type_move=False, type_h_v=0, limit_top=None, limit_bottom=None) -> None:
        self.image = pygame.image.load("C:\\Users\\Denise\\Desktop\\MyGame\\Assets\\" + path)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collision = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.type_moves = type_move
        self.move_h_v = type_h_v
        self.velocity = 0.2  # Velocidad de movimiento de la plataforma
        self.limit_top = limit_top
        self.limit_bottom = limit_bottom
        self.goes_up = False
        self.goes_down = False

    def update(self):
        if self.type_moves == True:
            if self.move_h_v == 0: # se mueve en y
                self.rect.x += self.velocity
                self.rect_ground_collision.x += self.velocity
                if self.rect.left < 0 or self.rect.right > ANCHO_VENTANA:
                    self.velocity = -self.velocity
            else:
                if self.limit_top is not None and self.limit_bottom is not None:
                    if self.rect.y <= self.limit_top or self.rect.y >= self.limit_bottom:
                        self.velocity = -self.velocity
                        self.goes_up = True
                        self.goes_down = False
                self.rect.y += self.velocity
                self.rect_ground_collision.y += self.velocity
                self.goes_down = True
                self.goes_up = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collision)
