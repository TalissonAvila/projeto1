Server side:
Opens a connection and waits to receive file. When establishing the connection, it receives the file divided into sizes of 1024 bytes. After receiving it complete, it closes the connection and the server.
This procedure it will happens on port 55551 and IP will be from localhost's user trought 'gethostname()' method.