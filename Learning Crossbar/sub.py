from __future__ import print_function
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import time


class MyComponent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def oncounter(count):
            print("event received: {0}", count)

        try:
            yield self.subscribe(oncounter, u'com.myapp.oncounter')
            print("subscribed to topic")
        except Exception as e:
            print("could not subscribe to topic: {0}".format(e))
if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://192.168.2.2:8080/ws", realm=u"realm1")
    runner.run(MyComponent)
