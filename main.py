import pygame
import sys
from constantes import *
from player import Player
from plataforma import Plataform

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("C:\\Users\\Denise\\Downloads\\CLASE_19_inicio_juego\\CLASE_19_inicio_juego\\Assets\\background1.jpeg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=GROUND_LEVEL, speed_walk=30, speed_run=8, gravity=30, jump_power=70,jump_height=200, frame_rate_ms=80,move_rate_ms=100)

lista_plataformas = []
lista_plataformas.append(Plataform(400,300,80,80,1))
lista_plataformas.append(Plataform(480,300,80,80,1))

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            '''
            if event.key == pygame.K_LEFT:
                player_1.walk(DIRECTION_L)
            if event.key == pygame.K_RIGHT:
                player_1.walk(DIRECTION_R)
            '''
            if event.key == pygame.K_SPACE:
                player_1.jump(True)
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_1.jump(False)
                #pass
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_L)
    if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_R)
    if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]) or\
        (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] ):
            player_1.stay()
    
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    for plataforma in lista_plataformas:
        plataforma.draw(screen)

    player_1.update(delta_ms,lista_plataformas)
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    



    






