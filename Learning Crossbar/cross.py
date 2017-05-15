from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
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
if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://192.168.2.2:8080/ws", realm=u"realm1")
    runner.run(MyComponent)


