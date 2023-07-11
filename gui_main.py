import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_main import MainMenu
from data_sqlite import create_database_game
flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)
create_database_game()
menu_main = MainMenu(name = "main", master_surface=screen,imagen_background=PATH_IMAGE+"fondo_menu.png")
menu_main.activar_musica()

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    menu_main.update_form(lista_eventos, delta_ms, segundo, keys) 

    pygame.display.flip()