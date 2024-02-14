import socket


def client_program():
    host = socket.gethostname() # "151.115.78.136" # as both code is running on same pc
    port = 5000 # socket server port number

    client_socket = socket.socket() # instantiate
    client_socket.connect((host, port)) # connect to the server

    #message = input(" -> ") # take input
    message = ""
    while message.lower().strip() != 'bye':

        data = client_socket.recv(1024).decode() # receive response

        print("Server: ", data) # show in terminal

        message = input(" -> ") # again take input

        client_socket.send(message.encode()) # send message


    client_socket.close() # close the connection


if __name__ == '__main__':
    client_program()