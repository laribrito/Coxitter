from sys import hexversion
from typing import Text
from kivy.logger import BLACK
from kivy.uix.behaviors import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from main import App
from kivy.metrics import dp

#Classe para o botão com imagem
class Btn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size=(75,75)

class Menu():
    def criar():
        #Um boxlayout para abrigar todo o menu
        box = BoxLayout(
            padding = 0,
            spacing=0
        )

        #gridlayout para os botões
        Grid = GridLayout(
            cols = 3, 
            size_hint_y = None
        )
        btn1 = Button(
            text = "HOME",
            font_name="telas/fontes/NewsCycle.ttf"
        )
        Grid.add_widget(btn1)
        btn2 = Button(
            text = "PERFIL",
            font_name="telas/fontes/NewsCycle.ttf"
        )
        Grid.add_widget(btn2)
        btn3 = Button(
            text = "PESQUISAR",
            font_name="telas/fontes/NewsCycle.ttf"
        )
        Grid.add_widget(btn3)

        #botão "coxinhar"
        anchor = AnchorLayout(anchor_x="right", anchor_y="bottom", padding=10)
        coxinhar = Btn(
            background_normal="telas/imagens/coxinhar.png",
            border=(0,0,0,0),
            size_hint=(None,None)
        )
        anchor.add_widget(coxinhar)
        
        box.add_widget(anchor)
        box.add_widget(Grid)
        
        return box
