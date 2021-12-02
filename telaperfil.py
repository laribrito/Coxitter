from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from menu import Menu
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
Builder.load_file("telas/perfil.kv")

#class appConfig
from appConfig import AppConfig

#Classe para título 
class Titulo(Label):
    #QUANDO TRABALHAR COM O TAMANHO TEM QUE USAR O DEF ON_SIZE()
    def on_size(self, *args):
        self.halign="right"
        self.text_size=self.size

class Perfil(Screen):
    #Elementos da tela .kv
    setNome = ObjectProperty(None)
    setLogin = ObjectProperty(None)
    setFoto = ObjectProperty(None)

    #Barra superior
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(size_hint_y=0.1, pos_hint={"top": 1})
        titulo = Titulo(text="Perfil")
        layout.add_widget(titulo)
        self.add_widget(layout)

    def retornaPerfil(self, login):
        UrlRequest(f'http://127.0.0.1:5000/api/perfil/{login}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                on_success = self.perfil_sucesso,
                on_error = self.erro,
            )

        UrlRequest(f"http://127.0.0.1:5000/api/foto/{login}",
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.foto_sucesso,
            on_error = self.erro,
        )
    
    '''
    Recebe a resposta da requisição do perfil.
    Em caso de sucesso, exibe os dados do perfil.
    Em caso de erro, exibe uma mensagem vermelha.
    '''
    def perfil_sucesso(self, req, resposta):
        if (resposta['status'] == 0):
            # Exibe os dados do perfil na interface
            self.setNome.text =  resposta['nome'] 
            self.setLogin.text = f'@{resposta["login"]}'
            # Adiciona o menu a tela
            menu = Menu.criar(2)
            self.add_widget(menu)
        else:
            # Exibe a mensagem de erro na resposta
            self.setNome.text = ''
            self.setLogin.text = resposta['msg']

    '''
    Efetua o tratamento em caso de erro ao efetuar a requisição.
    '''
    def erro(self, req, erro):
        self.setNome.text = ''
        self.setLogin.text = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'

    def foto_sucesso(self, req, resposta):
        if (resposta['status'] == 0):
            # Atualiza a foto na interface
            self.setFoto.source = resposta['url']
            self.setFoto.reload()
    
    def sair(self):
        UrlRequest(f'http://127.0.0.1:5000/api/sair',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.saida_sucesso,
            on_error = self.erro,
        )
        AppConfig.set_config('token', None)
        
    def saida_sucesso(self, req, resposta):
        if (resposta['status'] == 0):
            self.manager.transition.direction = 'right'
            self.manager.current = 'login'

