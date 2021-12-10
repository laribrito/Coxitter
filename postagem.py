from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.image import AsyncImage
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.properties import ObjectProperty

global x 
x=0

from appConfig import AppConfig

#Classe para o corpo da mensagem
class Mensagem(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = 1

        #Nunca tire essa linha se não seu aparelho vai explodir
        Clock.schedule_interval(self.atualizaLargura, 1/10)

    def atualizaLargura(self, *args):
        self.size= self.texture_size
        self.text_size = AppConfig.larguraBox, None
        
#Sem ela a mensagem não vai ficar legal
class Caixa(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(width=self.update_rect)
    
    def update_rect(instance, value, *args):
        global x
        if x < 4:
            #Armazena a largura do box lateral direito para passar ao labelMensagem
            AppConfig.larguraBox = instance.size[0]
        x+=1

#pode tirar dps
class Grid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(pos=self.update_rect, size=self.update_rect)
        
        with self.canvas.before:
            Color(.0, .11, 0.1, 1)
            #ARMAZENANDO A FORMA EM UMA VARIÁVEL
            self.rect=Rectangle(pos=self.pos, size=self.size)
    
    def update_rect(instance, value, *args):
        #E ATUALIZANDO ELA ATRAVÉS DE UMA FUNÇÃO
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

#classe para botão
class Botao(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size=(30,30)
        self.size_hint = (None, None)
        self.border=(0,0,0,0)

class DataHora(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size="15sp"
        self.halign = 'right'
        #QUANDO TRABALHAR COM O TAMANHO TEM QUE USAR O DEF ON_SIZE()
    def on_size(self, *args):
        #tamanho
        self.text_size=self.size

class Postagem(BoxLayout):
    btnCurtir=ObjectProperty(None)
    quantCurtidas = 0
    labelQuantC = ObjectProperty(None)
    id_post = 0
    def __init__(self, id_post, data_hora, quantCurtidas, nome, usuario, mensagem, fota, **kwargs):
        super().__init__(**kwargs)
        self.spacing=0
        self.padding=0

        self.quantCurtidas = quantCurtidas
        self.id_post = id_post

        layout=GridLayout(
            cols=2
        )

        #Imagem de perfil
        #LADO ESQUERDO
        imgPerfil=AsyncImage(
            source=fota,
            size_hint_x = 0.3,
            size_hint_y=1, #centraliza a imagem na postagem
            
        )
        layout.add_widget(imgPerfil)

        #Esse boxlayout está pegando algumas configurações padrão 
        # do nosso 'widgets_confi.kv'. Por isso algumas variáveis
        # são necessárias
        #LADO DIREITO
        box=Caixa(
            padding=0,
            spacing=40 
        )

        #Nome e login
        gridNome=GridLayout(
            spacing = 20,
            cols=2
        )
        labelNome=Label(
            text=nome
        )
        labelLogin=Label(
            text='@'+ usuario
        )
        gridNome.add_widget(labelNome)
        gridNome.add_widget(labelLogin)
        box.add_widget(gridNome)

        #Texto da mensagem
        labelTexto=Mensagem(
            text=mensagem

        )
        box.add_widget(labelTexto)

        #Botões
        gridIcones=GridLayout(
            cols=6,
            spacing=50
        )
        self.btnCurtir = Botao()
        btnComentar=Botao(
            background_normal='telas/imagens/comentario.png'
        )
        
        self.labelQuantC = Label(
            text=f"{quantCurtidas} curt."
        )

        gridIcones.add_widget(Label(text=""))
        gridIcones.add_widget(Label(text=""))
        gridIcones.add_widget(btnComentar)
        gridIcones.add_widget(self.btnCurtir)
        gridIcones.add_widget(self.labelQuantC)
        gridIcones.add_widget(Label(text=""))
        box.add_widget(gridIcones)

        #Data e hora
        labelDataHora=DataHora(
            text=data_hora
        )
        box.add_widget(labelDataHora)

        #Termina de montar o grid
        layout.add_widget(box)

        #Armazena em um boxlayout
        self.add_widget(layout)

        #Para poder adicionar essa linha no fim
        imgLinha=AsyncImage(
            source='telas/imagens/barrinha.png',
            # size_hint_y=0.4
        )
        self.add_widget(imgLinha)

        #busca quem o usuario segue
        UrlRequest(f'{AppConfig.servidor}//api/verifica_curtida/{id_post}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.curtida_sucesso
        )
    
    def curtida_sucesso(self, req, resposta):
        self.btnCurtir.bind(on_press=self.funcaoCurtida)
        if resposta["status"] == 0:
            #mostra o botao preenchido
            self.btnCurtir.background_normal='telas/imagens/curtido.png'
            self.btnCurtir.background_down='telas/imagens/curtido.png'
        else:
            #mostra a opção de curtir
            self.btnCurtir.background_normal='telas/imagens/curtir.png'
            self.btnCurtir.background_down='telas/imagens/curtir.png'

    def funcaoCurtida(instance, *args):
        botao = instance.btnCurtir
        quantL = instance.labelQuantC
        if botao.background_down == "telas/imagens/curtir.png":
            #postagem foi curtida
            botao.background_normal='telas/imagens/curtido.png'
            botao.background_down='telas/imagens/curtido.png'

            #label
            quant = quantL.text
            quant = quant.split(sep=" ")
            quant = int(quant[0])
            quant +=1
            quantL.text = f"{quant} curt."
            
            id_post = instance.id_post
            UrlRequest(f'{AppConfig.servidor}/api/curtir/{id_post}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                method="POST"
            )
        else:
            #postagem foi deixada de curtir
            botao.background_normal='telas/imagens/curtir.png'
            botao.background_down='telas/imagens/curtir.png'

            #label
            quant = quantL.text
            quant = quant.split(sep=" ")
            quant = int(quant[0])
            quant -=1
            quantL.text = f"{quant} curt."

            id_post = instance.id_post
            UrlRequest(f'{AppConfig.servidor}/api/descurtir/{id_post}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                method="DELETE"
            )
