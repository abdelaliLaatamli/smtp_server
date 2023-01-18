
import socket
import threading 
from .smtp_connection import SMTPConnection
from .connection_queue import ConnectionQueue

class ServerSMTP:

    _host:str="0.0.0.0"
    _port:int=25
    _server_socket:socket=None

    def __init__( self, host , port) -> None:
        self._host = host
        self._port = port
        self._server_socket:socket.socket = socket.socket()


    def start(self):

        try:
            self._server_socket.bind((self._host, self._port))
            print(f"Server SMTP is STARTED in {self._host}:{self._port}")
        except socket.error as e:
            raise Exception( f"Can't connect to this ip port couse of {str(e)}")

        # put on listening mode
        self._server_socket.listen(5)

        while True:
            client, address = self._server_socket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            thread = threading.Thread( target= SMTPConnection( client , address ).start_connection )
            ConnectionQueue().addConnectionthread(thread)
        
        print("server finished")

    
    def stop(self):
        if self._server_socket != None:
            self._server_socket.close()
