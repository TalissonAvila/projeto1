# server side
from socket import *


def recieve_file():
    """Opens a connection and waits to receive file. When establishing the connection, it receives the file divided into
    sizes of 1024 bytes. After receiving it complete, it closes the connection and the server.

    Args:
        None.

    Return:
        None.
    """
    host = gethostname()
    port = 55551
    print('Runing server.')
    print(f'HOST: {host} | PORT: {port}')
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    running = 1
    while running == 1:
        fd, address = server.accept()
        file_path = open("uploads/file_rcv.mp3", 'wb')
        end = 0
        while end == 0:
            read_buffer = fd.recv(1024)
            while read_buffer:
                file_path.write(read_buffer)
                read_buffer = fd.recv(1024)
                end = 1
            file_path.close()
            print('File recieved.')
            fd.close()
            running = 0
            print('Connection closed.')
    server.close()
    print('Server closed.')


recieve_file()
