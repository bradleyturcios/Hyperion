from __future__ import print_function
from os import environ

from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    """
    An application component that publishes an event every second.
    """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        counter = 0
        while True:
            self.publish(u'com.myapp.topic1', counter)
            counter += 1
            yield sleep(1)


if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://localhost:8080/ws", realm = u"realm1")
    runner.run(Component)
