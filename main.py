from os import name
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from telalogin import Login
from telacadastro import Cadastro


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(Cadastro(name='cadastro'))
        from telaperfil import Perfil
        sm.add_widget(Perfil(name='perfil'))
        
        

        return sm

if __name__ == '__main__':
    MyApp().run()
