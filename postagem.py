from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.image import AsyncImage

class Mensagem(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = 1

    def on_size(self, *args):
        self.text_size = self.width, None
        self.size = self.texture_size

class Postagem(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout=GridLayout(
            cols=2
        )

        #Imagem de perfil
        imgPerfil=AsyncImage(
            source="telas/imagens/padrao.png",
            size_hint_x = 0.3,
            
        )
        layout.add_widget(imgPerfil)

        box=BoxLayout(
        )
        print(box.width)

        #Nome e login
        gridNome=GridLayout(
            spacing = 20,
            cols=2
        )
        labelNome=Label(
            text="FuracãoDaCPI"
        )
        labelLogin=Label(
            text="@robsu"
        )
        gridNome.add_widget(labelNome)
        gridNome.add_widget(labelLogin)
        box.add_widget(gridNome)

        #Texto da mensagem
        labelTexto=Mensagem(
            text="Gente, fui hackeado! se eu aparecer no privado pedindo 5000 reais, sou eu mesmo! pfv paguem"

        )
        box.add_widget(labelTexto)

        #Botões
        gridIcones=GridLayout(
            cols=2
        )
        btnCurtir=Button(background_normal='telas/imagens/curtir.png')
        btnComentar=Button(background_normal='telas/imagens/comentario.png')
        gridIcones.add_widget(btnCurtir)
        gridIcones.add_widget(btnComentar)
        box.add_widget(gridIcones)

        #Data e hora
        labelDataHora=Label(
            text="08/12/2021 · 22:30"
        )
        box.add_widget(labelDataHora)

        #Termina de montar o grid
        layout.add_widget(box)

        #Armazena em um boxlayout
        self.add_widget(layout)

        #Para poder adicionar essa linha no fim
        imgLinha=AsyncImage(source='telas/imagens/barrinha.png')
        self.add_widget(imgLinha)

        self.bind(pos=self.update_rect, size=self.update_rect)
        
        with self.canvas.before:
            Color(.80, .91, 1, 1)
            #ARMAZENANDO A FORMA EM UMA VARIÁVEL
            self.rect=Rectangle(pos=self.pos, size=self.size)
    
    def update_rect(instance, value, *args):
        #E ATUALIZANDO ELA ATRAVÉS DE UMA FUNÇÃO
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size