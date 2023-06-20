from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,jump_height,frame_rate_ms,move_rate_ms) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\walk.png",10,1)[:]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\walk.png",10,1,True)[:]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\idle_new.png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\idle_new.png",11,1, True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\jump_newt.png",12,2,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\jump_newt.png",12,2,True)
        self.direction = DIRECTION_L
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
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
        self.rect_corrected = pygame.Rect(self.rect.x+130,self.rect.y-160 + self.rect.h-50,self.rect.w/3,160 )
        self.rect_ground_collition = pygame.Rect(self.rect.x+130,self.rect.y + self.rect.h-50,self.rect.w/3,GROUND_RECT_H )


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

    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.set_x(self.move_x)
            self.set_y(self.move_y)

            if(self.is_on_platform(lista_plataformas) == False):
                self.set_y(self.gravity)
            elif(self.is_jump): 
                self.jump(False)

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break
        return retorno

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



    def update(self,delta_ms, lista_plataformas):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,RED,self.rect_corrected)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


