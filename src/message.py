
class Message(object):
    def __init__(self, user, message, chatroom):
        self._user = user
        self._message = message
        self._chatroom = chatroom
        
    @property
    def getMessage(self):
        return self._message
    
    @property
    def getChatroom(self):
        return self._chatroom
    
    @property
    def getUser(self):
        return self._user
    
    
    
            