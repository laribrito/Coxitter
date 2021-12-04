from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from kivy.uix.boxlayout import BoxLayout
from titulo import Titulo

# Carrega a interface
Builder.load_file('telas/feed.kv')

class Feed(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        menu = Menu.criar(1)
        self.add_widget(menu)
        Titulo(self, "Feed")