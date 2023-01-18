import socket
import threading

class SMTPConnection:

    _connection:socket=None
    _server_smtp:any=None
    _address=None

    def __init__(self , connection:socket , address , server_smtp ):
        self._connection = connection
        self._address = address
        self._server_smtp = server_smtp

    def start_connection(self):
        self._connection.send(str.encode('Server is working:\r\n'))
        while True:
            data = self._connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')
            if not data:
                break
            if data.decode().rstrip() == 'quit' :
                self._connection.sendall("bye".encode())
                break
            self._connection.sendall(str.encode(response))
        print(f"current thread {threading.current_thread().ident} is closing ....")
        self._connection.close()
        print( len(self._server_smtp.threads) )
        self._server_smtp.threads.pop(threading.current_thread().ident)
        print( len(self._server_smtp.threads) )