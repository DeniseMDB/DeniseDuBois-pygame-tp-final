import pygame
import json
from data_sqlite import get_data_level
from gui_form import Form
from constantes import *
from gui_widget import Widget
from gui_healthbar import HealthBar
from player import Player
from enemigo import Enemigo
from plataforma import Plataform
from botin import Prize
from pez import Pez
import sys
import pygame.mixer

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound(PATH_IMAGE+r"sounds\background_music_2.mp3")




class InicioJuego(Form):
    def __init__(self,name,master_surface,save_file,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False,level_juego=1):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        
        self.level = "level_{0}".format(level_juego)
        self.num_level = level_juego
        self.lista_enemigos = []
        self.lista_plataformas = []
        self.lista_prize = []
        self.time = 80
        self.timer_surface = 0
        self.timer_widget = 0
        self.flag_pausa = False
        if self.active:
            sonido_fondo.play()
        else:
            sonido_fondo.stop()

        # Cargar el archivo JSON del nivel
        with open("data_level.json") as file:
            data = json.load(file)

        # Crear el objeto Player
        player_data = data[self.level][0]["player"]

        # Obtener los parámetros de animación del jugador del JSON
        walk_animation = player_data["walk"]
        idle_animation = player_data["idle"]
        jump_animation = player_data["jump"]
        hit_animation = player_data["hit"]
        hurt_animation = player_data["hurt"]
        dead_animation = player_data["dead"]

        # Crear el objeto Player con los parámetros de animación
        self.player = Player(
            x=player_data["x"],
            y=700 - 250,
            speed_walk=30,
            speed_run=8,
            gravity=40,
            jump_power=50,
            jump_height=100,
            health=1000,
            attack=1.2,
            frame_rate_ms=60,
            move_rate_ms=80,
            path_sprite=player_data["path_sprite"],
            walk=walk_animation,
            idle=idle_animation,
            jump=jump_animation,
            hit=hit_animation,
            hurt=hurt_animation,
            dead=dead_animation
        )
        self.cargar_score(save_file, level_juego)
        self.text_score = Widget(master_form=self, x = 250, y = 20, w = 400, h = 30, text="Puntaje",font_size=20,font_color=C_BLACK_2)
        self.text_time = Widget(master_form=self, x = 550, y = 20, w = 400, h = 30, text="Tiempo",font_size=20,font_color=C_BLACK_2)
        self.score = Widget(master_form=self, x=400, y = 50, w=100, h=30,image_background=PATH_IMAGE + r"\gui\Button1.png", text=" ",font_size=30, font_color=C_BLACK)
        self.health_bar = HealthBar(master_form=self,x=30,y=50,w=350,h=20,color_background=M_BRIGHT_HOVER,color_border=C_WHITE, value =self.player.health, value_max = self.player.health)
        self.time_widget = Widget(master_form=self, x=700, y = 50, w=100, h=30,image_background=PATH_IMAGE + r"\gui\time.png", text="{0}".format(self.time),font_size=30, font_color=C_BLACK)
        self.lista_widget = [self.text_score,self.text_time,self.score,self.health_bar,self.time_widget]
        #Imagen de fondo segun nivel
        imagen_fondo = data[self.level][0]["background"]
        self.image_background = pygame.image.load(PATH_IMAGE+imagen_fondo)
        self.image_background = pygame.transform.scale(self.image_background,(ANCHO_VENTANA,ALTO_VENTANA))
        self.suelo = pygame.image.load(PATH_IMAGE+data[self.level][0]["suelo"])
        self.suelo = pygame.transform.scale(self.suelo,(500,100))
        # Crear la lista de enemigos
        enemigos_data = data[self.level][0]["enemigos"]
        for enemigo_data in enemigos_data:
            enemigo = Enemigo(x=enemigo_data["x"], y=enemigo_data["y"], health=250, total_health=100, speed_movement=5, frame_rate_ms=100, move_rate_ms=120, limite_right=enemigo_data["limite_right"], limite_left=enemigo_data["limite_left"])
            self.lista_enemigos.append(enemigo)

        # Cargar los enemigos del tipo Pez si existen
        if "enemy_fish" in data[self.level][0]:
            enemigos_pez_data = data[self.level][0]["enemy_fish"]
            for enemigo_pez_data in enemigos_pez_data:
                enemigo_pez = Pez(x=enemigo_pez_data["x"], y=enemigo_pez_data["y"], health=300, total_health=150, speed_movement=9, frame_rate_ms=60, move_rate_ms=50, limite_right=enemigo_pez_data["limite_right"], limite_left=enemigo_pez_data["limite_left"])
                self.lista_enemigos.append(enemigo_pez)

        # Crear la lista de plataformas
        sand_floor = Plataform(0,GROUND_LEVEL,ANCHO_VENTANA,120,"sandfloor.png")
        plataformas_data = data[self.level][0]["plataformas"]
        for plataforma_data in plataformas_data:
            plataforma = Plataform(plataforma_data["x"], plataforma_data["y"], plataforma_data["w"], plataforma_data["h"], "wood_box.png")
            self.lista_plataformas.append(plataforma)
        self.lista_plataformas.append(Plataform(0,0,20,ALTO_VENTANA,"wood_box_flipped.png"))
        self.lista_plataformas.append(Plataform(1480,0,20,ALTO_VENTANA,"wood_box_flipped.png"))
        self.lista_plataformas.append(sand_floor)

        # Crear la lista de premios
        prize_data = data[self.level][0]["prize"]
        for prize in prize_data:
            premio = Prize(prize["x"], prize["y"], 60, 60, len(self.lista_prize), "antidote.png")
            self.lista_prize.append(premio)
    
    def cargar_score(self, save_file, nivel):
        datos = get_data_level(save_file, nivel)
        self.player.score = datos[0]

    def update_widgets(self):
        '''
        Actualiza la informacion que muestran los widget
        '''
        self.health_bar.value = self.player.health
        self.score.text = f"{self.player.score}"
        self.time_widget.text = f"{self.time}"

    def pause_game(self,lista_eventos,delta_ms,segundo,keys,on_off=False):
        if on_off:
            if not self.flag_pausa:
                self.on_click_boton("pause")


    def update(self, lista_eventos, delta_ms,segundo,keys):
        super().update(lista_eventos,delta_ms,segundo,keys)
        self.update_widgets()
        for widget in self.lista_widget:
            widget.update(lista_eventos)
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump(True)
                if event.key == pygame.K_e:
                    self.player.shoot(True)
                if event.key == pygame.K_f:
                    self.player.hit(True)
                if event.key == pygame.K_ESCAPE:
                    self.pause_game(lista_eventos, delta_ms,segundo,keys,on_off=True)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jump(False)
                if event.key == pygame.K_e:
                    self.player.shoot(False)
                if event.key == pygame.K_f:
                    self.player.hit(False)
            if event.type == segundo:
                self.time += -1

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.player.walk(DIRECTION_L)
        if not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.player.walk(DIRECTION_R)
        if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[
            pygame.K_f]) or \
                (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_f]):
            self.player.stay()
        
        
        if not self.player.is_alive or self.time < 0:
            self.set_active("lost")
        elif self.player.win_prize:
            self.forms_dict["win"].register_score(self.player.score, self.time)
            self.set_active("win")

    def draw(self, lista_eventos, delta_ms, keys):
        super().draw(lista_eventos,delta_ms,keys)
        self.timer_surface += delta_ms
        screen = self.master_surface
        screen.blit(self.image_background, self.image_background.get_rect())
        if self.timer_surface > 5:
            self.timer_surface = 0
            screen.blit(self.surface, self.slave_rect)
            self.render()

        self.timer_widget += delta_ms
        if self.timer_widget > 30:
            self.timer_widget = 0
            for aux_boton in self.lista_widget:
                aux_boton.draw()
        for plataforma in self.lista_plataformas:
            plataforma.update()
            plataforma.draw(screen)
        for prize in self.lista_prize:
            prize.draw(screen)
        for enemigo in self.lista_enemigos:
            enemigo.update(delta_ms,self.player)
            enemigo.draw(screen)
        for widget in self.lista_widget:
            widget.draw()
        screen.blit(self.suelo,(0,710))
        screen.blit(self.suelo,(500,710))
        screen.blit(self.suelo,(1000,710))
        self.player.update(delta_ms,self.lista_plataformas,self.lista_enemigos,self.lista_prize)
        self.player.draw(screen)

        pygame.display.flip()

        
