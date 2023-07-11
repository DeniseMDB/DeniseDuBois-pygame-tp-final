import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *
from random import choice

class TextBox(Widget):
    def __init__(self,master,x, y , w, h, color_background=None,color_border=None,image_background=None,text=None,font_size=15,font_color=COLOR_TEXTO_MENU):
        text = choice(["Jugador1","Jugador2", "Nombre", "Player"])
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font_size,font_color)
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        
    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 

    def update(self,lista_eventos):
        self.render()
        
        if self.slave_rect_collide.collidepoint(pygame.mouse.get_pos()):
            self.state = M_STATE_HOVER
            self.writing_flag = True
        else:
            self.state = M_STATE_NORMAL
            self.writing_flag = False
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:
                        self.text += evento.unicode
