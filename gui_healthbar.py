import pygame
from gui_widget import Widget
from constantes import *
from math import ceil

class HealthBar(Widget):
    def __init__(self,master_form,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None, value=0, value_max = 1):
        super().__init__(master_form,x,y,w,h,color_background,color_border,image_background,None,None,None)
        self.barra_vida = pygame.Rect(0,0,w,h)
        self.value_min = 0
        self.value = value
        self.value_max = value_max
        
    def render(self):
        super().render()
        self.barra_vida.w = self.value * self.w / self.value_max
        self.slave_surface.fill(C_GREEN_2, self.barra_vida)
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)
        

    def update(self, lista_eventos):
        self.render()


class ElementBar(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=None,color_border=None,image_background=None, value = 1,value_max = 3, element = None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,None,None,None)

        self.surface_element = pygame.image.load(element)
        self.surface_element = pygame.transform.scale(self.surface_element,(w/value_max, h)).convert_alpha()

        #print(value)
        self.value = ceil(value)
        self.value_max= value_max
        
    def render(self):
        super().render()
        if self.value < 0:
            self.value = 0
        elif self.value > self.value_max:
            self.value = self.value_max
            
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, 0))

        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self,lista_eventos):
        self.render()