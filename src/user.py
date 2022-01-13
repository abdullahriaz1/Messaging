class User(object):
    def __init__(self, name, userIdentifier):
        self._name = name
        self._userIdentifier = userIdentifier
        self._currentChatroom = None
        
    @property
    def getName(self):
        return self._name
    
    def setName(self, newName):
        self._name = newName
        return self._name
    
    @property
    def getCurrentChatroom(self):
        return self._currentChatroom
    
    def setCurrentChatroom(self, chatroom):
        
        self._currentChatroom = chatroom
        return self._currentChatroom
    
    @property
    def getUserIdentifier(self):
        return self._userIdentifier
        

        