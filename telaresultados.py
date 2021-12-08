from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from titulo import Titulo
from kivy.uix.boxlayout import BoxLayout


 #Carrega a interface
Builder.load_file('telas/resultados.kv')

class Resultados(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        menu = Menu.criar(3)
        self.add_widget(menu)
        Titulo(self, "Resultados")