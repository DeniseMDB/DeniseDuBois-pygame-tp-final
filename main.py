import pygame
import pygame.mixer
import sys
from constantes import *
from player import Player
from plataforma import Plataform
from enemigo import Enemigo
from botin import Prize

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
pygame.mixer.init()

#cancion_fondo = pygame.mixer.music.load(PATH_IMAGE+"soundtrack_menu.mp3")
sonido_pegada = pygame.mixer.Sound(PATH_IMAGE+"bob_esponja_golpe.mp3")
#sonido_walking = pygame.mixer.Sound(PATH_IMAGE+"walking_long.mp3")
#sonido_walking.set_volume(0.5)
#pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE+"background1.jpeg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

casa_bob = pygame.image.load(PATH_IMAGE+"SpongeBob_House_1.png")
casa_bob = pygame.transform.scale(casa_bob,(100,170))

player_1 = Player(x=0,y=700-250, speed_walk=30, speed_run=8, gravity=40, jump_power=50,jump_height=100,health=1000,attack=1.2, frame_rate_ms=60,move_rate_ms=80)
# enemigo_1 = Enemigo(x=500, y=120, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400)
# enemigo_2 = Enemigo(x=500, y=400, health=100, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400)

sand_floor = Plataform(0,GROUND_LEVEL,ANCHO_VENTANA,120,"sandfloor.png")

lista_enemigos = []
lista_enemigos.append(Enemigo(x=500, y=120, health=250, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400))
lista_enemigos.append(Enemigo(x=500, y=400, health=250, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=600,limite_left=400))
lista_enemigos.append(Enemigo(x=1100, y=250, health=250, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=1200,limite_left=900))
lista_enemigos.append(Enemigo(x=1280, y=120, health=250, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120,limite_right=1350,limite_left=1200))


lista_plataformas = []
#plataformas contornos
lista_plataformas.append(Plataform(0,0,20,ALTO_VENTANA,"wood_box_flipped.png"))
#lista_plataformas.append(Plataform(0,0,ANCHO_VENTANA,20,"wood_box.png"))
lista_plataformas.append(Plataform(1480,0,20,ALTO_VENTANA,"wood_box_flipped.png"))
#plataformas quietas
lista_plataformas.append(Plataform(0,400,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(0,180,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(400,200,300,50,"wood_box.png"))
lista_plataformas.append(Plataform(900,100,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(900,500,320,50,"wood_box.png"))
lista_plataformas.append(Plataform(900,350,320,50,"wood_box.png"))
lista_plataformas.append(Plataform(400,500,320,50,"wood_box.png"))
lista_plataformas.append(Plataform(200,600,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(750,600,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(1300,375,160,50,"wood_box.png"))
lista_plataformas.append(Plataform(1280,210,300,50,"wood_box.png"))
lista_plataformas.append(Plataform(1120,180,80,50,"wood_box.png"))
#plataformas moviles
lista_plataformas.append(Plataform(x=250,y=300,w=100,h=50,path="wood_box.png",type_move=True,type_h_v=1,limit_top=200,limit_bottom=400))
lista_plataformas.append(Plataform(750,310,100,50,"wood_box.png",True,1,100, 400))
lista_plataformas.append(sand_floor)
pygame.time.set_timer(pygame.USEREVENT, 2000)

lista_prize = []
lista_prize.append(Prize(70,340,60,60,len(lista_prize),"antidote.png"))#lista
lista_prize.append(Prize(1377,315,60,60,len(lista_prize),"antidote.png")) #lista
lista_prize.append(Prize(1379,690,60,60,len(lista_prize),"antidote.png"))#lista
lista_prize.append(Prize(970,42,60,60,len(lista_prize),"antidote.png"))
lista_prize.append(Prize(55,120,60,60,len(lista_prize),"antidote.png"))#lista
lista_prize.append(Prize(55,630,60,60,len(lista_prize),"antidote.png"))#lista




while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump(True)
            if event.key == pygame.K_e:
                player_1.shoot(True)
            if event.key == pygame.K_f:
                sonido_pegada.play()
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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtener las coordenadas del clic
            x, y = pygame.mouse.get_pos()
            print("Coordenadas del clic: ({}, {})".format(x, y))
        
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_L)
        #sonido_walking.play()
    if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
        player_1.walk(DIRECTION_R)
        #sonido_walking.play()
    if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_f]) or\
        (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_f]):
            player_1.stay()

    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    screen.blit(casa_bob, (1380,50))
    for plataforma in lista_plataformas:
        plataforma.update()
        plataforma.draw(screen)
    for enemigo in lista_enemigos:
        enemigo.update(delta_ms)
        enemigo.draw(screen)
    for prize in lista_prize:
        prize.draw(screen)
        

    # enemigo_2.update(delta_ms)
    # enemigo_2.draw(screen)
    player_1.update(delta_ms,lista_plataformas,lista_enemigos,lista_prize)
    player_1.draw(screen)
    
    pygame.display.flip()






