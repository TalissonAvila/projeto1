# client side

from typing import BinaryIO
from socket import *


class Client:
    def __init__(self):
        """Construct"""
        self.host = gethostname()
        self.port = 55551
        self.client = socket(AF_INET, SOCK_STREAM)

    def client_connection(self):
        """Connects the client using host by 'gethostname()' method and port by port 55551.

        Args:
            None.

        Returns:
            None.
        """
        self.client.connect((self.host, self.port))

    @staticmethod
    def open_file(path: str) -> BinaryIO:
        """Receive the path where the file is located and returns the file opened.

        Args:
            path(str): the Path/file.exe where the file is located.

        Returns:
            the file opened.
        """
        file_path_client_side = open(path, "rb")
        return file_path_client_side

    @staticmethod
    def read_file(file_open: BinaryIO) -> bytes:
        """Receive the file open and reads it into a variable in a form of bytes.

        Args:
            file_open (BinaryIO): the opened binary file.

        Returns:
            the file open in a form of bytes.
        """
        read_buffer = file_open.read()
        return read_buffer

    def send_file(self, read_buffer: bytes, file_opened: BinaryIO):
        """Receives the file open in a form of bytes and sends to server with length of 1024 bytes.

        Args:
            read_buffer (bytes): the file divided with length of 1024 bytes.
            file_opened (BinaryIO): the opened binary file.

        Returns:
             None.
        """
        while read_buffer:
            self.client.send(read_buffer)
            read_buffer = file_opened.read(1024)
            print('sending file...')

    def close_client(self):
        """After finishing uploading the file, closes the client-side connection.

        Args:
            None.

        Returns:
            None.
        """
        self.client.close()
        print('file sent.')

    def main(self):
        """Main function that receives the location of the file, establish a connection, open the file in a form of
         bytes and sends to server.
        """
        file_path = str("C:/!!Coisas Importantes!!/song1.mp3")
        Client.client_connection(self)
        open_file = Client.open_file(file_path)
        read_buffer = Client.read_file(open_file)
        Client.send_file(self, read_buffer, open_file)
        Client.close_client(self)


client = Client()
client.main()
