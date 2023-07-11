import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from form_inicio_juego import InicioJuego
from gui_form_pausa import PauseMenu
from gui_form_lose import LoseMenu
from gui_form_win import WinMenu

class NextLevel(Form):
    def __init__(self, master_surface,save_file, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False, name="levels", num_level=1,level_2=False,level_3=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.level_active = "level_{0}".format(num_level)
        self.save_file = save_file
        self.num_level = num_level
        self.active = active
        self.title = Widget(master_form=self, x=300, y=100, w=800, h=120, text="Selecciona un nivel para continuar", font_size=50, font_color=C_WHITE, image_background=PATH_IMAGE+"\gui\Button1.png")
        self.level_button_1 = Button(master=self, x=150, y=300, w=250, h=150, on_click=self.update_level,on_click_param=1, image_background=PATH_IMAGE+"botones_forms\\bob.png")
        self.text_nivel_1 = Widget(master_form=self, x=220, y=470, w=80, h=50, text="Nivel 1", font_size=20, font_color=C_WHITE, image_background=PATH_IMAGE+"\gui\Button1.png")
        self.level_button_2 = Button(master=self, x=550, y=300, w=250, h=150, on_click=self.update_level,on_click_param=2, image_background=PATH_IMAGE+"botones_forms\\patricio.png",active=level_2)
        self.text_nivel_2 = Widget(master_form=self, x=620, y=470, w=80, h=50, text="Nivel 2", font_size=20, font_color=C_WHITE, image_background=PATH_IMAGE+"\gui\Button1.png")
        self.level_button_3 = Button(master=self, x=1000, y=300, w=250, h=150, on_click=self.update_level,on_click_param=3, image_background=PATH_IMAGE+"botones_forms\\arenita.png",active=level_3)
        self.text_nivel_3 = Widget(master_form=self, x=1100, y=470, w=80, h=50, text="Nivel 3", font_size=20, font_color=C_WHITE, image_background=PATH_IMAGE+"\gui\Button1.png")
        self.menu_button = Button(master=self, x=460, y=600, w=500, h=100, on_click=self.menu_principal, text="Menu Principal", font_size=70)
        self.lista_widget = [self.title,self.level_button_1,self.text_nivel_1,self.level_button_2,self.text_nivel_2,self.level_button_3,self.text_nivel_3,self.menu_button]


    def update_level(self, n_level):
        self.forms_dict.pop("start")
        self.play_level(n_level)


    def play_level(self,n_level=1):
        InicioJuego(name=self.level_active, master_surface=self.master_surface, level_juego=n_level,save_file = self.save_file)
        PauseMenu(name="pause", master_surface=pygame.display.get_surface(), x=ANCHO_VENTANA//4, y=ALTO_VENTANA//4, w=ANCHO_VENTANA//2, h=ALTO_VENTANA//2, color_border=C_BLACK, num_level=n_level,save_file = self.save_file)
        LoseMenu(name="lost", master_surface=pygame.display.get_surface(), x=ANCHO_VENTANA//4, y=ALTO_VENTANA//4, w=ANCHO_VENTANA//2, h=ALTO_VENTANA//2, color_border=C_BLACK, num_level=n_level,save_file = self.save_file)
        WinMenu(name="win", master_surface=pygame.display.get_surface(), x=ANCHO_VENTANA//4, y=ALTO_VENTANA//4, w=ANCHO_VENTANA//2, h=ALTO_VENTANA//2, color_border=C_BLACK, num_level=n_level,save_file = self.save_file)
        self.on_click_boton(self.level_active)


    def menu_principal(self, parametro):
        self.on_click_boton("main")
