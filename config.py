from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("config.kv")

class config(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return config()

if __name__ == '__main__':
    MyApp().run()
