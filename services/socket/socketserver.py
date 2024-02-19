from services.socket.basesocketserver import BaseSocketServer


class SocketServer(BaseSocketServer):

    def connectPlayer1(self):
        self._connect1, address = self._socket.accept()
        #todo: make validation (username, password)
        #todo: return user info

    def connectPlayer2(self):
        self._connect2, address = self._socket.accept()
        #todo: make validation (username, password)
        #todo: return user info

    def sendMessagesPlayer1(self, messages):
        self._connect1.send(messages.encode())

    def sendMessagesPlayer2(self, messages):
        self._connect2.send(messages.encode())

    def recvMessagesPlayer1(self):
        return self._connect1.recv(1024).decode()

    def recvMessagesPlayer2(self):
        return self._connect2.recv(1024).decode()
