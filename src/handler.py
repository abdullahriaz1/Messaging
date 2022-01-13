from chatroom import Chatroom
from user import User
import time

class Handler(object):
    def __init__(self):
        '''
        We need to handle user creation and deletion, chatroom creation and deletion, 
        chatroom connection and disconnection, and the sending and receiving of 
        messages.
        '''
        self._chatrooms = []
        self._users = []
        self._userCounter = 0
        self._chatroomCounter = 0
    
    @property
    def getChatrooms(self):
        return self._chatrooms
    
    @property
    def getUsers(self):
        return self._users
    
    def generateUserIdentifier(self):
        #generates unique user ID
        self._userCounter += 1
        return self._userCounter
    
    def generateChatroomIdentifier(self):
        #generates unique chatroom ID
        self._chatroomCounter += 1
        return self._chatroomCounter
    
    def getChatroom(self, chatroomIdentifier):
        #returns chatroom object given chatroom identifier
        for i in range(len(self._chatrooms)):
            if self._chatrooms[i].getChatroomIdentifier == chatroomIdentifier:
                return self._chatrooms[i]
        return None
    
    def getUser(self, userIdentifier):
        #returns user object given user identifier
        for i in range(len(self._users)):
            if self._users[i].getUserIdentifier == userIdentifier:
                return self._users[i]
        return None
    
    def createChatroom(self, lifetime, chatName):
        newChatroom = Chatroom(self, lifetime, self.generateChatroomIdentifier(), chatName)
        self._chatrooms.append(newChatroom)
        return newChatroom
        
    def deleteChatroom(self, chatroomIdentifier):
        chatroomToDelete = self.getChatroom(chatroomIdentifier)
        if chatroomToDelete in self._chatrooms:
            chatroomToDelete.removeAllUsers()
            self._chatrooms.remove(chatroomToDelete)
            return chatroomToDelete
        return None
    
    def createUser(self, name):
        newUser = User(name, self.generateUserIdentifier())
        self._users.append(newUser)
        return newUser
        
    def deleteUser(self, userIdentifier):
        userToDelete = self.getUser(userIdentifier)
        if userToDelete in self._users:
            self._users.remove(userToDelete)
        return userToDelete
            
    def connectUserToChatroom(self, userIdentifier, chatroomIdentifier):
        #finds user object, finds chatroom object, then connects user to chatroom
        userToConnect = self.getUser(userIdentifier)
        chatroomToConnect = self.getChatroom(chatroomIdentifier)
        if userToConnect != None and chatroomToConnect != None:
            connectUserToRoom = chatroomToConnect.addUser(userToConnect)
            connectRoomToUser = userToConnect.setCurrentChatroom(chatroomToConnect)
            return (connectUserToRoom, connectRoomToUser)
        return None
    
    def disconnectUserFromChatroom(self, userIdentifier, chatroomIdentifier):
        #finds user object, finds chatroom object, then disconnects user from chatroom
        userToDisconnect = self.getUser(userIdentifier)
        chatroomToDisconnectFrom = self.getChatroom(chatroomIdentifier)
        if userToDisconnect != None and chatroomToDisconnectFrom != None:
            disconnectUserFromRoom = chatroomToDisconnectFrom.removeUser(userToDisconnect)
            disconnectRoomFromUser = userToDisconnect.setCurrentChatroom(None)
            return (disconnectUserFromRoom,disconnectRoomFromUser)
        return None
    
    def sendMessage(self, userIdentifier, message):
        #finds user, finds the chatroom the user is in, then sends the message in the chatroom object's message list
        userSendingMessage = self.getUser(userIdentifier)
        chatroomToSendMessage = userSendingMessage.getCurrentChatroom
        if chatroomToSendMessage != None and userSendingMessage != None:
            sendMessageToChatroom = chatroomToSendMessage.sendMessage(userSendingMessage, message)
            return sendMessageToChatroom
        return message
    
    