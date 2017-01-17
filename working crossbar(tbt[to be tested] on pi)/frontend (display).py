from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.support import install_twisted_reactor
install_twisted_reactor()
from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from kivy.uix.image import Image as Image2


class MyComponent(ApplicationSession):

    def onJoin(self, details):
        print("session ready", self.config.extra)

        ui = self.config.extra['ui']
        ui.on_session(self)

        self.subscribe(ui.display_pict, u"com.example.kivy")


class CrossbarKivyApp(App):


    def build(self):
        
        self.session = None

        runner = ApplicationRunner(url = u"ws://192.168.1.130/ws", realm = u"realm1", extra = dict(ui=self))
        runner.run(MyComponent, start_reactor=False)

        root = self.setup_gui()
        return root

    def setup_gui(self):

        self.layout = BoxLayout()
        self.button = Button(text='Get Picture')
        self.button.bind(on_press = self.ask_pict)
        self.image = Image2(source = 'k.png')
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.button)
        return self.layout

    def on_session(self, session):

        self.session = session

    def ask_pict(self, *arg):
        print('num')
        self.session.publish(u"com.example.kivy", 'text')

    def display_pict(self, im):

        f = open("k.png" , mode= "wb")
        f.write(im)
        f.close()
        self.image.reload()

        

if __name__ == '__main__':
    CrossbarKivyApp().run()
