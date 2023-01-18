
import socket
import threading 
from .smtp_connection import SMTPConnection

class ServerSMTP:

    _host:str="0.0.0.0"
    _port:int=25
    _server_socket:socket=None
    threads={}

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
            # threading.Thread( target= self.multi_threaded_client , args=( client, address ) ).start()
            thread = threading.Thread( target= SMTPConnection( client , address , self ).start_connection )
            if( len(self.threads) < 2 ):
                thread.start()
                self.threads[thread.ident] = thread
                # self.threads.append()
            print(thread.ident , thread )

    
    def multi_threaded_client(self , connection , address):
        smtp = SMTPConnection(connection , address)
        smtp.start_connection()
        # connection.send(str.encode('Server is working:\r\n'))
        # while True:
        #     data = connection.recv(2048)
        #     response = 'Server message: ' + data.decode('utf-8')
        #     if not data:
        #         break
        #     if data.decode().rstrip() == 'quit' :
        #         connection.sendall("bye".encode())
        #         break
        #     connection.sendall(str.encode(response))
        # connection.close()
    
    def stop(self):
        if self._server_socket != None:
            self._server_socket.close()
