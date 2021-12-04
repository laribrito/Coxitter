from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class LayoutTitulo(BoxLayout):
    def __init__(self, titulo, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint={"top": 1}
        self.size_hint_y=0.1
        # QUANDO FOR PINTAR ALGO TEM QUE IR ATUALIZANDO A POSIÇÃO E TAMANHO DO WIDGET 
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        with self.canvas.before:
            Color(.80, .91, 1, 1) if titulo=="Feed" else Color(1,1,1,1)
            #ARMAZENANDO A FORMA EM UMA VARIÁVEL
            self.rect=Rectangle(pos=self.pos, size=self.size)
    
    def update_rect(instance, value, *args):
        #E ATUALIZANDO ELA ATRAVÉS DE UMA FUNÇÃO
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    

class LabelTitulo(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Atributos que não serão alterados ficam no __init__
        self.halign="right"
        self.valign="center"
        self.size_hint_y=1

    #QUANDO TRABALHAR COM O TAMANHO TEM QUE USAR O DEF ON_SIZE()
    def on_size(self, *args):
        #tamanho
        self.text_size=self.size

class Titulo():
    def __init__(self, tela, texto):
        self.tela=tela
        self.texto=texto

        layout = LayoutTitulo(self.texto)
        titulo = LabelTitulo(text=f"{self.texto}")
        layout.add_widget(titulo)
        self.tela.add_widget(layout)