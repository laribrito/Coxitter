from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("editarbio.kv")

class editarbio(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return editarbio()

if __name__ == '__main__':
    MyApp().run()
