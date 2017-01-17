from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks


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
