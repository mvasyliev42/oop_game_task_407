from services.socket.basesocketserver import BaseSocketServer
from services.authorisation import Authorisation
class SocketServer(BaseSocketServer):

    def connectPlayer1(self):
        self._connect1, address = self._socket.accept()
        self.sendMessagesPlayer1("Введіть username: ")
        username = self.recvMessagesPlayer1()
        self.sendMessagesPlayer1("Введіть password: ")
        password = self.recvMessagesPlayer1()
        auth = Authorisation(username, password)
        login = auth.login()
        if login == False:
            self.sendMessagesPlayer1("Логін, або пароль не правильний!")
            #todo: придумати адекватну реалізацію неправильного паролю
            exit()
        else:
            self.sendMessagesPlayer1("Ви успішно підключилися!")
        return login
        #todo: make validation (username, password)
        #todo: return user info

    def connectPlayer2(self):
        self._connect2, address = self._socket.accept()
        self.sendMessagesPlayer2("Введіть username: ")
        username = self.recvMessagesPlayer2()
        self.sendMessagesPlayer2("Введіть password: ")
        password = self.recvMessagesPlayer2()
        auth = Authorisation(username, password)
        login = auth.login()
        if login == False:
            self.sendMessagesPlayer2("Логін, або пароль не правильний!")
            # todo: придумати адекватну реалізацію неправильного паролю
            exit()
        else:
            self.sendMessagesPlayer2("Ви успішно підключилися!")
        return login
        #todo: make validation (username, password)
        #todo: return user info
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

    def sendMessagesPlayer1(self, messages):
        self._connect1.send(messages.encode())

    def sendMessagesPlayer(self, messages):
        self._connect1.send(messages.encode())

    def sendMessagesPlayer2(self, messages):
        self._connect2.send(messages.encode())

    def recvMessagesPlayer1(self):
        return self._connect1.recv(1024).decode()

    def recvMessagesPlayer2(self):
        return self._connect2.recv(1024).decode()

    def recvMessagesPlayer(self):
        return self._connect1.recv(1024).decode()

    def get_connect(self):
        return self._connect