from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from urllib.parse import urlencode
from kivy.properties import ObjectProperty

# Carrega a interface
Builder.load_file('telas/cadastro.kv')

class Cadastro(Screen):
   #Elementos da interface
   setMensagem = ObjectProperty(None)

   def cadastrar(self, login, nome, senha1, senha2):
      UrlRequest(f'http://127.0.0.1:5000/api/cadastro',
            on_success = self.cadastro_sucesso,
            on_error = self.cadastro_erro,
            req_headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Accept': 'text/plain'
            },
            req_body = urlencode({
                'login': login,
                'senha1': senha1,
                'senha2': senha2,
                'nome': nome,
            }),
        )
    
   def cadastro_sucesso(self, req, resposta):
      if (resposta['status']) == 0:
         # Transiciona de volta à tela de login, com mensagem
         self.manager.transition.direction = 'right'
         self.manager.current = 'login'
         self.manager.current_screen.setMensagem.text = 'Cadastro efetuado!'
      else:
         # Exibe a mensagem de erro
         self.setMensagem.text = resposta['msg']

    
   def cadastro_erro(self, req, erro):
      self.setMensagem.text = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'