from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from kivy.uix.boxlayout import BoxLayout
from titulo import Titulo
from kivy.properties import ObjectProperty
from postagem import Postagem

# Carrega a interface
Builder.load_file('telas/feed.kv')

class Fundo(Screen):
    caixinha = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.adicionar()
        # Adiciona o menu a tela
        menu = Menu.criar(1)
        self.add_widget(menu)
        Titulo(self, "Meu Feed")
    def adicionar(self):
        jaca = Postagem()
        self.caixinha.add_widget(jaca)