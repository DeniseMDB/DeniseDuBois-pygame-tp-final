import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

class Controls(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        self.title = Widget(master_form=self, x = 400, y = 80, w = 600, h = 150, text="Controles",font_size=60)
        self.caminar = Widget(master_form=self, x =100, y = 280, w = 180, h = 50, text="Caminar",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.tecla_mover = Widget(master_form=self, x =550, y = 280, w = 180, h = 50, text="Teclas < y >",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button1.png")
        self.pegar = Widget(master_form=self, x = 750, y = 540, w = 180, h = 50, text="Pegar",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.tecla_pegar = Widget(master_form=self, x =1200, y = 540, w = 180, h = 50, text="F",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button1.png")
        self.saltar = Widget(master_form=self, x = 90, y = 540, w = 180, h = 50, text="Saltar",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.tecla_saltar = Widget(master_form=self, x =550, y = 540, w = 180, h = 50, text="Espacio",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button1.png")
        self.disparar = Widget(master_form=self, x = 750, y = 280, w = 180, h = 50, text="Disparar",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.tecla_shoot = Widget(master_form=self, x =1200, y = 280, w = 180, h = 50, text="E",font_size=30,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button1.png")
        self.continue_button = Button(master=self, x =600, y = 700, w = 180, h = 50, on_click=self.back,text="Atras", font_size= 40,font_color=C_WHITE,image_background=PATH_IMAGE+"//gui//Button2.png")
        self.lista_widget = [self.title,self.caminar,self.pegar,self.saltar,self.disparar,self.continue_button,self.tecla_mover,self.tecla_pegar,self.tecla_saltar,self.tecla_shoot]
    
    def back(self,parametro):
        self.forms_dict.pop("controls")
        self.on_click_boton("main")

