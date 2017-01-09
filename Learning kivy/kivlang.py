""" Just a note, the below code looks pretty simple and empty because the kivy language was used. This is its own language with its own syntax, specifically for kivy. All that code is in the other folder
below we tell python to expect this window and this widget, which are the classes, but we tell python what to do with these widgets: size, position, order, basically how it will look, in the kivy language.
That code is in the other file, the mc.kv file in this case, and "loaded" onto this script below"""
from kivy.config import Config

Config.set('graphics', 'fullscreen', 'auto')

from kivy.app import App                 #Add the ability to create applications
from kivy.uix.boxlayout import BoxLayout  # Adding the BoxLayout, that is ability to organize widgets in a box like way.
from kivy.uix.label import Label           #Add the ability to create Labels. Basically textboxes.
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder
from kivy.base import runTouchApp
""" All of the above is just importing a bunch of libraries. Python can do a lot of computing, but it can't do everything.
so someone else has written code for this before, and compiled it into libraries. We just "import" it and manipulate it to our need"""


class Title(Widget):          #Creating a class, called titlewidget, that will hold the two labels (textboxes) of the title
    def __init__(self, **kwargs):
        super(Title, self).__init__(**kwargs)                          #"Pass" just means do nothing and continue

class Texty(Widget):           #Creating a class, called textwidget, that will hold text, that is the sensor values.
    def __init__(self, **kwargs):
        super(Texty, self).__init__(**kwargs)                           #Same pass as before

class Man(BoxLayout):
    def __init__(self, **kwargs):
        super(Man, self).__init__(**kwargs)

class ContBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContBox, self).__init__(**kwargs)

class TestApp(App):
    def build(self):
        return ContBox()
    
if __name__ == '__main__':
    TestApp().run()
