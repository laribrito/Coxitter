from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from titulo import Titulo
from kivy.uix.boxlayout import BoxLayout

# Carrega a interface
Builder.load_file('telas/pesquisar.kv')

class Pesquisar(Screen):
    menu = Menu(3)
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        self.add_widget(self.menu)
        Titulo(self, "Pesquisar")