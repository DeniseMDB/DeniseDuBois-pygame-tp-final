import pygame
from constantes import *
from auxiliar import Auxiliar
from balas import *
from enemigo import Enemigo
from plataforma import Plataform
import pygame.mixer

pygame.mixer.init()
sonido_disparo = pygame.mixer.Sound(PATH_IMAGE+"bubble_pop.mp3")
sonido_colision = pygame.mixer.Sound(PATH_IMAGE+"electricity_CUT.mp3")
sonido_muerte = pygame.mixer.Sound(PATH_IMAGE+"losing.mp3")
sonido_pegada = pygame.mixer.Sound(PATH_IMAGE+"bob_esponja_golpe.mp3")
sonido_enemigo_muerte = pygame.mixer.Sound(PATH_IMAGE+"fart_death.mp3")
recogiendo_frasco = pygame.mixer.Sound(PATH_IMAGE+"grabbing_jar.wav")


class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,jump_height,health,attack,frame_rate_ms,move_rate_ms) -> None:
        character_width = CHARACTER_ANCHO
        character_height = CHARACTER_ALTO
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"walk.png",10,1,character_width,character_height)[:]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"walk.png",10,1,character_width,character_height,True)[:]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"idle_new.png",11,1,character_width,character_height)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"idle_new.png",11,1,character_width,character_height, True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"jump_newt.png",12,2,character_width,character_height,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"jump_newt.png",12,2,character_width,character_height,True)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"hit_hand_1.png",12,1,character_width,character_height,False)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"hit_hand_1.png",12,1,character_width,character_height,True)
        self.hurt_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"hurt.png",14,1,character_width,character_height)[:]
        self.hurt_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"hurt.png",14,1,character_width,character_height,True)[:]
        self.final_hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"dead.png",39,1,character_width,character_height)[:]
        self.dead = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE+"dead.png",39,1,character_width,character_height)[17:]
        self.direction = DIRECTION_L
        self.frame = 0
        self.lives = 5
        self.is_alive = True
        self.health = health
        self.can_move = True
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.attack_value = attack
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.can_jump = True
        self.tiempo_transcurrido_animation = 0
        self.rate_frames_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.rect_corrected = pygame.Rect(self.rect.x+100,self.rect.y-100 + self.rect.h-50,self.rect.w/3,120 )
        self.rect_ground_collision = pygame.Rect(self.rect.x+100,self.rect.y+10 + self.rect.h-50,self.rect.w/3,GROUND_RECT_H )
        self.bullets = []
        self.is_shooting = False
        self.hitting = False
        self.win_prize = False
        self.is_fall = False

        self.min_x = MIN_X  # Coordenada x mínima permitida
        self.max_x = MAX_X  # Coordenada x máxima permitida
        self.min_y = MIN_Y  # Coordenada y mínima permitida
        self.max_y = MAX_Y  # Coordenada y máxima permitida




    def walk(self, direction):
        if self.is_alive and self.can_move:
            if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                self.direction = direction
                if direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

            # colision derecha
            if self.direction == DIRECTION_R and self.rect_corrected.x + self.rect_corrected.width >= self.max_x:
                self.move_x = 0
                self.rect.x = self.max_x - self.rect_corrected.width*2
                self.rect_corrected.x = self.max_x - self.rect_corrected.width
                self.rect_ground_collision.x = self.max_x - self.rect_corrected.width


            # colision iz
            if self.direction == DIRECTION_L and self.rect_corrected.x <= self.min_x:
                self.move_x = 0
                self.rect.x = self.min_x -100
                self.rect_corrected.x = self.min_x
                self.rect_ground_collision.x = self.min_x
        

    def jump(self,on_off = True):
        if self.is_alive and self.can_jump:
            if self.rect_corrected.y + self.jump_power > 40:
                if(on_off and self.is_jump == False and self.is_fall == False):
                    self.y_start_jump = self.rect.y
                    if(self.direction == DIRECTION_R):
                        self.move_x = int(self.move_x / 2)
                        self.move_y = -self.jump_power
                        self.animation = self.jump_r
                    else:
                        self.move_x = int(self.move_x / 2)
                        self.move_y = -self.jump_power
                        self.animation = self.jump_l
                    self.frame = 0
                    self.is_jump = True
                if(on_off == False):
                    self.is_jump = False
                    self.stay()



    def stay(self):
        if self.is_alive:
            if(self.animation != self.stay_r and self.animation != self.stay_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.stay_r
                else:
                    self.animation = self.stay_l
                self.move_x = 0
                self.move_y = 0
                self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_corrected.x += delta_x
        self.rect_ground_collision.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_corrected.y += delta_y
        self.rect_ground_collision.y += delta_y

    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect_corrected.y) > self.jump_height and self.is_jump) and self.rect_ground_collision.y < 700:
                self.move_y = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_platform(lista_plataformas) and self.rect_ground_collision.y < 700):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False


    def is_on_platform(self,plataform_list):
        retorno = False
        
        if(self.rect_ground_collision.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.rect_ground_collision.colliderect(plataforma.rect_ground_collision)):
                    if plataforma.type_moves:
                        if plataforma.goes_up:
                            self.rect.y -= plataforma.velocity
                            self.rect_corrected.y -= plataforma.velocity
                            self.rect_ground_collision.y -= plataforma.velocity
                            retorno = True
                        if plataforma.goes_down:
                            self.rect.y += plataforma.velocity
                            self.rect_corrected.y += plataforma.velocity
                            self.rect_ground_collision.y += plataforma.velocity
                            retorno = True
                    retorno = True
                    break       
        return retorno    
    
    def hit_enemy(self, enemigo):
        if self.animation == self.hit_r or self.animation == self.hit_l:  # Verificar si el jugador está realizando un golpe
            if self.rect_corrected.colliderect(enemigo.rect):  # Verificar colisión entre el jugador y el enemigo
                return True
        return False
    
    def hurting_enemy(self, lista_enemigos):
        if self.hitting:
            for enemigo in lista_enemigos:
                    if self.hit_enemy(enemigo):
                        if enemigo.health > 0:
                            enemigo.hurt(self.attack_value)
                            if enemigo.health <= 0:
                                enemigo.is_alive = False
                                enemigo.animation = enemigo.dead_animation
                                enemigo.frame = 0
                                #lista_enemigos.remove(enemigo)
        if self.is_shooting:
            for bullet in self.bullets[:]:
                for enemigo in lista_enemigos:
                    if bullet.rect.colliderect(enemigo.rect) and enemigo.health > 0:
                        enemigo.health -= 30
                        self.bullets.remove(bullet)
                        break
                    if enemigo.health <= 0:
                        enemigo.is_alive = False
                        enemigo.animation = enemigo.dead_animation
                        enemigo.frame = 0
                        sonido_enemigo_muerte.play()

                        #lista_enemigos.remove(enemigo)

    # def check_bullet_enemy_collision(self, lista_enemigos):
    #     for bullet in self.bullets[:]:
    #         for enemigo in lista_enemigos:
    #             if bullet.rect.colliderect(enemigo.rect):
    #                 enemigo.health -= 1
    #                 self.bullets.remove(bullet)
    #                 break

    def hit(self, on_off):
        if (on_off == True and self.hitting == False):
            if (self.direction == DIRECTION_R):
                self.animation = self.hit_r
                #sonido_pegada.play()
            else:
                self.animation = self.hit_l
                #sonido_pegada.play()
            self.frame = 0
            self.hitting = True
        else:
            self.hitting = False
            self.animation = self.stay()


    def hurt(self,lista_enemigos):
        if self.is_alive:
            for enemigo in lista_enemigos:
                if self.rect_corrected.colliderect(enemigo.rect_collision) and not self.hitting and enemigo.is_alive:
                    if self.health > 0:
                        self.health -= 1
                        sonido_colision.play()
                        if self.direction == DIRECTION_R:
                            self.animation = self.hurt_r
                            self.frame = 0
                        if self.direction == DIRECTION_L:
                            self.animation = self.hurt_l
                            self.frame = 0
                    else:
                        self.is_alive = False
                        self.animation = self.final_hit
                        self.frame = 0
                if not enemigo.is_alive:
                    if self.rect_corrected.colliderect(enemigo.rect):
                        lista_enemigos.remove(enemigo)
                        recogiendo_frasco.play()
                        self.score += 100
        if self.is_alive == False:
            sonido_muerte.play()
            self.animation = self.dead
            self.can_move = False
            self.can_jump = False




