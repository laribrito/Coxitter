from os import name
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        from telalogin import Login
        sm.add_widget(Login(name='login'))
        from telacadastro import Cadastro
        sm.add_widget(Cadastro(name='cadastro'))
        from telaperfil import Perfil
        sm.add_widget(Perfil(name='perfil'))
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
        return sm

if __name__ == '__main__':
    MyApp().run()
