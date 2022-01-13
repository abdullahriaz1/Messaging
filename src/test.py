#testing how to transfer properties between objects using classes
class One(object):
    def __init__(self):
        self.x = 1
        self.list = []
        
    def transferX(self,other):
        other.list.append(self.x)
        print(other.list)
f = One()
y = One()
f.transferX(y)
f.transferX(y)
f.transferX(y)

#testing the implementation of our messaging handler
from handler import Handler
s = Handler()
s.createUser('Myself')
s.createUser('My Homie')
print([user.getUserIdentifier for user in s.getUsers])
print([user.getName for user in s.getUsers])

s.createChatroom(12,'myroom1')
s.createChatroom(12,'myroom2')
print([chatroom.getChatroomIdentifier for chatroom in s.getChatrooms])

s.connectUserToChatroom(1,1)
s.connectUserToChatroom(2, 2)
print([chatroom.getUsersInChatroom for chatroom in s.getChatrooms])

s.disconnectUserFromChatroom(2,2)
print([chatroom.getUsersInChatroom for chatroom in s.getChatrooms])

s.sendMessage(1,"Hello World")
print([[message.getMessage for message in chatroom.getMessages] for chatroom in s.getChatrooms])

print([user.getName for user in s.getUsers])
print([[user.getName for user in chatroom.getUsersInChatroom] for chatroom in s.getChatrooms])

s.deleteChatroom(2)
print([chatroom for chatroom in s.getChatrooms])

s.deleteChatroom(1)
print([chatroom for chatroom in s.getChatrooms])

s.deleteChatroom(100)
print([chatroom for chatroom in s.getChatrooms])

print(s.deleteChatroom(10000))