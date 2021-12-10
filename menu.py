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
from kivy.network.urlrequest import UrlRequest
from urllib.parse import urlencode

global x 
x=0

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

class PopUpCoxinhar(Popup):
    getText = CaixaTexto(
        size_hint_y=0.3
    )
    setMensagem = Label(
        size_hint_y= 0.3,
        text="",
        color=(0,0,0,1)
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Cria o popup de nova postagem a tela
        label = Label(
            size_hint_y= 0.1,
            text="Coxinhe sobre o que está acontecendo...",
            color=(0,0,0,1)
        )

        box = BoxLayout(
            size_hint_y=1,
            orientation="vertical",
            padding=30,
            spacing=20
        )

        box.add_widget(label)
        box.add_widget(self.setMensagem)
        box.add_widget(self.getText)
        

        postar = Button(
            text="Coxinhar",
            size_hint_y=0.2,
            background_normal="",
            background_color="#CCEAFF",
            color=(0,0,0,1)
        )

        postar.bind(on_press=self.postar)
        box.add_widget(postar)
        box.add_widget(Label(text="",size_hint_y=0.2))

        self.separator_color=(0.8, 0.91, 1, 1)
        self.title='Nova postagem'
        self.title_color=(0,0,0,1)
        self.title_size="18sp"
        self.content=box
        self.size_hint=(.9, .8)
        self.pos_hint={"top":.9}
        self.background=""
        self.background_color=(.98, .98, .98, 1)

    def postar(self, *args):
        mensagem = self.getText.text
        UrlRequest(f"{AppConfig.servidor}/api/Postagem",
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}',
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
            },
            req_body = urlencode({
                'corpo': mensagem,
            }),
            on_success = self.postar_sucesso
        )

    def postar_sucesso(self, req, resposta):
        self.setMensagem.text=resposta["msg"]
        self.getText.text=""
    
class Menu(BoxLayout):
    popCox = PopUpCoxinhar()
    def __init__(self, num, **kwargs):
        super().__init__(**kwargs)

        self.popCox.bind(on_dismiss=self.atualizaAi)

        self.padding=0
        self.spacing=0

        # Gridlayout para os botões
        Grid = GridLayout(
            cols = 3, 
            size_hint_y = None
        )

        # Botões
        btn1 = BtnMenu(
            text = "FEED"
        )
        btn1.bind(on_press=self.mostraFeed)
        Grid.add_widget(btn1)

        btn2 = BtnMenu(
            text = "PERFIL"
        )
        btn2.bind(on_press=self.mostraPerfil)
        Grid.add_widget(btn2)
        
        btn3 = BtnMenu(
            text = "PESQUISAR"
        )
        btn3.bind(on_press=self.mostraPesquisar)
        Grid.add_widget(btn3)

        # Botão "coxinhar"
        anchor = AnchorLayout(anchor_x="right", anchor_y="bottom", padding=10)
        coxinhar = Btn(
            background_normal="telas/imagens/coxinhar.png",
            background_down="telas/imagens/coxinhar.png",
            border=(0,0,0,0),
            size_hint=(None,None)
        )
        coxinhar.bind(on_press=self.Coxinhar)
        anchor.add_widget(coxinhar)

        self.add_widget(anchor)
        self.add_widget(Grid)

        #Tratamento estético nos botões
        # Todos os botões recebem a fonte normal
        btn1.font_name="telas/fontes/NewsCycle.ttf"
        btn2.font_name="telas/fontes/NewsCycle.ttf"
        btn3.font_name="telas/fontes/NewsCycle.ttf"

        lista=[btn1,btn2,btn3]

        # O botão correspondente ao número indicado recebe a fonte bold
        lista[num-1].font_name="telas/fontes/NewsCycle-Bold.ttf"
    def atualizaAi(self, *args):
        global x
        x+=1
        if x%4==0:
            perfil = AppConfig.telas[0]
            perfil.postagens(AppConfig.get_config('login'))

            feed = AppConfig.telas[1]
            feed.feed_seguidores(AppConfig.get_config('login'))

    def mostraFeed(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="feed"
        manager.transition = SlideTransition()
        manager.current_screen.atualizar()

    def mostraPerfil(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="perfil"
        manager.transition = SlideTransition()
        manager.current_screen.atualizaNumeros(AppConfig.get_config("login"))

    def mostraPesquisar(self, *args):
        manager = AppConfig.manager
        manager.transition = NoTransition()
        manager.current="pesquisar"
        manager.transition = SlideTransition()

    def Coxinhar(self, *args):
        self.popCox.open()