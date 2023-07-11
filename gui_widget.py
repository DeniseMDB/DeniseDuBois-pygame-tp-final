import pygame
from pygame.locals import *
from constantes import *

class Widget:
    def __init__(self,master_form,x,y,w,h,color_background = None,color_border = None,image_background=None,text=None,font_size=None,font_color=COLOR_TEXTO_MENU, center = True):
        self.center = center
        self.master_form = master_form 
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        
        self.image_background = image_background
        if self.image_background != None:
            self.asignar_imagen_background(self.image_background)


        self.text = text
        if(self.text != None):
            self.text = text
            self.font_color = font_color
            try:
                self.font_sys = pygame.font.Font(PATH_IMAGE + r"Krabby_Patty.ttf", font_size)
            except:
                self.text = None
                print("Error en archivo font de texto")
            
            
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect(x = self.x, y = self.y)
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y


    def asignar_imagen_background(self, image_background):
        try:
            self.image_background = pygame.image.load(image_background).convert_alpha()
            self.image_background = pygame.transform.scale(self.image_background,(self.w, self.h)).convert_alpha()
        except:
            self.image_background = None
            print("Error al cargar la imagen {0}".format(image_background))

    def render(self):
        
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect(x = self.x, y = self.y)
        

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))
        
        if self.text != None:
            self.image_text = self.font_sys.render(self.text,True,self.font_color,self.color_background)
            if self.center:
                self.image_text_rect = self.image_text.get_rect(center = (self.slave_rect.width/2, self.slave_rect.height/2)) 
            else:
                self.image_text_rect = self.image_text.get_rect(x = 0, centery = self.slave_rect.height/2) 
            self.slave_surface.blit(self.image_text, self.image_text_rect)
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)




    def update(self, lista_eventos):
        self.render()


    def draw(self):
        # pygame.draw.rect(self.master_form.surface, C_BLACK, self.slave_rect)
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)