import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from form_inicio_juego import InicioJuego


class LoseMenu(Form):
    def __init__(self, name, master_surface,save_file, x, y, w, h, color_background=None, imagen_background=PATH_IMAGE+"forms\\lose.png", color_border=None, active=False,num_level=1):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.save_file = save_file
        self.num_level = num_level
        self.replay_button = Button(master=self, x=20, y=320, w=150, h=50, on_click=self.replay, text="Reiniciar",font_size=25,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.main_menu_button = Button(master=self, x=180, y=320, w=190, h=50, on_click=self.menu_principal, text="Menu Principal",font_size=20,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.settings_button = Button(master=self, x=400, y=320, w=150, h=50, on_click=self.settings, text="Settings",font_size=25,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.back_to_game= Button(master=self, x=560, y=320, w=150, h=50,on_click=self.on_click_boton, on_click_param="level_{0}".format(self.num_level),text="Reanudar",font_size=25,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.texto_title = Widget(master_form=self, x = 100, y = 30, w = 500, h = 80, text="Has Fallado",font_size=50,font_color=C_WHITE)
        self.lista_widget = [self.replay_button, self.main_menu_button, self.settings_button,self.back_to_game,self.texto_title ]
        self.level_2 = False
        self.level_3 = False
        if self.num_level == 2:
            self.level_2 =True
        if self.num_level == 3:
            self.level_2 =True
            self.level_3 =True

    def replay(self, parametro):
        self.forms_dict.pop("level_{0}".format(self.num_level))
        InicioJuego(name="level_{0}".format(self.num_level), master_surface=self.master_surface, level_juego=self.num_level)
        self.on_click_boton("level_{0}".format(self.num_level))


    def menu_principal(self, parametro):
        self.eliminar_formularios(["level_{0}".format(self.num_level),"pause"])
        #self.activar_musica("music_main")
        self.on_click_boton("main")

    def settings(self, parametro):
        # Lógica para abrir el menú de configuración
        pass

