from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

# Carrega a interface
Builder.load_file('telas/mudarBio.kv')

from appConfig import AppConfig

class MudarBio(Screen):
   setMensagem = ObjectProperty(None)
   getNome = ObjectProperty(None)
   
   def mudarbio(self, bio):
      UrlRequest(
         "http://127.0.0.1:5000/api/mudarBio",
         on_success=self.mudarbio_sucesso,
         on_error=self.mudarbio_erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
         },
         req_body = urlencode({
                'bio': bio
            }),
        )
   def mudarbio_sucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Sucesso! Salva o token e o nome do usuário.
         AppConfig.set_config('token', resposta['token'])
         AppConfig.set_config('bio', self.getBio.text)

         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'left'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('bio'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']