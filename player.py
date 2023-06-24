from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar
from balas import *
from enemigo import Enemigo

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,jump_height,frame_rate_ms,move_rate_ms) -> None:
        character_width = CHARACTER_ANCHO
        character_height = CHARACTER_ALTO
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\walk.png",10,1,character_width,character_height)[:]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\walk.png",10,1,character_width,character_height,True)[:]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\idle_new.png",11,1,character_width,character_height)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\idle_new.png",11,1,character_width,character_height, True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\jump_newt.png",12,2,character_width,character_height,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\jump_newt.png",12,2,character_width,character_height,True)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\hit_hand_1.png",12,1,character_width,character_height,False)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\hit_hand_1.png",12,1,character_width,character_height,True)
        self.direction = DIRECTION_L
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.attack_value = 1
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.tiempo_transcurrido_animation = 0
        self.rate_frames_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.rect_corrected = pygame.Rect(self.rect.x+100,self.rect.y-100 + self.rect.h-50,self.rect.w/3,120 )
        self.rect_ground_collition = pygame.Rect(self.rect.x+130,self.rect.y+10 + self.rect.h-50,self.rect.w/6,GROUND_RECT_H )
        self.bullets = []
        self.is_shooting = False
        self.hitting = False

    def walk(self,direction):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
        

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self, delta_ms, lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.set_x(self.move_x)
            self.set_y(self.move_y)

            if not self.is_on_platform(lista_plataformas) and self.rect.y < GROUND_LEVEL:
                self.set_y(self.gravity)
            elif self.is_jump:
                if self.is_on_platform(lista_plataformas):
                    self.jump(False)
                else:
                    self.set_y(self.gravity)

    def is_on_platform(self, lista_plataformas):
        if self.rect.y == 540:
            return True

        for plataforma in lista_plataformas:
            if self.rect_ground_collition.colliderect(plataforma.rect_ground_collision):
                return True

        return False
    
    def hit_enemy(self, enemigo):
        if self.animation == self.hit_r or self.animation == self.hit_l:  # Verificar si el jugador está realizando un golpe
            if self.rect_corrected.colliderect(enemigo.rect):  # Verificar colisión entre el jugador y el enemigo
                return True
        return False
    
    def hurting_enemy(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.hit_enemy(enemigo):
                if enemigo.health > 0:
                    enemigo.hurt(self.attack_value)
                    if enemigo.health <= 0:
                        enemigo.animation = enemigo.dead_animation
                        pygame.time.set_timer(pygame.USEREVENT, 2000)
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'enemy': enemigo}))



    def hit(self, on_off):
        if (on_off == True and self.hitting == False):
            if (self.direction == DIRECTION_R):
                self.animation = self.hit_r
            else:
                self.animation = self.hit_l
            self.frame = 0
            self.hitting = True
        else:
            self.hitting = False
            self.animation = self.stay()
#HOLA
    def shoot(self, on_off):
        if (on_off and not self.is_shooting):
            self.is_shooting = True
            
            bullet = Bullet(self.rect_corrected.centerx, self.rect_corrected.centery, self.direction)
            self.bullets.append(bullet)
        if not on_off:
            self.is_shooting = False

        self.update_bullets()

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.update()



    def set_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_corrected.x += delta_x
        self.rect_ground_collition.x += delta_x
    
    def set_y (self, delta_y):
        self.rect.y += delta_y 
        self.rect_corrected.y += delta_y        
        self.rect_ground_collition.y += delta_y

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.rate_frames_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0



    def update(self,delta_ms, lista_plataformas,lista_enemigos):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
        self.hurting_enemy(lista_enemigos)
        if self.is_shooting:
            self.shoot(True)
        
        self.update_bullets()
    
    def draw_bullets(self, screen):
        if self.is_shooting:
            for bullet in self.bullets:
                bullet.draw(screen)
        
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect_corrected)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        self.draw_bullets(screen)



