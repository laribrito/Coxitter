from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.image import AsyncImage

class Postagem():
    def __init__(self) -> None:
        tudo=BoxLayout()

        layout=GridLayout(
            cols=2
        )

        #Imagem de perfil
        imgPerfil=AsyncImage(
            source=""
        )
        layout.add_widget(imgPerfil)

        box=BoxLayout(
            orientation="vertical"
        )

        #Nome e login
        gridNome=GridLayout(
            cols=2
        )
        labelNome=Label(
            text="Robsu"
        )
        labelLogin=Label(
            text="@robsu"
        )
        gridNome.add_widget(labelNome)
        gridNome.add_widget(labelLogin)
        box.add_widget(gridNome)

        #Texto da mensagem
        labelTexto=Label(
            text="Mensagem"
        )
        box.add_widget(labelTexto)

        #Botões
        gridIcones=GridLayout(
            cols=2
        )
        btnCurtir=Button()
        btnComentar=Button()
        gridIcones.add_widget(btnCurtir)
        gridIcones.add_widget(btnComentar)
        box.add_widget(gridIcones)

        #Data e hora
        labelDataHora=Label(
            text="Hoje e agora"
        )
        box.add_widget(labelDataHora)

        #Termina de montar o grid
        layout.add_widget(box)

        #Armazena em um boxlayout
        tudo.add_widget(layout)

        #Para poder adicionar essa linha no fim
        imgLinha=AsyncImage()
        tudo.add_widget(imgLinha)
