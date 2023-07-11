import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Button(Widget):
    def __init__(self,master,x,y,w,h,color_background=None,color_border=None,image_background=None,text=None,font_size=20,font_color=COLOR_TEXTO_MENU,on_click=None,on_click_param=None, active = True):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.active = active
        if not self.active:
            self.asignar_imagen_background(PATH_IMAGE + r"\gui\locked.png")
        
    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 


    def update(self,lista_eventos):
        self.render()
        if self.active:
            mousePos = pygame.mouse.get_pos()
            self.state = M_STATE_NORMAL
            if self.slave_rect_collide.collidepoint(mousePos):
                if(pygame.mouse.get_pressed()[0]):
                    self.state = M_STATE_CLICK
                else:
                    self.state = M_STATE_HOVER
                
            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if(self.slave_rect_collide.collidepoint(evento.pos)):
                        self.on_click(self.on_click_param)