#HOLA
    def shoot(self, on_off):
        if (on_off and not self.is_shooting):
            self.is_shooting = True
            bullet = Bullet(self.rect_corrected.centerx, self.rect_corrected.centery, self.direction)
            self.bullets.append(bullet)
            sonido_disparo.play()
        if not on_off:
            self.is_shooting = False

        self.update_bullets()

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.update()

    def get_prize(self,prize):
        if self.rect_corrected.colliderect(prize.rect):  # Verificar colisión entre el jugador y el prize
            return True
        return False
    
    def win(self,lista_prize,lista_enemigos):
        if lista_prize:
            for prize in lista_prize:
                if self.get_prize(prize):
                    lista_prize.remove(prize)
                    recogiendo_frasco.play()
                    self.score += 100
        if len(lista_prize) == 0 and len(lista_enemigos) == 0:
            self.win_prize = True


    def set_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_corrected.x += delta_x
        self.rect_ground_collision.x += delta_x
    
    def set_y (self, delta_y):
        self.rect.y += delta_y 
        self.rect_corrected.y += delta_y        
        self.rect_ground_collision.y += delta_y

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.rate_frames_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0



    def update(self,delta_ms, lista_plataformas,lista_enemigos,lista_prize):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
        self.hurt(lista_enemigos)
        if self.is_shooting:
            self.shoot(True)
        
        self.update_bullets()
        self.hurting_enemy(lista_enemigos)
        self.win(lista_prize,lista_enemigos)
        
    
    def draw_bullets(self, screen):
        if self.is_shooting:
            for bullet in self.bullets:
                bullet.draw(screen)
        
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect_corrected)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collision)
        #print(self.rect_ground_collision)
        #print(self.health)
        print(self.score)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        self.draw_bullets(screen)