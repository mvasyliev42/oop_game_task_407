import socket
import threading


def client_program():
    host = socket.gethostname()  # "151.115.78.136" # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # message = input(" -> ") # take input
    message = ""
    while message.lower().strip() != 'bye':
        data = client_socket.recv(1024).decode()  # receive response

        print("Server: ", data)  # show in terminal

        message = input(" -> ")  # again take input

        client_socket.send(message.encode())  # send message

    client_socket.close()  # close the connection


def recv():
    global client_socket

    while True:
        data = client_socket.recv(1024).decode()
        print(data)


def send():
    global client_socket
    while True:
        message = input(" -> ")
        client_socket.send(message.encode())


if __name__ == '__main__':
    host = socket.gethostname()  # "151.115.78.136" # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    thread1 = threading.Thread(target=recv)
    thread2 = threading.Thread(target=send)

    thread1.start()
    thread2.start()

    # client_program()
