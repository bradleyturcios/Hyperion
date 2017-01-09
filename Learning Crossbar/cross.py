rom autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks

class MyComponent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        counter = 0
        while True:
            self.publish(u'com.myapp.oncounter', counter)
            counter += 1
            yield sleep(1)
