from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu

# Carrega a interface
Builder.load_file('telas/pesquisar.kv')

class Pesquisar(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        menu = Menu.criar(3)
        self.add_widget(menu)