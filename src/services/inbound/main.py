import socket
import os
from _thread import *
from concurrent.futures import ThreadPoolExecutor

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
executor = ThreadPoolExecutor(3)
# pool = multiprocessing.Pool.ThreadPool(processes=3)

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection , address):

    connection.send(str.encode('Server is working:\r\n'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        if data.decode().rstrip() == 'quit' :
              connection.sendall("bye".encode())
              break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    # multi_threaded_client(client, address )
    start_new_thread(multi_threaded_client, ( client, address ))
    # executor.submit( multi_threaded_client , ( client, address ) )
    #ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    

ServerSideSocket.close()