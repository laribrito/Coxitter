from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("editarperfil.kv")

class editperf(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return editperf()

if __name__ == '__main__':
    MyApp().run()
