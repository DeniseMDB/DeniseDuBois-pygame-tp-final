import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_form_start import StartMenu
from gui_form_score import FormScore
from gui_form_controles import Controls



class MainMenu(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=True):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        self.title = Widget(master_form=self, x = 100, y = 50, w = 1000, h = 150, text="Bob Esponja Game",font_size=80)
        self.start_button = Button(master=self, x = 300, y = 300, w = 500, h = 100, on_click=self.start, text="Iniciar Juego", font_size= 60)
        self.controls_button = Button(master=self, x = 300, y = 410, w = 470, h = 100, on_click=self.controls, text="Controles", font_size= 60)
        self.score_button = Button(master=self, x = 300, y = 520, w = 500, h = 100, on_click=self.ranking,text="Ranking Puntaje", font_size= 60)
        self.lista_widget = [self.title,self.start_button,self.controls_button,self.score_button]

    def start(self, parametro):
        StartMenu(name="start", master_surface=self.master_surface, imagen_background=PATH_IMAGE+"fondo_start.png")
        self.on_click_boton("start")

    def controls(self, parametro):
        Controls(name="controls", master_surface=self.master_surface, imagen_background=PATH_IMAGE+"forms\controles.png")
        self.on_click_boton("controls")
    
    def ranking(self, parametro):
        FormScore(name="scores", master_surface=self.master_surface, imagen_background=PATH_IMAGE+"fondo_start.png")
        self.on_click_boton("scores")

    # def update_form(self, lista_eventos, delta_ms, segundo, keys):
    #     for form in self.forms_dict.values():
    #         if form.active:
    #             form.update(lista_eventos, delta_ms, segundo, keys)  # Agregar el argumento 'keys' aquí
    #             form.draw(lista_eventos, delta_ms, keys)  # Pasar 'keys' como argumento también
    #             break

    # def draw(self,lista_eventos,delta_ms,segundo): 
    #     super().draw(lista_eventos,delta_ms,segundo)
    #     for aux_widget in self.lista_widget:    
    #         aux_widget.draw()