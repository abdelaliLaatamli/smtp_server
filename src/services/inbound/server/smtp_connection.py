import socket
import threading
from .connection_queue import ConnectionQueue

class SMTPConnection:

    _connection:socket=None
    _address=None

    def __init__(self , connection:socket , address ):
        self._connection = connection
        self._address = address

    def start_connection(self):
        self._connection.send(str.encode('Server is working:\r\n'))
        while True:
            data = self._connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')
            if not data:
                break
            if data.decode().rstrip() == 'quit' or data.decode().rstrip() == 'q':
                self._connection.sendall("bye".encode())
                break
            self._connection.sendall(str.encode(response))
        
        
        print(f"current thread {threading.current_thread().ident} is closing ....")
        ConnectionQueue().dequeue_connection(threading.current_thread().ident)
        self._connection.close() 
