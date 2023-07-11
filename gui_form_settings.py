import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_healthbar import ElementBar
import pygame.mixer

pygame.mixer.init()
sonido_click = pygame.mixer.Sound(PATH_IMAGE+r"sounds\click.mp3")

class Settings(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        self.save_file = ""
        self.title = Widget(master_form=self, x = 250, y = 200, w = 1000, h = 150, text="Musica",font_size=80)

        self.back_menu = Button(master=self, x =460, y = 520, w = 500, h = 100, on_click=self.menu_pausa,text="Atras", font_size= 70)
        self.plus_sound = Button(master=self,x=1010,y=400,w=50,h=50,image_background=PATH_IMAGE + r"\gui\plus.png",on_click=self.change_music,on_click_param=1)
        self.minus_sound = Button(master=self,x=440,y=400,w=50,h=50,image_background=PATH_IMAGE + r"\gui\minus.png",on_click=self.change_music,on_click_param=-1)
        self.sound_bar = ElementBar(master=self,x=500,y=390,w=500,h=70, value=(pygame.mixer.music.get_volume()*20) ,value_max = 10, image_background=PATH_IMAGE + r"\gui\BarraGris.png",element= PATH_IMAGE + r"\gui\Button3.png")
        self.lista_widget = [self.back_menu ,self.title,self.plus_sound,self.minus_sound,self.sound_bar]

    
    def change_music(self, incremento):
        '''
        Cambia el valor de la barra de musica y setea el volumen de la musica pygame.mixer
        Se divide por 20 para que el valor maximo sea 0.5
        '''
        self.sound_bar.value += incremento
        volumen = self.sound_bar.value / 10.0
        pygame.mixer.music.set_volume(volumen)
        sonido_click.play()


    def menu_pausa(self, parametro):
        self.forms_dict.pop("settings")
        self.on_click_boton("pause")