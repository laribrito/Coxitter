from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

Builder.load_file("telas/perfil.kv")

#class appConfig
from appConfig import AppConfig

class Perfil(Screen):
    #Elementos da tela .kv
    setNome = ObjectProperty(None)
    setLogin = ObjectProperty(None)
    def retornaPerfil(self, login):
        UrlRequest(f'http://127.0.0.1:5000/api/perfil/{login}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                on_success = self.perfil_sucesso,
                on_error = self.erro,
            )

            # UrlRequest(f"{AppConfig.servidor}/api/foto/{login}",
            #     req_headers = {
            #         'Authorization': f'Bearer {AppConfig.get_config("token")}'
            #     },
            #     on_success = self.foto_sucesso,
            #     on_error = self.erro,
            # )
    
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
        else:
            # Exibe a mensagem de erro na resposta
            self.setNome.text = ''
            self.setLogin.text = resposta['msg']

    '''
    Efetua o tratamento em caso de erro ao efetuar a requisição.
    '''
    def erro(self, req, erro):
        self.setNome.text = ''
        self.setLogin.text = 'Erro.'


