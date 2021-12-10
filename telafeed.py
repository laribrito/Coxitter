from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from kivy.uix.boxlayout import BoxLayout
from titulo import Titulo
from kivy.properties import ObjectProperty
from postagem import Postagem
from kivy.network.urlrequest import UrlRequest

#class appConfig
from appConfig import AppConfig

# Carrega a interface
Builder.load_file('telas/feed.kv')

class Fundo(Screen):
    caixinha = ObjectProperty(None)
    rolagem = ObjectProperty(None)
    menu = Menu(1)
    numSeguidores = -1
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        self.add_widget(self.menu)
        #Adiciona o título
        Titulo(self, "Meu Feed")

        self.atualizar()

    def feed_seguidores(self, login):
        UrlRequest(f'http://127.0.0.1:5000/api/feed/{login}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.feed_sucesso
        )

    def atualizar(self):
        UrlRequest(f'http://127.0.0.1:5000/api/feed_SEGUINDO/{AppConfig.get_config("login")}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.atualizar_sucesso
        )

    def atualizar_sucesso(self, req, resposta):
        tamanho = len(resposta["lista"])
        print(tamanho)
        if self.numSeguidores != tamanho:
            print("tem que atualizar")
            self.feed_seguidores(AppConfig.get_config("login"))
            self.numSeguidores = tamanho
            print(tamanho)
        else:
            print("não precisa")

    def feed_sucesso(self, req, resposta):
        #Limpa o widget
        self.caixinha.clear_widgets()
        #Depois adiciona
        if (resposta['status'] == 0):
            # Exibe os dados do feed na interface
            lista = resposta['lista']
            for post in lista:
                armazem = Postagem(
                    nome = post['nome'],
                    usuario = post['usuario'],
                    mensagem = post['texto'],
                    data_hora = post['datahora'],
                    fota = post['foto'],
                    id_post = post["id_post"],
                    quantCurtidas = post["quantCurtidas"]
                )
                self.caixinha.add_widget(armazem)
            self.rolagem.scroll_y=1
