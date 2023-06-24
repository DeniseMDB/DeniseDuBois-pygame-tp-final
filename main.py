import pygame
import sys
from constantes import *
from player import Player
from plataforma import Plataform
from enemigo import Enemigo

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\background1.jpeg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

casa_bob = pygame.image.load(PATH_IMAGE+"SpongeBob_House_1.png")
casa_bob = pygame.transform.scale(casa_bob,(100,170))

player_1 = Player(x=0,y=GROUND_LEVEL+50, speed_walk=30, speed_run=8, gravity=50, jump_power=70,jump_height=200, frame_rate_ms=60,move_rate_ms=80)
# enemigo_1 = Enemigo(x=500, y=120, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400)
# enemigo_2 = Enemigo(x=500, y=400, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400)

sand_floor = Plataform(0,GROUND_LEVEL+250,ANCHO_VENTANA,60,"sandfloor.png")

lista_enemigos = []
lista_enemigos.append(Enemigo(x=500, y=120, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400))
lista_enemigos.append(Enemigo(x=500, y=400, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400))

lista_plataformas = []
lista_plataformas.append(Plataform(0,400,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(400,200,300,50,"wood_box.png"))
lista_plataformas.append(Plataform(900,100,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(250,300,80,50,"wood_box.png",1,1,200, 400))
lista_plataformas.append(sand_floor)
pygame.time.set_timer(pygame.USEREVENT, 2000)
#HOLA
def remove_enemy(enemy):
    lista_enemigos.remove(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump(True)
            if event.key == pygame.K_e:
                player_1.shoot(True)
            if event.key == pygame.K_f:
                player_1.hit(True)
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_1.jump(False)
            if event.key == pygame.K_e:
                player_1.shoot(False)
            if event.key == pygame.K_f:
                player_1.hit(False)
        if event.type == pygame.USEREVENT:
            if 'enemy' in event.__dict__:
                remove_enemy(event.enemy)
        
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_L)
    if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_R)
    if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_f]) or\
        (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_f]):
            player_1.stay()

    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    screen.blit(casa_bob, (900,390))
    for plataforma in lista_plataformas:
        plataforma.update()
        plataforma.draw(screen)
    for enemigo in lista_enemigos:
        enemigo.update(delta_ms)
        enemigo.draw(screen)
        

    # enemigo_2.update(delta_ms)
    # enemigo_2.draw(screen)
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)
    
    pygame.display.flip()






