from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("editfoto.kv")

class editfoto(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return editfoto()

if __name__ == '__main__':
    MyApp().run()
