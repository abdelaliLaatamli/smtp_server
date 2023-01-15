import socket
import ssl
import os
import base64

certchain = f"{os.getcwd()}{os.sep}keys{os.sep}certchain.pem"
private = f"{os.getcwd()}{os.sep}keys{os.sep}private.key"

HOST = "smtp.office365.com"  # The server's hostname or IP address
PORT = 587  # The port used by the server
# PORT = 25  # The port used by the server

context = ssl.create_default_context()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #s.bind(("51.222.146.133",59166))


    s.settimeout(10)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode())

    # s.send(b"EHLO smtp.gmail.com\r\n")
    s.send(b"EHLO smtp.office365.com\r\n")
    data = s.recv(1024)
    print(data.decode())

    s.send(b"starttls\r\n")

    data = s.recv(1024)
    print(data.decode())

    # without warning 
    # s = context.wrap_socket(s, server_hostname=HOST)

    #with warning 
    #s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)

    s.send(b"AUTH LOGIN\r\n")
    data = s.recv(1024)
    print(data.decode())

    s.send( f"{base64.b64encode(b'abdelalilaatamli@outlook.fr').decode()}\r\n".encode() )
    data = s.recv(1024)
    print(data.decode())


    s.send( f"{base64.b64encode(b'@Abdo@1993@').decode()}\r\n".encode() )
    data = s.recv(1024)
    print(data.decode())


    
    s.send( "MAIL FROM: <abdelalilaatamli@outlook.fr>\r\n".encode() )
    data = s.recv(1024)
    print(data.decode())

    s.send( "RCPT TO: <abdo332015@gmail.com>\r\n".encode() )
    data = s.recv(1024)
    print(data.decode())

    s.send( "DATA\r\n".encode() )
    data = s.recv(1024)
    print(data.decode())
    

    s.send( b"Subject: test\r\n")
    s.send( b"This is a line in the email.\nThis is a second line in the email." )
    s.send( b"\r\n.\r\n")
    #s.send( b"Subject: test\r\nThis is a line in the email.\nThis is a second line in the email.\r\n.\r\n" )
    data = s.recv(1024)
    print(data.decode())


    s.send( b"QUIT\r\n" )
    data = s.recv(1024)
    print(data.decode())


    # quit rset

    # print("Message after connection request:" + recv)

#print(f"Received {data!r}")