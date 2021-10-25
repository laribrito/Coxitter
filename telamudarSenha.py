from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

# Carrega tela kivy de Edição de Senha
Builder.load_file("telas/mudarSenha.kv")

from appConfig import AppConfig

class MudarSenha(Screen):
    #Elementos da interface
   setMensagem = ObjectProperty(None)
   getNome = ObjectProperty(None)
   
   def mudarsenha(self, senha1, senha2):
      UrlRequest(
         "http://127.0.0.1:5000/api/mudarSenha",
         on_success=self.mudarsenha_sucesso,
         on_error=self.mudarsenha_erro,
         req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
         },
         req_body = urlencode({
                'senha1': senha1,
                'senha2': senha2
            }),
        )
   def mudarsenha_sucesso(self, req, resposta):
      if (resposta['status'] == 0):
         # Sucesso! Salva o token e a senha do usuário.
         AppConfig.set_config('token', resposta['token'])
         AppConfig.set_config('senha1', self.getSenha1.text)
         AppConfig.set_config('senha2', self.getSenha2.text)


         # Transiciona para a tela de perfil
         self.manager.transition.direction = 'left'
         self.manager.current = 'perfil'
         self.manager.current_screen.retornaPerfil(AppConfig.get_config('login'))
      else:
         # Exibe a mensagem de erro na resposta
         self.setMensagem.text = resposta['msg']