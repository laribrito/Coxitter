from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from kivy.uix.boxlayout import BoxLayout
from telaperfil import Titulo

# Carrega a interface
Builder.load_file('telas/feed.kv')

class Feed(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        menu = Menu.criar(1)
        self.add_widget(menu)
        layout = BoxLayout(size_hint_y=0.1, pos_hint={"top": 1})
        titulo = Titulo(text="Feed")
        layout.add_widget(titulo)
        self.add_widget(layout)