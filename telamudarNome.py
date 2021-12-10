from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from urllib.parse import urlencode

# Carrega tela kivy de Edição de Nome
Builder.load_file("telas/mudarNome.kv")

from appConfig import AppConfig

class MudarNome(Screen):
   #Elementos da interface
   setMensagem = ObjectProperty(None)
   
   def mudarnome(self, nome):
      UrlRequest(
         f"{AppConfig.servidor}/api/editarnome",
         on_success=self.editarNomeSucesso,
         on_error=self.erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain',
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
         },
         req_body = urlencode({
                'nome': nome,
                "login": AppConfig.get_config("login")
            }),
        )
   def editarNomeSucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'right'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('login'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']
   def erro(self, req, erro):
        self.setMensagem = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'