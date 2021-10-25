from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

# Carrega tela kivy de Edição de Nome
Builder.load_file("telas/mudarNome.kv")

from appConfig import AppConfig

class MudarNome(Screen):
       #Elementos da interface
   setMensagem = ObjectProperty(None)
   getNome = ObjectProperty(None)
   
   def mudarnome(self, nome):
      UrlRequest(
         "http://127.0.0.1:5000/api/mudarNome",
         on_success=self.mudarnome_sucesso,
         on_error=self.mudarnome_erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
         },
         req_body = urlencode({
                'nome': nome
            }),
        )
   def login_sucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Sucesso! Salva o token e o nome do usuário.
         AppConfig.set_config('token', resposta['token'])
         AppConfig.set_config('nome', self.getNome.text)

         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'left'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('login'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']