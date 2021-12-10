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

    btnSeguir = Button(
            font_name='telas/fontes/NewsCycle.ttf',
            background_color="#A3C0FF",
            color=(.2, .2, .2,1),
            background_normal="",
    )

    #Elementos da tela .kv
    setNome = ObjectProperty(None)
    setLogin = ObjectProperty(None)
    setFoto = ObjectProperty(None)
    caixinha = ObjectProperty(None)
    setBtnSeguir = ObjectProperty(None)
    setSeguidores = ObjectProperty(None)
    setSeguindo = ObjectProperty(None)

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

        #busca os seguidores
        UrlRequest(f'http://127.0.0.1:5000/api/feed_SEGUIDORES/{login}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.seguidores_sucesso
        )

        #busca quem o usuario segue
        UrlRequest(f'http://127.0.0.1:5000/api/feed_SEGUINDO/{login}',
            req_headers = {
                'Authorization': f'Bearer {AppConfig.get_config("token")}'
            },
            on_success = self.seguindo_sucesso
        )

    def testeSeguindo(self, req, resposta):
        self.btnSeguir.bind(on_press=self.funcaoBtnSeguir)
        if resposta["status"] == 0:
            self.setBtnSeguir.clear_widgets()
            #mostra o botão de deixar de seguir
            self.btnSeguir.text="Deixar de seguir"
            self.setBtnSeguir.add_widget(self.btnSeguir)
        else:
            self.setBtnSeguir.clear_widgets()
            #mostra o botão de seguir
            self.btnSeguir.text="Seguir"
            self.setBtnSeguir.add_widget(self.btnSeguir)

    def seguidores_sucesso(self, req, resposta):
        num = resposta["lista"]
        num = len(num)
        if num == 1:
            self.setSeguidores.text=f"1 seguidor"
        else:
            self.setSeguidores.text=f"{num} seguidores"
    
    def seguindo_sucesso(self, req, resposta):
        num = resposta["lista"]
        self.setSeguindo.text=f"{len(num)} seguindo"

    def funcaoBtnSeguir(instance, *args):
        texto = instance.btnSeguir.text
        login = instance.setLogin.text
        login = login[1:len(login)]
        if texto == "Seguir":
            instance.btnSeguir.text = "Deixar de seguir"
            num = instance.setSeguidores.text
            num = num.split(sep=" ")
            num = int(num[0])
            num +=1
            if num == 1:
                instance.setSeguidores.text = f"1 seguidor"
            else:
                instance.setSeguidores.text = f"{num} seguidores"
            
            UrlRequest(f'http://127.0.0.1:5000/api/seguir/{login}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                method="POST"
            )
        else:
            instance.btnSeguir.text = "Seguir"
            num = instance.setSeguidores.text
            num = num.split(sep=" ")
            num = int(num[0])
            num -=1
            if num == 1:
                instance.setSeguidores.text = f"1 seguidor"
            else:
                instance.setSeguidores.text = f"{num} seguidores"

            UrlRequest(f'http://127.0.0.1:5000/api/unfollow/{login}',
                req_headers = {
                    'Authorization': f'Bearer {AppConfig.get_config("token")}'
                },
                method="DELETE"
            )

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