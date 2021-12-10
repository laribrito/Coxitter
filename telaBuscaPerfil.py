from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from menu import Menu
from titulo import Titulo
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

#class appConfig
from appConfig import AppConfig
from postagem import Postagem


 #Carrega a interface
Builder.load_file('telas/buscaPerfil.kv')

class BuscaPerfil(Screen):
    menu = Menu(3)

    #Elementos da tela .kv
    setNome = ObjectProperty(None)
    setLogin = ObjectProperty(None)
    setFoto = ObjectProperty(None)
    caixinha = ObjectProperty(None)
    setBtnSeguir = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        # Adiciona o menu a tela
        self.add_widget(self.menu)
        Titulo(self, "Resultado")

    def mostraPerfil(self, resposta, *args):
        login = resposta["login"]
        self.setNome.text =  resposta['nome']
        self.setLogin.text = f'@{login}'

        #busca a foto do usuário
        UrlRequest(f"http://127.0.0.1:5000/api/foto/{login}",
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.foto_sucesso,
            on_error = self.erro,
        )    

        #busca as mensagens
        UrlRequest(f'http://127.0.0.1:5000/api/buscar_msg/{login}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.postagens_sucesso
        )

        #verifica se está seguindo
        UrlRequest(f"http://127.0.0.1:5000/api/confere_follow/{login}",
        req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
        },
        on_success=self.testeSeguindo,
        on_error=self.erro
        )

    def testeSeguindo(self, req, resposta):
        btnSeguir = Button(
            font_name='telas/fontes/NewsCycle.ttf',
            background_color="#A3C0FF",
            color=(.2, .2, .2,1),
            background_normal="",
        )
        if resposta["status"] == 0:
            self.setBtnSeguir.clear_widgets()
            #mostra o botão de deixar de seguir
            btnSeguir.text="Deixar de seguir"
            self.setBtnSeguir.add_widget(btnSeguir)
        else:
            self.setBtnSeguir.clear_widgets()
            #mostra o botão de seguir
            btnSeguir.text="Seguir"
            self.setBtnSeguir.add_widget(btnSeguir)

    def erro(self, req, erro):
        self.setNome.text = ''
        self.setLogin.text = 'Não foi possível conectar ao servidor.\nTente novamente mais tarde.'

    def foto_sucesso(self, req, resposta):
        if (resposta['status'] == 0):
            # Atualiza a foto na interface
            self.setFoto.source = resposta['url']
            self.setFoto.reload()

    def postagens_sucesso(self, req, resposta):
        self.caixinha.clear_widgets()
        if (resposta['status'] == 0):
            # Exibe os dados do feed na interface
            lista = resposta['lista']
            for post in lista:
                armazem = Postagem(
                    nome = post['nome'],
                    usuario = post['usuario'],
                    mensagem = post['texto'],
                    data_hora = post['datahora'],
                    fota = post['foto']
                )
                self.caixinha.add_widget(armazem)