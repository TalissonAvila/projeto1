# client side
from socket import *


def send_file(path: str):
    """It receives the file inside its folders, and initiates a connection with the server, sending this file in
     a size of 1024 bytes.

    Args:
        path (str) : Path/file.extension.

    Return:
        None.
    """
    host = gethostname()
    port = 55551
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))
    file_path_client_side = open(path, "rb")
    read_buffer = file_path_client_side.read()

    while read_buffer:
        client.send(read_buffer)
        read_buffer = file_path_client_side.read(1024)
        print('sending file...')
    client.close()
    print('file sent.')


file_path = str("C:/!!Coisas Importantes!!/song1.mp3")
send_file(file_path)
