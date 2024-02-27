from services.socket.basesocketserver import BaseSocketServer
from services.authorisation import Authorisation
class SocketServer(BaseSocketServer):

    

    
    def connectPlayer(self):
        self._connect, address = self._socket.accept()
        self.sendMessagesPlayer("Введіть username: ")
        username = self.recvMessagesPlayer()
        self.sendMessagesPlayer("Введіть password: ")
        password = self.recvMessagesPlayer()
        auth = Authorisation(username, password)
        login = auth.login()
        if login == False:
            self.sendMessagesPlayer("Логін, або пароль не правильний!")
            # todo: придумати адекватну реалізацію неправильного паролю
            exit()
        else:
            self.sendMessagesPlayer("Ви успішно підключилися!")
        return login

   

    def sendMessagesPlayer(self, messages):
        self._connect1.send(messages.encode())

    

   

    def recvMessagesPlayer(self):
        return self._connect1.recv(1024).decode()

    def get_connect(self):
        return self._connect