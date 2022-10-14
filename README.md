# projeto1
 implementar um envio de arquivo do cliente para o servidor utilizando poetry com os seguintes requisitos: cliente e servidor com poetry's proprio;  snake_case; docstring (função do método, entrada e saída) usando padrão google).

## Solving this propoused problem:
###  . Client side:
It receives the file inside its folders, and initiates a connection with the server, sending this file in a size of 1024 bytes.
This procedure it will happens on port 55551 and IP will be from desktop's user trought __gethostname()__ method.


###  . Server side:
Opens a connection and waits to receive file. When establishing the connection, it receives the file divided into sizes of 1024 bytes. After receiving it complete, it closes the connection and the server.
This procedure it will happens on port 55551 and IP will be from localhost's user trought __gethostname()__ method.