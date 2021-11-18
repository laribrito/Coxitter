from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu

# Carrega a interface
Builder.load_file('telas/home.kv')

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        menu = Menu.criar(1)
        self.add_widget(menu)