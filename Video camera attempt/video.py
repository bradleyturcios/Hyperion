from kivy.app import App                 
from kivy.uix.boxlayout import BoxLayout          
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.camera import Camera

#We above importing all the widgets we are going to use, such as a slider or the camera widget.

class VideoWidget(Widget):  #we create the class that will contain the widgets. From a display wise standpoint, this widget will be simple, thus all the layout will be in one class.
    def __init__(self, **kwargs):
        super(VideoWidget, self).__init__(**kwargs)                   #Do nothing becasue everythibng, for the most part, will be done in kivy language.

class Main(App):
    def build(self):
        return VideoWidget()

if __name__ == '__main__':
    Main().run()
