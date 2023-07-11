import pygame
from constantes import *
import pygame.mixer

pygame.mixer.init()
sonido_click = pygame.mixer.Sound(PATH_IMAGE+r"sounds\click.mp3")
musica_fondo = pygame.mixer.Sound(PATH_IMAGE+r"sounds\background_music.mp3")

class Form():
    '''
    Clase padre de todos los menus del juego; cada formulario creado es agregado a 'forms_dict'
    '''
    forms_dict = {}
    sounds_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        '''
        Atributos: dimensiones, ubicacion dentro de la pantalla, elementos de fondo,
        superficie y su rectangulo,lista de widgets cuya funcion es permitir la 
        interaccion con el usuario
        '''
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect(x = x, y = y)
        self.active = active
        
        if imagen_background != None:
            try:
                self.image_background  = pygame.image.load(imagen_background).convert_alpha()
                self.image_background  = pygame.transform.scale(self.image_background, (self.w, self.h)).convert_alpha()
            except:
                self.image_background = None
                print("Imagen background para el formulario no encontrada")
        else:
            self.image_background = None

        self.lista_widget = []


    def on_click_boton(self, parametro):
        '''
        Activa formulario y genera sonido de click
        '''
        sonido_click.play()
        self.set_active(parametro)


    def eliminar_formularios(self, lista_claves):
        '''
        Metodo para eliminar formularios de 'forms_dict' se usa cuando se quieran descartar
        varios formularios que ya no sean requeridos, en caso de error informa que la clave no existe
        '''
        for clave in lista_claves:
            try:
                self.forms_dict.pop(clave)
            except:
                print("La clave no existe")


    def set_active(self,name):
        '''
        Metodo que desactiva a todos los formularios de 'forms_dict', y luego activa al formulario pasado
        como parametro. Este metodo se utiliza cuando se quiere viajar entre formularios
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True


    def update_form(self, lista_eventos, delta_ms, segundo, keys):
        '''
        Metodo que actualiza y muestra en pantalla al primer formulario que se encuentre activo
        '''
        for form in self.forms_dict.values():
            if form.active:
                form.update(lista_eventos, delta_ms, segundo,keys)
                form.draw(lista_eventos, delta_ms, keys)
                break
    

    def activar_musica(self):
        '''
        Metodo para activar la musica del juego, 
        si el archivo pasado como parametro no existe informa el error
        '''
        try:
            musica_fondo.play()
            pygame.mixer.music.play(-1)
        except:
            print("ARCHIVO NO ENCONTRADO")

    def desactivar_sonido_actual(self):
        '''
        Metodo para detener el sonido actual
        '''
        musica_fondo.stop()

    

    def render(self):
        '''
        Coloca los elementos de fondo en la superficie del formulario, 
        en caso de no tenerlos, no hara nada
        '''
        if(self.color_background != None):
            self.surface.fill(self.color_background)

        if(self.image_background != None):
            self.surface.blit(self.image_background, (0,0))

        if self.color_border != None:
            pygame.draw.rect(self.surface, self.color_border, self.surface.get_rect(), 2)


    def update(self, lista_eventos, delta_ms, segundo,keys):
        '''
        Recorre la lista de widgets del formulario y los actualiza, recibe la lista de eventos
        para verificar el tiempo, mouse y teclado.
        '''
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)


    def draw(self, lista_eventos, delta_ms, keys):
        '''
        Blitea la superficie del formulario sobre la master_surface (la pantalla), luego
        en la superficie del form, coloca el fondo y los widgets
        '''
        self.master_surface.blit(self.surface,self.slave_rect)
        self.render()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
            