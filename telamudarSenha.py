from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from urllib.parse import urlencode

# Carrega tela kivy de Edição de Senha
Builder.load_file("telas/mudarSenha.kv")

from appConfig import AppConfig

class MudarSenha(Screen):
    #Elementos da interface
   setMensagem = ObjectProperty(None)
   getNome = ObjectProperty(None)
   
   def mudarsenha(self, senha1, senha2):
      UrlRequest(
         f"{AppConfig.servidor}/api/editarsenha",
         on_success=self.mudarsenha_sucesso,
         on_error=self.mudarsenha_erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain',
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
         },
         req_body = urlencode({
                'senha1': senha1,
                'senha2': senha2, 
                "login": AppConfig.get_config("login")
            }),
        )
   def mudarsenha_sucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'right'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('login'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']

   def mudarsenha_erro(self, req, erro):
      self.setMensagem = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'