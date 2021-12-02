from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color
from appConfig import AppConfig

# Classe para o GridLayout dos botões
class BtnMenu(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color="#B4C5FF"
        self.background_normal=""
        self.background_down=""

# Classe para o botão com imagem
class Btn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size=(75,75)            

# Classe de Label sem configurações
class CaixaTexto(TextInput):
    def on_size(self, *args):
        self.height=self.line_height*6
        self.multiline=True

class Menu():
    def criar(num):
        # Um boxlayout para abrigar todo o menu
        box = BoxLayout(
            padding = 0,
            spacing=0
        )

        # Gridlayout para os botões
        Grid = GridLayout(
            cols = 3, 
            size_hint_y = None
        )

        # Botões
        btn1 = BtnMenu(
            text = "FEED"
        )
        btn1.bind(on_press=Menu.mostraFeed)
        Grid.add_widget(btn1)

        btn2 = BtnMenu(
            text = "PERFIL"
        )
        btn2.bind(on_press=Menu.mostraPerfil)
        Grid.add_widget(btn2)
        
        btn3 = BtnMenu(
            text = "PESQUISAR"
        )
        btn3.bind(on_press=Menu.mostraPesquisar)
        Grid.add_widget(btn3)

        # Botão "coxinhar"
        anchor = AnchorLayout(anchor_x="right", anchor_y="bottom", padding=10)
        coxinhar = Btn(
            background_normal="telas/imagens/coxinhar.png",
            background_down="telas/imagens/coxinhar.png",
            border=(0,0,0,0),
            size_hint=(None,None)
        )
        coxinhar.bind(on_press=Menu.Coxinhar)
        anchor.add_widget(coxinhar)

        box.add_widget(anchor)
        box.add_widget(Grid)

        #Tratamento estético nos botões
        # Todos os botões recebem a fonte normal
        btn1.font_name="telas/fontes/NewsCycle.ttf"
        btn2.font_name="telas/fontes/NewsCycle.ttf"
        btn3.font_name="telas/fontes/NewsCycle.ttf"

        lista=[btn1,btn2,btn3]

        # O botão correspondente ao número indicado recebe a fonte bold
        lista[num-1].font_name="telas/fontes/NewsCycle-Bold.ttf"

        return box

    def mostraFeed(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="feed"
        manager.transition = SlideTransition()

    def mostraPerfil(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="perfil"
        manager.transition = SlideTransition()

    def mostraPesquisar(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="pesquisar"
        manager.transition = SlideTransition()

    def Coxinhar(self, *args):
        # Cria o popup de nova postagem a tela
        box = BoxLayout(size_hint_y=None)

        getText = CaixaTexto(size_hint_y=None)
        box.add_widget(getText)

        postar = Button(
            text="Coxinhar",
            size_hint_y=None,
            background_normal="",
            background_color="#CCEAFF"
        )
        box.add_widget(postar)

        popup = Popup(
            separator_color=(.8, .91, 1, 1),
            title='Nova postagem',
            title_color=(0,0,0,1),
            title_size="18sp",
            content=box,
            size_hint=(.9, .8),
            pos_hint={"top":.9},
            background="",
            background_color=(.98, .98, .98, 1)

        )
        popup.open()
        