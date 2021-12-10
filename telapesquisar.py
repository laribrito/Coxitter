from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from titulo import Titulo
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivy.properties import ObjectProperty

#class appConfig
from appConfig import AppConfig

# Carrega a interface
Builder.load_file('telas/pesquisar.kv')

class Pesquisar(Screen):
    setMensagem = ObjectProperty(None)
    menu = Menu(3)
    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        self.add_widget(self.menu)
        Titulo(self, "Pesquisar")

    def buscaPerfil(self, login):
        UrlRequest(f'{AppConfig.servidor}/api/perfil/{login}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                on_success = self.busca_sucesso,
                # on_error = self.erro,
            )

    def busca_sucesso(self, req, resposta):
        if resposta["status"] == 0:
            if resposta["login"] == AppConfig.get_config("login"):
                self.manager = AppConfig.manager
                self.manager.transition.direction = 'right'
                self.manager.current="perfil"
                self.manager.transition = SlideTransition()
            else:
                self.manager.current = 'buscaPerfil'
                self.manager.transition.direction = 'left'
                self.manager.current_screen.mostraPerfil(resposta)
                self.setMensagem.text=""
        else:
            self.setMensagem.text=resposta["msg"]
    