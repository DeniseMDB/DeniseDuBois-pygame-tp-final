import pygame
from auxiliar import Auxiliar
from constantes import *

class Enemigo:
    def __init__(self, x, y, health, total_health, speed_movement, frame_rate_ms, move_rate_ms, limite_right, limite_left,attack = 1):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Desktop\\MyGame\\Assets\\jellyfish_2.png",5, 2,80,80)[:9]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Desktop\\MyGame\\Assets\\jellyfish_2.png",5, 2,80,80, True)[:9]
        self.dead_animation = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"jelly_sprite.png",4,1,60,60)
        self.direction = DIRECTION_R
        self.speed_movement = speed_movement
        self.health = health
        self.total_health = total_health
        self.attack = attack
        self.can_move = True
        self.can_shoot = True
        self.is_alive = True
        self.animation = self.walk_r
        self.animation_list = None
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_collision = pygame.Rect(self.rect.centerx+30,self.rect.centery-10,self.rect.w/1.7,60 )
        self.tiempo_transcurrido_animation = 0
        self.rate_frames_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.limite_r = limite_right
        self.limite_l = limite_left

    def movement(self, delta_ms):
        if self.is_alive:
            self.tiempo_transcurrido_move += delta_ms
            if self.tiempo_transcurrido_move >= self.move_rate_ms:
                self.tiempo_transcurrido_move = 0
                if self.rect.x <= self.limite_r and self.rect.x >= self.limite_l:
                    if self.direction == DIRECTION_R:
                        if self.rect.x + self.speed_movement <= self.limite_r:
                            self.rect.x += self.speed_movement
                            self.rect_collision.x += self.speed_movement
                        else:
                            self.rect.x = self.limite_r
                            self.rect_collision.x = self.limite_r
                            self.direction = DIRECTION_L
                            self.animation = self.walk_l
                    else:
                        if self.rect.x - self.speed_movement >= self.limite_l:
                            self.rect.x -= self.speed_movement
                            self.rect_collision.x -= self.speed_movement
                        else:
                            self.rect_collision.x = self.limite_l
                            self.rect.x = self.limite_l
                            self.direction = DIRECTION_R
                            self.animation = self.walk_r

#HOLA

    def update(self, delta_ms):
        self.movement(delta_ms)
        self.do_animation(delta_ms)

    def do_animation(self, delta_ms):
        if self.is_alive:
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= self.rate_frames_ms:
                self.tiempo_transcurrido_animation = 0
                self.frame += 1
                if self.frame >= len(self.animation):
                    self.frame = 0
        self.frame=0
        
    def hurt(self,attack):
        if self.is_alive and self.health > 0:
            self.health -= attack
        if self.health < 0:
            self.animation = self.dead_animation
            self.frame = 0
            self.can_shoot = False
            self.can_move = False
            return self.is_alive == False
        
        else:
            return self.is_alive == True

    def draw(self, screen):
        if DEBUG:
            #pygame.draw.rect(screen, RED, self.rect)  # Opcional: dibujar el rectángulo del enemigo
            pygame.draw.rect(screen,BLUE,self.rect_collision)
        #print(self.health)
        print(self.is_alive)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
