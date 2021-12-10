from os import name
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

#classe appConfig
from appConfig import AppConfig

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        # Se existir token, abre já o perfil. Se não, abre a tela de login.
        
        if (AppConfig.get_config('token') != None):
            from telaperfil import Perfil
            perfil = Perfil(name='perfil')
            AppConfig.telas.append(perfil)
            sm.add_widget(perfil)
            sm.current_screen.retornaPerfil(AppConfig.get_config('login'))
            from telalogin import Login
            sm.add_widget(Login(name='login'))
        else:
            from telalogin import Login
            sm.add_widget(Login(name='login'))
            from telaperfil import Perfil
            perfil = Perfil(name='perfil')
            AppConfig.telas.append(perfil)
            sm.add_widget(perfil)

        # Carrega as outras telas
        from telacadastro import Cadastro
        sm.add_widget(Cadastro(name='cadastro'))
        from telaMudarFoto import MudarFoto
        sm.add_widget(MudarFoto(name='mudarFoto'))
        from telaconfig import Config
        sm.add_widget(Config(name='config'))
        from telaMudarBio import MudarBio
        sm.add_widget(MudarBio(name='mudarBio'))
        from telamudarSenha import MudarSenha
        sm.add_widget(MudarSenha(name='mudarSenha'))
        from telamudarNome import MudarNome
        sm.add_widget(MudarNome(name='mudarNome'))
        from telafeed import Fundo
        fundo = Fundo(name='feed')
        AppConfig.telas.append(fundo)
        sm.add_widget(fundo)
        #from telafeed import Feed
        #sm.add_widget(Feed(name='feed'))
        from telapesquisar import Pesquisar
        sm.add_widget(Pesquisar(name='pesquisar'))
        from telaBuscaPerfil import BuscaPerfil
        sm.add_widget(BuscaPerfil(name='buscaPerfil'))

        AppConfig.manager = sm 

        return sm

if __name__ == '__main__':
    MyApp().run()
