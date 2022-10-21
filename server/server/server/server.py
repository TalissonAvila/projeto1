# server side

from typing import BinaryIO
from socket import *


class Server:
    def __init__(self):
        """Construct"""
        self.host = gethostname()
        self.port = 55551
        self.server = socket(AF_INET, SOCK_STREAM)

    def server_connection(self):
        """Binds socket to address.Then shows IP and port on terminal.

        Args:
            None.
        Returns:
            None.
        """
        self.server.bind((self.host, self.port))
        print(f'HOST: {self.host} | PORT: {self.port}')

    def listened_time(self):
        """Specifies the number of unaccepted connections that the server will allow, five,  before refusing
         new connections.

        Returns:
            None.

        Args:
            None.
        """
        self.server.listen(5)

    def running_connection(self, file_path: BinaryIO):
        """Accepts the connection from client and writes the file with length of 1024 bytes. After completed,
        closes the server connection, show's it on terminal.

        Args:
            file_path (BinaryIO): receive the location where the file it will be on server.

        Returns:
            None.
        """
        connection, address = self.server.accept()
        read_buffer = connection.recv(1024)
        while read_buffer:
            file_path.write(read_buffer)
            read_buffer = connection.recv(1024)
        connection.close()
        print('Connection closed.')

    @staticmethod
    def close_file(file_path: BinaryIO):
        """Closes the file connection and shows it on terminal that the file was received.

        Args:
            file_path (BinaryIO):

        Returns:
            None.
        """
        file_path.close()
        print('file received.')

    @staticmethod
    def file_path_server() -> BinaryIO:
        """Chooses the file path on server side and opens, then prepare to write.

        Args:
            None.

        Returns:
            file_path (BinaryIO): the file location on server side.
        """
        file_path = open("uploads/file_rcv.mp3", 'wb')
        return file_path

    @staticmethod
    def close_server(self):
        """Closes the server connection then shows it on terminal.

        Args:
            None.
        Returns:
            None.
        """
        self.server.close()
        print('Server closed.')

    def main(self):
        """Main function that open connections, that defines five as listening time. Receives the file from client then
        saves on an 'uploads' folder. Then closes: connection, file and server.
        """
        Server.server_connection(self)
        Server.listened_time(self)
        file = Server.file_path_server()
        Server.running_connection(self, file)
        Server.close_file(file)
        Server.close_server(self)


server = Server()
server.main()
