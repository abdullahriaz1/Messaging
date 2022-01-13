from message import Message
class Chatroom(object):
    def __init__(self, server, lifetime, chatRoomIdentifier, chatName):
        self._lifetime = lifetime
        self._chatroomIdentifier = chatRoomIdentifier
        self._users = []
        self._messageList = []
        self._chatName = chatName
        
    @property
    def getChatroomIdentifier(self):
        return self._chatroomIdentifier
    
    @property
    def getUsersInChatroom(self):
        return self._users
    
    @property
    def getMessages(self):
        return self._messageList
    
    def addUser(self,user):
        self._users.append(user)
        return user.getName
    
    def removeUser(self,user):
        self._users.remove(user)
        return user.getName
    
    def removeAllUsers(self):
        allUsersRemoved = self.getUsersInChatroom
        for user in allUsersRemoved:
            user.setCurrentChatroom(None)
        self._users = []
        return allUsersRemoved
    
    def sendMessage(self, user, message):
        newMessage = Message(user, message, self)
        self._messageList.append(newMessage)
        return newMessage
    
    
        
            
        