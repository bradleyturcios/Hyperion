from __future__ import print_function
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    
    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        self.received = 0
        sub = yield self.subscribe(self.on_event, u"com.example.event")
        print("Subscribed to com.example.kivy")
        
    def on_event(self):
        print("Got event:")
        im = open("screenshot1.png", mode='rb')
        self.publish(u"com.example.kivy", str(im.read()))
        im.close()

    def onDisconnect(self):
        print("disconnected")
        if reactor.running:
            reactor.stop()


if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://192.168.1.130:8080/ws", realm=u"realm1")
    runner.run(Component)
