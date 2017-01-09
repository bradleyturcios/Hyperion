from kivy.app import App                 #Add the ability to create applications
from kivy.uix.boxlayout import BoxLayout  # Adding the BoxLayout, that is ability to organize widgets in a box like way.
from kivy.uix.label import Label           #Add the ability to create Labels. Basically textboxes.
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class BBox(BoxLayout):
    pass

class Img(App):
    def build(self):
        return BBox()

if __name__ == '__main__':
    Img().run()
