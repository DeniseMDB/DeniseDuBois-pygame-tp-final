import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from form_inicio_juego import InicioJuego
from data_sqlite import *
from gui_form_score import FormScore


class WinMenu(Form):
    def __init__(self, name, master_surface,save_file, x, y, w, h, color_background=None, imagen_background=PATH_IMAGE+"forms\\win.png", color_border=None, active=False,num_level=1):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.level_name = "level_{0}".format(num_level)
        self.num_level = num_level
        self.next_button = Button(master=self, x=480, y=150, w=190, h=45, on_click=self.next, text="Siguiente Nivel",font_size=18,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.main_menu_button = Button(master=self, x=480, y=240, w=190, h=45, on_click=self.menu_principal, text="Menu Principal",font_size=18,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.texto_title = Widget(master_form=self, x = 100, y = 30, w = 500, h = 80, text="Muy bien!",font_size=50,font_color=C_WHITE)
        self.lista_widget = [self.next_button, self.main_menu_button,self.texto_title ]
        self.save_file = save_file
        self.score_total = 0
        self.score_time = 10


    def next(self, parametro):
        if self.num_level < ULTIMO_NIVEL:
            self.eliminar_formularios([self.level_name, "pause", "win", "lose"])
            self.forms_dict["levels"].play_level(n_level=self.num_level + 1)
        else:
            FormScore(name="scores", master_surface=self.master_surface, imagen_background=PATH_IMAGE+"fondo_start.png")
            self.eliminar_formularios(["win","pause"])
            self.on_click_boton("scores")

    def menu_principal(self, parametro):
        self.eliminar_formularios(["level_{0}".format(self.num_level),"pause","win", "lose"])
        #self.activar_musica("music_main")
        self.on_click_boton("main")

    def settings(self, parametro):
        # Lógica para abrir el menú de configuración
        pass


    def register_score(self, score_player, time):
        self.score_total = score_player + time*(self.score_time*self.num_level)
        cronometro = get_time_level(self.save_file, self.num_level)
        if self.num_level < ULTIMO_NIVEL:
            save_game(self.save_file, self.num_level + 1, self.score_total, (cronometro + 60 - time))
        else:
            save_score(get_name_save(self.save_file), self.score_total, (cronometro + 60 - time))
            