import socket

class BaseSocketServer:

    def __init__(self):
        self._connect1 = None
        self._connect2 = None

        # get the hostname
        host = socket.gethostname()
        port = 5001  # initiate port no above 1024

        self._socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        self._socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        self._socket.listen(2)

    def connectPlayer1(self):
        pass

    def connectPlayer2(self):
        pass

    def sendMessagesPlayer1(self, messages):
        pass

    def sendMessagesPlayer2(self, messages):
        pass

    def recvMessagesPlayer1(self):
        pass

    def recvMessagesPlayer2(self):
        pass


    def __del__(self):
        self._connect1.close()
        self._connect2.close()



# conn, address = server_socket.accept()  # accept new connection
# print("Connection from: " + str(address))
#
# data = conn.recv(1024).decode()
# conn.send(data.encode())
