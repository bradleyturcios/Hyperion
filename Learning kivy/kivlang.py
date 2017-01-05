from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
 

class titlewidget(Widget):
    pass

class textwidget(Widget):
    pass

class mainwidget(Widget):
    pass

class MC(App):
    
    def build(self):
        self.load_kv('mc.kv')
        return mainwidget()

if __name__=="__main__":
    MC().run()
