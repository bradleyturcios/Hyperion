""" Just a note, the below code looks pretty simple and empty because the kivy language was used. This is its own language with its own syntax, specifically for kivy. All that code is in the other folder
below we tell python to expect this window and this widget, which are the classes, but we tell python what to do with these widgets: size, position, order, basically how it will look, in the kivy language.
That code is in the other file, the mc.kv file in this case, and "loaded" onto this script below"""

from kivy.app import App                 #Add the ability to create applications
from kivy.uix.boxlayout import BoxLayout  # Adding the BoxLayout, that is ability to organize widgets in a box like way.
from kivy.uix.label import Label           #Add the ability to create Labels. Basically textboxes.
from kivy.uix.widget import Widget      #Give ability to understand that you are going to be adding a widget
                                        """ All of the above is just importing a bunch of libraries. Python can do a lot of computing, but it can't do everything.
                                            so someone else has written code for this before, and compiled it into libraries. We just "import" it and manipulate it to our need"""


class TitleWidget(Widget):          #Creating a class, called titlewidget, that will hold the two labels (textboxes) of the title
    pass                            #"Pass" just means do nothing and continue

class TextWidget(Widget):           #Creating a class, called textwidget, that will hold text, that is the sensor values.
    pass                            #Same pass as before

class MainWidget(Widget):            #Create a class that will be the main widget. This is where all the parts and widgets will be condensed into one window.
    pass                            #Same pass paas before

class MC(App):                      #This is the class we need to create for python. We inherit from App. That is, we tell this class to expect to use all of the components of an application.
    def build(self):                #Create the build function. This is function that will hold all of the rules for how the final application will look.
        self.load_kv('mc.kv')       #We tell the file to look at the mc.kv file.
        return Mainwidget()         #We then tell it which class is our main class, that is the one with all of th pieces condensed into one window. And we return it, thas is run it.

if __name__=="__main__":            #Some syntax stuff idk what this does, just know you need it for running object oriented programs.
    MC().run()                      # We tell python which one class is the one to run. In this case, the MC class is the one that builds the kivy application. That is we run mc, which knows how to display application,
                                    # because it inherits from app. MC runs mainwidget, which actually has all the python kivy gui make-me-pretty stuff.
