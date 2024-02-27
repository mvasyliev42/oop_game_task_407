class ServerSocketTreads:
    def connectPlayer1(self, connect):
        self._connect1 = connect
        
    
    def connectPlayer2(self, connect):
        self._connect2 = connect
        
    
    def sendMessagesPlayer1(self, messages):
        self._connect1.send(messages.encode())


    def sendMessagesPlayer2(self, messages):
        self._connect2.send(messages.encode())

    def recvMessagesPlayer1(self):
        return self._connect1.recv(1024).decode()

    def recvMessagesPlayer2(self):
        return self._connect2.recv(1024).decode()