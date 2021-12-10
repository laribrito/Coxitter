from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from urllib.parse import urlencode

# Carrega a interface
Builder.load_file('telas/login.kv')

# Classe AppConfig
from appConfig import AppConfig

class Login(Screen):
   #Elementos da interface
   setMensagem = ObjectProperty(None)
   getLogin = ObjectProperty(None)
   
   def entrar(self, login, senha):
      UrlRequest(
         f"{AppConfig.servidor}/api/login",
         on_success=self.login_sucesso,
         on_error=self.login_erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
         },
         req_body = urlencode({
                'login': login,
                'senha1': senha
            }),
        )
   def login_sucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Sucesso! Salva o token e o login do usuário.
         AppConfig.set_config('token', resposta['token'])
         AppConfig.set_config('login', self.getLogin.text)

         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'left'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('login'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']
   
   def login_erro(self, req, erro):
      self.setMensagem.text = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'