from constantes import *
from gui_form import *
from gui_button import Button
from gui_widget import Widget
from data_sqlite import *

class FormScore(Form):
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.jugador = Widget(master_form=self, x = 280, y = 50, w = 260, h = 90, text="Jugador", font_size= 75)
        self.score = Widget(master_form=self, x = 605, y = 50, w = 260, h = 90, text="Puntos", font_size= 75)
        self.tiempo = Widget(master_form=self, x = 930, y = 50, w = 260, h = 90, text="Tiempo", font_size= 75)
        self.back = Button(master=self,x=50, y=670, w=120,h =50,on_click=self.retroceder, text="Atras", font_size= 50)
        self.lista_widget = [self.score, self.jugador, self.tiempo, self.back]
        self.crear_tabla(get_scores())


    def crear_tabla(self, lista_tuplas):
        '''
        Recibe como parametro una lista de tuplas, se creara una fila de widgets
        por cada tupla, la cantidad de widgets en la fila depende de la cantidad
        de elementos de la tupla, cada fila y columna esta separada por parametros
        hardcodeados
        '''
        pos_y = 200
        nro = 1
        for tupla in lista_tuplas:
            pos_x = 310
            for dato in tupla:
                data = Widget(master_form=self, x = pos_x, y = pos_y, w=200, h= 60, text= "{0}".format(dato), font_size=30, font_color=C_BLACK, image_background= PATH_IMAGE + r"\gui\board.png")
                self.lista_widget.append(data)
                pos_x += 325
            pos_y += 100
            nro += 1

    
    def retroceder(self, parametro):
        '''
        Elimina al formulario 'score' de forms_dict y pone en activo al formulario 'options'
        '''
        self.forms_dict.pop("scores")
        self.on_click_boton("main")