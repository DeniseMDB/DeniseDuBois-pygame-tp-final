import pygame
import re
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_textbox import TextBox
from gui_form_levels import NextLevel
from data_sqlite import create_start

class StartMenu(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        self.save_file = ""
        self.title = Widget(master_form=self, x = 250, y = 200, w = 1000, h = 150, text="Ingresa tu nombre:",font_size=80)
        self.input = TextBox(master=self,x=500,y=380,w=400,h=100,color_background=None,color_border=None,image_background="Assets//gui//Button_XL_09.png",text="Text",font_size=50,font_color=C_WHITE) #ingresa el nombre
        self.continue_button = Button(master=self, x =460, y = 520, w = 500, h = 100, on_click=self.continuar,text="Continuar", font_size= 70)
        self.lista_widget = [self.title,self.input,self.continue_button]
    
    def continuar(self,parametro):
        self.save_name(None)
        NextLevel(master_surface=self.master_surface,name="levels",num_level=1,imagen_background=PATH_IMAGE+"fondo_start.png",level_2=True,level_3=True,save_file=self.save_file)
        self.on_click_boton("levels")


    def save_name(self, parametro):
        if re.search("^ | $", self.input.text):
            self.input.text = self.input.text.strip()
        self.save_file = self.input.text

        create_start(self.save_file, self.input.text, ULTIMO_NIVEL)
