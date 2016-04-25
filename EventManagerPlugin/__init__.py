from Coronado.Plugin import AppPlugin as AppPluginBase
from Coronado.Config import Config as ConfigBase

class Config(ConfigBase):

    def __init__(self, keys=None): 
        if keys is None:
            keys = []
        super().__init__(
        [
            'eventManagerName'
        ] + keys)

    def _getEventManagerName(self):
        return 'eventManager'


class AppPlugin(AppPluginBase):
    context = None

    # pylint: disable=unused-argument
    def start(self, app, context):
        self.context = context
        self.context['eventManager'] = self.makeEventManager()
        self.context['shortcutAttrs'].append('eventManager')


    def makeEventManager(self):
        raise NotImplementedError()


class EventManager(object):

    def __init__(self, name, ioloop):
        self.name = name
        self.ioloop = ioloop is not None and ioloop or IOLoop.current()
        self.messageHandlers = {}

    def start(self):
        pass


    def on(self, eventType, listener, sourceId=None, listenerId=None):
        '''
        Listen for an event on the given source.

        sourceId: ID of the event source
        eventType: type of event for which to listen
        listener: function to call when the specified event occurs
        listenerId: ID of this event listening request (default None
            means listener ID will be auto-generated)
        '''
        raise NotImplementedError()


    def trigger(self, eventType, **kwargs):
        raise NotImplementedError()


    def off(self, listenerId):
        raise NotImplementedError()


    def _onEvent(self, listenerId, **kwargs):
        # Call message handler associated with the binding ID, if any
        if listenerId in self.messageHandlers:
            self.messageHandlers[listenerId](**kwargs)


    def _saveHandler(self, listenerId, messageHandler):
        self.messageHandlers[listenerId] = messageHandler
